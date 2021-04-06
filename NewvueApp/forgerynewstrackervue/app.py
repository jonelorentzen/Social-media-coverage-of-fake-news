from flask import Flask, jsonify, redirect, request, url_for
from flask_cors import CORS
import requests
import json
import os
import time
import praw
import geocoder
from datetime import datetime


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['TESTING'] = True


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


#Getting data from TWITTER
def auth():
    return os.environ.get("BEARER_TOKEN")

def create_url(query):
    tweet_fields = "tweet.fields=public_metrics,created_at,geo,referenced_tweets,text,author_id,id,in_reply_to_user_id"
    max_results = "max_results=100"
    user_fields = "user.fields=profile_image_url"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}&{}".format(
        query, tweet_fields, user_fields ,max_results
        )
    return url

def create_id_url(query):
   
    tweet_fields = "tweet.fields=public_metrics,created_at,geo,lang,referenced_tweets,text,author_id,in_reply_to_user_id"
    user_fields = "user.fields=profile_image_url"
    url = "https://api.twitter.com/2/tweets?ids={}&{}&{}".format(
        query, tweet_fields, user_fields
        )
    return url

def create_users_url(query):

    user_fields= "user.fields=location,name,profile_image_url,public_metrics,username,verified"
    url = "https://api.twitter.com/2/users?ids={}&{}".format(
        query, user_fields
    )
    return url

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAEYbLwEAAAAA2QFmIRNmiAc3uEuMAPT9AoknvZw%3D7rtwFRPtWgSFp70bogE1sBP1WzqkR5cubh9vlN2COt9AiT6kfk"}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

@app.route('/showinfo', methods=['GET', 'POST'])
def showinfo():
    d = request.json
    print(d)

    #Reddit API call, time displayed in unix

    reddit = praw.Reddit(
    client_id="UK5XRgvcO7C2cQ",
    client_secret="9OIo7S6kOBLlQZadOlo5miG0A9OC4g",
    user_agent="my user agent")

    reddit_data = []

    for submission in reddit.subreddit("all").search(d["query"], limit=100):
       reddit_data.append({"title": str(submission.title), "update_ratio": str(submission.upvote_ratio), "upvotes": str(submission.ups),
       "url": str(submission.url), "created_at": str(submission.created_utc), "subreddit": str(submission.subreddit), "number_of_comments": str(submission.num_comments)})
    
       
    #Create the token to get acess to the Twitter 
    bearer_token = auth()
    headers = create_headers(bearer_token)


    #API call to get back a dictionary with 10 api call without any duplicates
    json_response = api_caller(d["query"], headers)
    # New call to the the Twitter API that uses the ID of the retweeted tweets and adds the data of the original tweets to the dictionary
    #The create_id_url creates the url that is used to call the api with.
    ids = extract_retweets(json_response)
    url_ids = create_id_url(ids)
    json_response2 = connect_to_endpoint(url_ids, headers)
    
    for item in json_response2["data"]:
        json_response["data"].append(item)

    json_response["data"] = sorted(json_response["data"], key = lambda i: i['public_metrics']["retweet_count"],reverse=True)

    json_response3 = extract_usernames(json_response, headers)
    
    for i in range(len(json_response["data"])):
        json_response3[i]["public_metrics_user"] = json_response3[i].pop("public_metrics")
        json_response3[i]["author_id"] = json_response3[i].pop("id")
        json_response["data"][i].update(json_response3[i])
   

    #Create all of the data that is going to be displayed in the frontend from the json_response
    alldata = json_response["data"].copy()
    barchart = create_barchart(json_response)
    linechart = create_linechart(json_response)
    topposts = create_topposts(json_response)
    topusers = create_topusers(json_response)
    activity = create_activity(json_response)
    links = create_links(json_response)
    nodes = create_nodes(links)
    geochart = create_geochart(json_response)
    links = create_links(json_response)
    nodes = create_nodes(links)

    
    
    
     

    json_response["data"] = {d["query"]: {"alldata": alldata, "barchart": barchart, "linechart": linechart, "topposts": topposts, "topusers": topusers, 
    "activity": activity, "geochart": geochart, "reddit": reddit_data, "query": d["query"], "nodes": nodes, "links": links }}

    
    return json.dumps(json_response)


#The fuction api_caller is a fuction that is used to call the api 10 times and add the responses to the json_response
#We use the time libery to avoid getting the same json response back from the api, so it waits 1 second between every api call
def api_caller(query, headers):
    url = create_url(query)
    json_response = connect_to_endpoint(url, headers)

    time.time()
    count = 0
    while True:
        api_call = connect_to_endpoint(url, headers)
        for item in api_call["data"]:
            if item["id"] not in json_response["data"]:
                json_response["data"].append(item)
        
        time.sleep(2)
        count += 1
        print ("tick")

        if count == 2:
            count = 0
            break

    json_response_no_duplicates = remove_duplicates(json_response)
    return json_response_no_duplicates

#Function for removing the duplicate responses when calling the api 10 times. When searching for a query that is popular you get few duplicates from the api.
#Searching for a query that is not popular you will get many duplicates often the same from all 10 api calls.
#We use a empty dictionary that we add to and if the same value gets stored in the same key it will just be overwritten so there will be no duplicates
def remove_duplicates(json_response):           
    response_map = {}
    for i in range(len(json_response["data"])):
        key = json_response["data"][i]["id"] 
        value = json_response["data"][i]
        response_map[key] = value 

    json_response_no_duplicates = {"data":[]}
    for value in response_map.values():
        json_response_no_duplicates["data"].append(value)

    return json_response_no_duplicates

#Function for extracting the data about the orginal tweets that was retweeted. 
#The reasoning behind this is because the twitter search api returns alot of retweets of an orignal tweet.
#And when the api returns a retweet you only get the retweets not the likes, quotes or the replies of the orginal tweet.
#So we call the api for the orignal tweets that we extract from the retweets.
def extract_retweets(json_response):
    id_list = []
    tweet_dict = json_response["data"]
    for i in range(len(tweet_dict)):
        if "referenced_tweets" in tweet_dict[i]:
            if tweet_dict[i]["referenced_tweets"][0]["type"] == "retweeted":
                if tweet_dict[i]["referenced_tweets"][0]["id"] not in id_list:
                    id_list.append(tweet_dict[i]["referenced_tweets"][0]["id"])
                    if len(id_list) == 100:
                        break
    joined_string = ",".join(id_list)
    return joined_string

#Function for extracting all off the usernames and calling the API for every 100 tweet.
#Returning all of the user data that is missing from the first API call.
#With this function we get the location and stats like how many followers a user has.xz z
def extract_usernames(json_response, headers):
    author_id_list = []
    tweet_dict = json_response["data"]

    for i in range(len(tweet_dict)):
        author_id_list.append(tweet_dict[i]["author_id"])
 
    url_list = []
    for i in range(0, len(author_id_list), 100):
        chunk = author_id_list[i:i + 100]
        joined_string = ",".join(chunk)
        url_users_ids = create_users_url(joined_string)
        url_list.append(url_users_ids)

    time.time()
    count = 0
    json_response2 = connect_to_endpoint(url_list[0], headers)
    
    while True: 
        if len(url_list) == 1:
            break
        for i in range(len(url_list)-1):
            api_call = connect_to_endpoint(url_list[i+1], headers)
            for item in api_call["data"]:
                json_response2["data"].append(item)

        time.sleep(1)
        count += 1
        print("tick")
        if count == len(url_list)-1:
            count = 0
            break
        
    return json_response2["data"]


#Function to extract the total likes, retweets, replies and quotes. The API return the total retweets of the original tweet is a user has retweeted it.
#So the function does not count the retweets of a retweet. Only the retweets of the orignal tweet
def create_barchart(json_response):
    tweets = json_response["data"]
    total_retweets = 0
    total_likes = 0
    total_replies = 0
    total_quotes = 0

    for i in range(len(tweets)):
        if "referenced_tweets" in tweets[i]:
              if tweets[i]['referenced_tweets'][0]["type"] != "retweeted":
                  total_retweets += tweets[i]['public_metrics']["retweet_count"]
                  total_likes += tweets[i]['public_metrics']["like_count"]
                  total_replies += tweets[i]['public_metrics']["reply_count"]
                  total_quotes += tweets[i]['public_metrics']["quote_count"]
        else:
              total_retweets += tweets[i]['public_metrics']["retweet_count"]
              total_likes += tweets[i]['public_metrics']["like_count"]
              total_quotes += tweets[i]['public_metrics']["quote_count"]
              total_replies += tweets[i]['public_metrics']["reply_count"]
       
    barchartlist = [['Likes', total_likes], ['Retweeets', total_retweets],['Replies', total_replies],['Quotes',total_quotes]]

    return barchartlist

#Function to make a list that is needed to display the areachart   
def create_linechart(json_response):
    tweets = json_response["data"]
    allDates = []
    finalDates = {}
    
      
    for i in range(len(tweets)):
        element = tweets[i]["created_at"]
        allDates.append(element)

    for i in range(len(tweets)):
        allDates[i] = allDates[i].replace(".000Z", "")

    allDates.sort() 
    allDates = allDates[7:]

    for i in range(len(allDates)):
        finalDates[allDates[i]]=i+1

    
          
    return finalDates

#Function that returns the dates from when a person retweets a tweet
def create_retweet_linechart(json_response):
    tweets = json_response["data"]
    allDates = []
    finalDates = []
      
    for i in range(len(tweets)):
        if "referenced_tweets" in tweets[i]:
              if tweets[i]['referenced_tweets'][0]["type"] == "retweeted":
                    element = tweets[i]["created_at"]
                    allDates.append(element)
 

    for i in range(len(tweets)):
        allDates[i] = allDates[i].replace(".000Z", "")

    allDates.sort() 
    allDates = allDates[5:]
    
    for i in range(len(allDates)):
        finalDates.append([allDates[i],i+1])
          
    return finalDates

#Function the extract the top 3 post and returns a dictonary with all the data needed to display as a tweet
def create_topposts(json_response):
    tweets = json_response["data"]
    topposts = []
    for i in range(len(tweets)):
        if "referenced_tweets" not in tweets[i]:
            date = format_date(tweets[i]["created_at"])
            topposts.append({"author_id": tweets[i]["author_id"], "retweets": tweets[i]['public_metrics']["retweet_count"], "likes": tweets[i]['public_metrics']["like_count"], "text": tweets[i]['text'],
            "username": tweets[i]["username"], "img": tweets[i]["profile_image_url"], "date": date, "followers": tweets[i]['public_metrics_user']["followers_count"], "verified": tweets[i]["verified"], "id": tweets[i]["id"]})
            if len(topposts) == 3:
                break

    return topposts


#Maybe add functionality that returns day and month like 13 Feb...
def format_date(timestamp):
    ts = time.strptime(timestamp[:19], "%Y-%m-%dT%H:%M:%S")
    s = time.strftime("%m/%d/%Y", ts)
    return s

#Function for extracting the top 9 users with the most followers with a check that is not added 
def create_topusers(json_response):
    tweets = json_response["data"]
    topusers = []
    for i in range(len(tweets)):
        if tweets[i] not in topusers:
            topusers.append({"username": tweets[i]["username"], "img": tweets[i]["profile_image_url"], "followers": tweets[i]['public_metrics_user']["followers_count"], "verified": tweets[i]["verified"]})
            if len(topusers) == 9:
                break
    sorted_topusers = sorted(topusers, key = lambda i: i['followers'],reverse=True)
    return sorted_topusers

#Function to extact the data displayed in the yellow header. Returning a dictionary with the total posts, users and engagement
#Users is only users that is posting something not a user that is retweeting. Total posts is the total tweets, replies and quotes. 
#Engangement is likes and retweets
def create_activity(json_response):
    activity = {}
    tweets = json_response["data"]
    user_ids = []
    
    engagement = 0 
    total_posts = 0
    for i in range(len(tweets)):
        if "referenced_tweets" in tweets[i]:
              if tweets[i]['referenced_tweets'][0]["type"] != "retweeted":
                  engagement += tweets[i]['public_metrics']["retweet_count"]
                  engagement += tweets[i]['public_metrics']["like_count"]
                  total_posts += 1   
                  if tweets[i]["author_id"] not in user_ids:
                      user_ids.append(tweets[i]["author_id"])          
        else:
              engagement += tweets[i]['public_metrics']["retweet_count"]
              engagement += tweets[i]['public_metrics']["like_count"]
              total_posts += 1
              if tweets[i]["author_id"] not in user_ids:
                      user_ids.append(tweets[i]["author_id"])
            
    activity["posts"] = total_posts
    activity["users"] = len(user_ids)
    activity["engagement"] = engagement

    return activity

def create_links(json_response):

    links = []

    tweets = json_response["data"]
    for i in range(len(tweets)):
        if "referenced_tweets" in tweets[i]:
            if tweets[i]['referenced_tweets'][0]["type"] == "retweeted":
                text = tweets[i]['text']
                idxAt = text.find('@')
                idxCo = text.find(':')
                tweet_id = tweets[i]['id']
                followers = tweets[i]['public_metrics_user']['followers_count']

                if followers <= 10000:
                    size = 3
                elif followers <= 50000:
                    size = 5
                elif followers <= 100000:
                    size = 7
                elif followers <= 1000000:
                    size = 10
                elif followers > 1000000:
                    size = 13

                print(text[idxAt+1:idxCo])
                links.append({'source': text[idxAt+1:idxCo], 'target': tweets[i]['username'], 'size':size})


            elif tweets[i]['referenced_tweets'][0]["type"] == "replied_to":
                text = tweets[i]['text']
                idxAt = text.find('@')
                idxS = text.find(' ')
                followers = tweets[i]['public_metrics_user']['followers_count']

                if followers <= 10000:
                    size = 3
                elif followers <= 50000:
                    size = 5
                elif followers <= 100000:
                    size = 7
                elif followers <= 1000000:
                    size = 10
                elif followers > 1000000:
                    size = 13

                print(text[idxAt:idxS])
                links.append({'source': text[idxAt+1:idxS], 'target': tweets[i]['username'], 'size':size})

    return links


def create_nodes(links):
    nodes = []
    for i in range(len(links)):
        if links[i]['source'] not in nodes:

            nodes.append({"id":links[i]['source'], 'size':links[i]['size']})
        
        if links[i]['target'] not in nodes:
            nodes.append({"id":links[i]['target'], 'size':links[i]['size'] })
    print(nodes)
    return nodes


def create_geochart(json_response):
    all_locations = []
    tweets = json_response["data"]
    for tweet in tweets:
        if "location" in tweet:
            all_locations.append(tweet["location"])
            if len(all_locations) == 99:
                break
 
    all_countries = []
   
    g = geocoder.mapquest(all_locations, method='batch', key="DW8AsY8QcWjfHn5wzHK769LT4LwAK0l6")
    for result in g:
        all_countries.append(str(result.country))
        
    
    geochart = dict((x,all_countries.count(x)) for x in set(all_countries))

    # all_countries = []
    # g = geocoder.bing(all_locations, method='batch_reverse', key="AqcxdNzZ8kzbAdu6-q3McqsTRC3qsc2CjNAkwIxfVMPj8mhEqppdBE7GUL3OKS0n")
    # for result in g:
    #     all_countries.append(str(result.country))
    #     print(result.country)

    # geochart = dict((x,all_countries.count(x)) for x in set(all_countries))

    return geochart


if __name__ == '__main__':
    app.run(debug=True)

"export FLASK_DEBUG=ON"
