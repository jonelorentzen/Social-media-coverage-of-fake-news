<template>
  <div class="faq">
    <div class="headline">
      <h1>Forgery News Tracker</h1>
    </div>

    <div class="text-container">
      <dl>
          <dt>FAQ Index</dt> 
      <ul>
          <li class="mb-0 pb-0"><a href="#faq-q1">What is Forgery News Tracker?</a></li> 
          <li class="mb-0 pb-0"><a href="#faq-q2">How does search work?</a></li> 
          <li class="mb-0 pb-0"><a href="#faq-q3">What does the different charts and graphs display?</a></li> 
          <li class="mb-0 pb-0"><a href="#faq-q4">Does Forgery News Tracker get back all of the tweets about the query on Twitter?</a></li> 
          <li class="mb-0 pb-0"><a href="#faq-q5">Does Forgery News Tracker tell is a claim is true or false?</a></li> 
          <li class="mb-0 pb-0"><a href="#faq-q5">Who are the Forgery News Tracker developers?</a></li> 

          
      </ul> 
          <dt id="faq-q1">What is Forgery News Tracker?</dt> 
          <dd class="faq-element-contents">
            Forgery News Tracker is a tool that visualizes the spread of a user defined query online on social media. You as the user has the opportunity to write 
            a claim or some news that you want to check how much it has spread on the social medias Twitter and Reddit.
          </dd> 

          <dt id="faq-q2">How does search work?</dt> 
          <dd class="faq-element-contents">
            The search works by the user writes in a query or chooses a predefined query. When the user activates the chosen query, it will be sent a call to the back end 
            to retrive all of the data that is going to be displayed to the user. The defined query must be in the tweet or post on reddit to be sent back from the back end.
            After the data is loaded the user can go the the dashboard where all of the data is displayed in different charts and graphs.
          </dd> 

          <dt id="faq-q3">What does the different charts and graphs display?</dt> 
          <dd class="faq-element-contents">
            In the dashboard you as the user will see a few different charts and graphs that is retrieved from the query chosen. At the top of the page you will see the activity
            which is a overview of the simple stats about the query on twitter. In the activity element you will find how many unique users that has tweeted, quoted or replied to
            a tweet. Below the activity you will find the timelime which shows you the total tweets, replies, quotes and reweets over time. So if a Twitter user tweets the timeline
            increases by one, the same goes for if a user retweets a tweet where the query is present. 

            Futhermore we have a barchart for displaying the total likes, retweets, replies and quotes for all of the tweets that is returned from the back end. To display where the 
            users are tweeting from, there is a geochart of the world. Where the user can hover the mouse over countries to see how many tweets where posted from a country. There is 
            also displayed the top post where the 3 tweets with the most retweets are displayed, and the user can click to view the original tweet. Beside the top posts there is a 
            section for the most influential users that displayes the top 9 users with the most followers that has tweeted about this topic.
          </dd> 

          <dt id="faq-q4">Does Forgery News Tracker get back all of the tweets about the query on Twitter?</dt> 
          <dd class="faq-element-contents">
            No, as per now there is a limit from the Twitter API that restricts us from extracting all of the tweets about the topic. Forgery News Tracker is using the free 
            Twitter API which is resticted to fetching max 100 tweets, we are maximizing the free API by using muliple API calls. But we will never be able to get as many tweets with 
            the free version as the enterprise version would give. In the enterprise version you would get access to all tweets in the archive.
          </dd> 

          <dt id="faq-q5">Does Forgery News Tracker tell is a claim is true or false?</dt> 
          <dd class="faq-element-contents">
            Forgery News Tracker does not do any type of fact checking, this website is only for displaying the spread of fake news. But the query does not have to be a claim that is fake.
            The search function will also work for all types of queries, for example searching for "football" or "dog" will return all of the same charts and graphs. But the intent for making
            this application is to create a tool that could be used to visualize the spread of a false claim or some fake news spreading on social medias. 
          </dd> 

          <dt id="faq-q6">Who are the Forgery News Tracker developers?</dt> 
          <dd class="faq-element-contents">
            Forgery News Tracker is a bachelor thesis for the University of Stavanger Faculty of Science and Technology written by Awalle Mohamed, Jone Lorentzen and Ramtin Hafezinejad
          </dd> 


      </dl>
    </div>

  </div>
</template>

<script>
export default {
    name: 'faq',
    
};  
</script>



<style>
.faq{
    color: black;
    text-align: left;
}

.headline{
  text-align: center;
  padding-top: 50px;
}

.headline h1{
  font-weight: bold;
}

.text-container{
  padding: 50px;
}

.text-container dd{
  padding: 10px;
}

</style>