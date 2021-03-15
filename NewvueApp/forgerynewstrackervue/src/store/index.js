import { createStore } from "vuex";
import Backendapi from '../backend_api/api.js';

export default createStore({
  state: {
    searches: [{
      title: '',
    }],
  //   {'text': '@GunnarBj @marie_holmqvist fast i Norge så sa man åt Alpenresenärer att sätta sig i karantän oavsett symptom. Här gjorde man faktiskt inte det. Har du läst den här? Jag är öppen för att diskutera sakfel i den https://t.co/lrBtJus2ld',
  //    'author_id': '1273549542806491136', 'id': '1369942833973649408', 'created_at': '2021-03-11T09:26:38.000Z', 'public_metrics': {'retweet_count': 0, 'reply_count': 2, 'like_count': 12, 'quote_count': 0}, 'referenced_tweets': [{'type': 'replied_to', 'id': '1369942131805196291'}]},
  //     {'text': 'RT @ingel2: En håndfull selskaper eier covid-vaksinene, men klarer ikke å lage nok. 100 land krever at de slipper patentet fri, så all ledi…',
  //      'author_id': '567251909', 'id': '1369837473753403393', 'created_at': '2021-03-11T02:27:58.000Z', 'public_metrics': {'retweet_count': 31, 'reply_count': 0, 'like_count': 0, 'quote_count': 0}, 'referenced_tweets': [{'type': 'retweeted', 'id': '1369534399038058498'}]}, {'text': 'RT @ingel2: En håndfull selskaper eier covid-vaksinene, men klarer ikke å lage nok. 100 land krever at de slipper patentet fri, så all ledi…', 
  //      'author_id': '4860786046', 'id': '1369811425141665793', 'created_at': '2021-03-11T00:44:28.000Z', 'public_metrics': {'retweet_count': 31, 'reply_count': 0, 'like_count': 0, 'quote_count': 0}, 'referenced_tweets': [{'type': 'retweeted', 'id': '1369534399038058498'}]}]
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
      console.log(total_likes, total_retweets, total_replies, total_quotes)
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
        title: SearchItem
      })
    },
    loading(){
      console.log("loading")
    }

  },

  actions: {
    addNewSearch({commit}, SearchItem){
      commit("NEW_SEARCH",SearchItem);
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
        
      } catch (err){
        this.commit('error',err)
      }
    }
  },
  modules: {

  },
  getters: {
    GetBarChartList: state => state.BarChartList,
    GetLineChartList: state => state.LineChartList

  }
});

