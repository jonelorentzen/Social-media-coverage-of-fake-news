from flask import Flask, jsonify, redirect, request, url_for
from flask_cors import CORS
import requests
import json
import os
import time

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('ppppng!')

#Dictionary that is used to send the data to the javascript
app.config['newdata'] = {}

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
    url = "https://api.twitter.com/2/tweets?ids={}&{}".format(
        query, tweet_fields, user_fields
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

        #Create the token to get acess to the Twitter 
        bearer_token = auth()
        headers = create_headers(bearer_token)



        #API call to get back a dictionary with 10 api call without any duplicates
        json_response = api_caller('Trump', headers)

        # New call to the the Twitter API that uses the ID of the retweeted tweets and adds the data of the original tweets to the dictionary
        #The create_id_url creates the url that is used to call the api with.
        ids = extract_retweets(json_response)
        url_ids = create_id_url(ids)
        json_response2 = connect_to_endpoint(url_ids, headers)
        
        for item in json_response2["data"]:
            json_response["data"].append(item)
        
        app.config['newdata'] = json_response
        
        #return redirect(url_for('testingJs'))
        return json.dumps(app.config['newdata'])

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

        if count == 3:
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


if __name__ == '__main__':
    app.run()