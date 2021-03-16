import { createStore } from "vuex";
import Backendapi from '../backend_api/api.js';

export default createStore({
  state: {
    searches: [],
    tweets: [],
    BarChartList: [],
    LineChartList: []
  },
  mutations: {
    SetTweets(state, response){
      state.tweets = response

    },
    SetBarChartList(state, tweets){
      let total_retweets = 0
      let total_likes = 0
      let total_replies = 0
      let total_quotes = 0
     console.log(tweets.data)
      for (let i = 0; i < Object.keys(tweets.data).length; i++) {
          if ("referenced_tweets" in tweets.data[i]) {
              if (tweets.data[i]['referenced_tweets']['0']["type"] !== "retweeted") {
                  total_retweets += tweets.data[i]['public_metrics']["retweet_count"]
                  total_likes += tweets.data[i]['public_metrics']["like_count"]
                  total_replies += tweets.data[i]['public_metrics']["reply_count"]
                  total_quotes += tweets.data[i]['public_metrics']["quote_count"]
              }
          } else {
              total_retweets += tweets.data[i]['public_metrics']["retweet_count"]
              total_likes += tweets.data[i]['public_metrics']["like_count"]
              total_quotes += tweets.data[i]['public_metrics']["quote_count"]
              total_replies += tweets.data[i]['public_metrics']["reply_count"]
          }
      }
      // console.log(total_likes, total_retweets, total_replies, total_quotes)
      state.BarChartList = [['Likes', total_likes], ['Retweeets', total_retweets],['Replies', total_replies],['Quotes',total_quotes]]
    
    },
    SetLineChartList(state, tweets) {
      let allDates = [];
      let finalDates = [];
      
      for (let i = 0; i < Object.keys(tweets.data).length; i++) {
          const element = tweets.data[i]["created_at"];
          allDates.push(element)
          
      }
      for (let i = 0; i < tweets.data.length; i++){
          allDates[i] = allDates[i].replace(".000Z", "")
    
          
      }
      allDates.sort();

      for (let i = 0; i < tweets.data.length; i++){
          finalDates.push([allDates[i],i+1])
    
      }
      console.log(finalDates)
      
      state.LineChartList = finalDates;
      
      },

    NEW_SEARCH(state,SearchItem){
      state.searches.push({
        title: SearchItem,
        active: false,
      })
    },
    loading(){
      console.log("loading")
    },
    searchItemActive(state, index){
      state.searches[index].active = !state.searches[index].active
    }

  },

  actions: {
    addNewSearch({commit}, SearchItem){
      commit("NEW_SEARCH",SearchItem, );
    },
    async getResult(state, searchValue) {
      this.commit('loading')
      try{
        let api = new Backendapi();
        let response = await api.getMessages(searchValue);
        console.log(response)
        state.commit("SetTweets", response);
        state.commit("SetBarChartList", response);
        state.commit("SetLineChartList", response);
        console.log("done")
      } catch (err){
        this.commit('error',err)
      }
    },
    searchItemActive(commit, index){
      this.commit("searchItemActive", index)
    }
  },
  modules: {

  },
  getters: {
    GetBarChartList: state => state.BarChartList,
    GetLineChartList: state => state.LineChartList,
    getSearchByIndex: (state) => (index) => {return state.searches[index]}

  }
});

