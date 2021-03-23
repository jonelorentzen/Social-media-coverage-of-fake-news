from flask import Flask, jsonify, redirect, request, url_for
from flask_cors import CORS
import requests
import json
import os
import time
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


#Getting data from TWITTER
def auth():
    return os.environ.get("BEARER_TOKEN")

def create_url(query):
    tweet_fields = "tweet.fields=public_metrics,created_at,geo,referenced_tweets,text,author_id"
    max_results = "max_results=100"
    user_fields = "user.fields=profile_image_url"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}&{}".format(
        query, tweet_fields, user_fields ,max_results
        )
    return url

def create_id_url(query):
   
    tweet_fields = "tweet.fields=public_metrics,created_at,geo,lang,referenced_tweets,text,author_id"
    user_fields = "user.fields=profile_image_url"
    url = "https://api.twitter.com/2/tweets?ids={}&{}&{}".format(
        query, tweet_fields, user_fields
        )
    return url

def create_users_url(query):

    user_fields= "user.fields=id,location,name,profile_image_url,public_metrics,username,verified"
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

    user_ids = extract_usernames(json_response)
    url_users_ids = create_users_url(user_ids)
    json_response3 = connect_to_endpoint(url_users_ids, headers)
        
    for i in range(99):
        json_response3["data"][i]["public_metrics_user"] = json_response3["data"][i].pop("public_metrics")
        json_response["data"][i].update(json_response3["data"][i])
    
    
    #Create Barchart and LineChart from json_response
    barchart = create_barchart(json_response)
    linechart = create_linechart(json_response)
    topposts = create_topposts(json_response)
    topusers = create_topusers(json_response)
    #all text
    allText = all_text(json_response)
    print(type(allText))
    print(allText)

     
    json_response["data"] = {d["query"]: {"barchart": barchart, "linechart": linechart, "topposts": topposts, "topusers": topusers, "alltext": allText}}
    sentiment = show_tweets_text_sentiment(json_response)
    json_response["data"][d["query"]]["sentiment"] = sentiment
    return json.dumps(json_response)

def extract_usernames(json_response):
    author_id_list = []
    tweet_dict = json_response["data"]
    for i in range(99):
        author_id_list.append(tweet_dict[i]["author_id"])

    joined_string = ",".join(author_id_list)
    return joined_string


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
        
        time.sleep(1)
        count += 1
        print ("tick")

        if count == 1:
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
    
def create_linechart(json_response):
    tweets = json_response["data"]
    allDates = []
    finalDates = []
      
    for i in range(len(tweets)):
        element = tweets[i]["created_at"]
        allDates.append(element)

    for i in range(len(tweets)):
        allDates[i] = allDates[i].replace(".000Z", "")

    allDates.sort()

    for i in range(len(tweets)):
        finalDates.append([allDates[i],i+1])
          
    return finalDates

def create_topposts(json_response):
    tweets = json_response["data"]
    topposts = []
    for i in range(len(tweets)):
        if "referenced_tweets" not in tweets[i]:
            date = format_date(tweets[i]["created_at"])

            topposts.append({"author_id": tweets[i]["author_id"], "retweets": tweets[i]['public_metrics']["retweet_count"], "likes": tweets[i]['public_metrics']["like_count"], "text": tweets[i]['text'],
            "username": tweets[i]["username"], "img": tweets[i]["profile_image_url"], "date": date, "followers": tweets[i]['public_metrics_user']["followers_count"], "verified": tweets[i]["verified"]})
            if len(topposts) == 3:
                break

    return topposts

def all_text(json_response):
    tweets = json_response["data"]
    allText = []
    for i in range(len(tweets)):
        allText.append({"tweets_text": tweets[i]["text"]})
    return allText



#Maybe add functionality that returns day and month like 13 Feb...
def format_date(timestamp):
    ts = time.strptime(timestamp[:19], "%Y-%m-%dT%H:%M:%S")
    s = time.strftime("%m/%d/%Y", ts)
    return s

def create_topusers(json_response):
    tweets = json_response["data"]
    topusers = []
    for i in range(len(tweets)):
        topusers.append({"username": tweets[i]["username"], "img": tweets[i]["profile_image_url"], "followers": tweets[i]['public_metrics_user']["followers_count"], "verified": tweets[i]["verified"]})
        if len(topusers) == 9:
            break
    sorted_topusers = sorted(topusers, key = lambda i: i['followers'],reverse=True)
    return sorted_topusers

def create_activity(json_response):
    tweets = json_response["data"]
    user_ids = []
    for i in range(len(tweets)):
        user_ids.append(tweets[i]["author_id"])
    # print(len(user_ids))
    list(dict.fromkeys(user_ids))
    # print(len(user_ids))

# https://betterprogramming.pub/twitter-sentiment-analysis-15d8892c0082
#####################################
#########      SENTIMENT   ##########
#########       TWEETS     ##########
#####################################
# 1) Get the text of every tweet. 
# 2) put each tweet in a DataFrame
# 3) remove "@", "#", "links" etc.
# 4) Add subjectivity and polarity to the DataFrame
# 5) Send data to json_response

#  Print tweet text
def show_tweets_text_sentiment(json_response):
    print("Show the 5 recent tweets:\n")
    tweets = json_response["data"]
    
    textTweets=[]
    for i, (k,v) in enumerate(tweets.items()):
        for i in range(len(tweets[k]["alltext"])):
            # print(i+1,') ', tweets[k]["alltext"][i]["tweets_text"], '\n')
            textTweets.append(tweets[k]["alltext"][i]["tweets_text"])
    
    # df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])
    # print(textTweets)
    print(" ____**________**____ ")

    # Create a dataframe with a column called Tweets
    df = pd.DataFrame(columns=['Tweets'])
    for tweet in textTweets:
        cleantweet = cleanTxt(tweet)
        df = df.append({"Tweets": cleantweet}, ignore_index=True)
    # Show  rows of data

    # Create two new columns 'Subjectivity' & 'Polarity'
    df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
    df['Polarity'] = df['Tweets'].apply(getPolarity)
    df['Analysis'] = df['Polarity'].apply(getAnalysis)
    pd.set_option('display.max_rows', df.shape[0]+1)

    # Turn DataFrame to Dictionary 
    dictionaryObject = df.to_dict()

    sentiment = {"Positive": 0, "Negative": 0, "Neutral": 0}

    analysis = dictionaryObject["Analysis"]

    print(analysis)

    for i in range(len(analysis)):
        if analysis[i] == "Positive":
            sentiment["Positive"] += 1
        elif analysis[i] == "Negative":
            sentiment["Negative"] += 1
        else:
            sentiment["Neutral"] += 1
        
    print(sentiment)
    
    return sentiment
    
# Create a function to clean the tweets
def cleanTxt(text):
    text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
    text = re.sub('#', '', text) # Removing '#' hash tag
    text = re.sub('RT[\s]+', '', text) # Removing RT
    text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
    
    return text
# I want to add the tweets’ subjectivity and polarity to the DataFrame. In order to do this, I’ll create two functions: one to get the tweets called Subjectivity (how subjective or opinionated the text is — a score of 0 is fact, and a score of +1 is very much an opinion) and the other to get the tweets called Polarity (how positive or negative the text is, — score of -1 is the highest negative score, and a score of +1 is the highest positive score).

# A function to get the subjectivity
def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

# A function to get the polarity
def getPolarity(text):
   return  TextBlob(text).sentiment.polarity

# function to compute negative (-1), neutral (0) and positive (+1) analysis
def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'
    


    




if __name__ == '__main__':
    app.run()
