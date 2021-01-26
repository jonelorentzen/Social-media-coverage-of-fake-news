#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, render_template,jsonify
import requests
import json
import os
DEVELOPMENT_ENV  = True

app = Flask(__name__)

app_data = {
    "name":         "Fake news tracker -  Web App",
    "description":  "A basic Flask app using bootstrap for layout to represent the spread of fake news on social media",
    "author":       "FakeNewsTrack3",
    "html_title":   "Fake News Tracker",
    "project_name": "Fake News Tracker",
    "keywords":     "flask, webapp, template, basic"
}

#getting data from TWITTER
#....................................................
def auth():
    return os.environ.get("BEARER_TOKEN")

def create_url(query):
    # Tweet fields are adjustable.s
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
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
    query = request.form.get('query')
    if request.method == 'POST':
        querys = request.form.get('query')
        bearer_token = auth()
        url = create_url(querys)
        headers = create_headers(bearer_token)
        json_response = connect_to_endpoint(url, headers)

        #handle the data in a different function
        show_autherId(json_response)
        
        #print(json.dumps(json_response, indent=4, sort_keys=True))
        return json.dumps(json_response, indent=4, sort_keys=True)
    
    return render_template('showinfo.html', app_data=app_data)

def show_autherId(json_response):
    #print(json_response)
    # print([obj['text'] for obj in json_response['data'] if(obj['text'])])
    print("___________________")
    print([{"author_id" : obj['author_id']} for obj in json_response['data'] if(obj['author_id'])])

    #print ([obj['author_id'] for obj in json_response if (obj['author_id'])])
    # newDict={}
    # for item in json_response['data']:
    #     newDict.update(item)
    # json_response['data'] = newDict
    # print(json_response['data']['author_id'])



@app.route('/test1', methods=['GET', 'POST'])
def testing():
    #for GET requests
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask'}
        return jsonify(message)

    #for POST requests
    if request.method == 'POST':
        print(request.get_json()) #parsing as JSON
        return 'Success', 200

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', app_data=app_data)


@app.route('/about')
def about():
    return render_template('about.html', app_data=app_data)


@app.route('/service')
def service():
    return render_template('service.html', app_data=app_data)


@app.route('/contact')
def contact():
    return render_template('contact.html', app_data=app_data)



if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)