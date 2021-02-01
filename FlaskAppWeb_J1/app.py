#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, render_template,jsonify,redirect, url_for
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
    "keywords":     "Flask, webapp, template, basic"
}

app.config['newdata'] = {}

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
    tweet_fields = "tweet.fields=public_metrics"
    max_results = "max_results=100"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}".format(
        query, tweet_fields, max_results
        )
    return url
#https://api.twitter.com/1.1/search/tweets.json?q=trump&result_type=popular

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
    if request.method == 'POST':
        querys = request.form.get('query')
        bearer_token = auth()
        url = create_url(querys)
        headers = create_headers(bearer_token)
        json_response = connect_to_endpoint(url, headers)
        app.config['newdata'] = json_response
        
        return redirect(url_for('testingJs'))

    print(app.config['newdata'])    
    return json.dumps(app.config['newdata'])


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

@app.route('/testingJs')
def testingJs():
    return render_template('testingJs.html', app_data=app_data)

@app.route('/new')
def new():
    return render_template('new.html', app_data=app_data)

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)