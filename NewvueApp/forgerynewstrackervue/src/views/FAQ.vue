<template>
  <div class="faq">
    <h1>Forgery News Tracker</h1>
    <dl>
        <dt>FAQ Index</dt> 
    <ul>
        <li class="mb-0 pb-0"><a href="#faq-q1">What is Hoaxy?</a></li> 
        <li class="mb-0 pb-0"><a href="#faq-q10">What is the difference between Articles search and Twitter search?</a></li> 
        <li class="mb-0 pb-0"><a href="#faq-q2">How does Articles search work?</a></li> 
    </ul> 
        <dt id="faq-q1">What is Hoaxy?</dt> 
        <dd class="faq-element-contents">
        				Hoaxy is a tool that visualizes the spread of articles online. Articles can
								be found on Twitter, or in a corpus of claims and related fact checking.
        </dd> 
        <dt id="faq-q10">What is the difference between Articles search and Twitter
									search?
		</dt> 
        <dd class="faq-element-contents">
								There are two search modes.
                                                                <b>Articles</b> search finds claims
								and related fact checking in a limited corpus of articles from
								low-credibility and fact-checking sources, dating back to 2016. 
								This mode leverages the
								<a href="https://rapidapi.com/truthy/api/hoaxy" target="_blank">Hoaxy API</a>
								to retrieve relevant articles, accounts, and
								tweets. <b>Twitter</b> search lets users track articles from any
								sources posted on Twitter, but only within the last 7 days. 
								
								
								Twitter mode uses
								the
								<a href="https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets" target="_blank">Twitter Search API</a>
								to retrieve relevant, popular, or mixed	tweets matching your
								search query. It is compatible with all
								<a href="https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators" target="_blank">advanced search operators</a>.
								
								At most, Hoaxy is capable of visualizing the top 1000 accounts and in the case of a Twitter search, this will be the most recently active 1000 accounts if sorted by <em>Recent</em>.
		</dd> 
    </dl>

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

</style>