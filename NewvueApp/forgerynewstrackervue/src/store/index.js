import { createStore } from "vuex";
import Backendapi from '../backend_api/api.js';

export default createStore({
  state: {
    //List with objects that contain the title and if the title is active or not 
    searches: [],
    //State to keep control over the indexes in tweets and searches. {"Index in the searchlist": "Index in the tweets list"}, {5:0, 1:1}
    searchesIndexInTweets: {},
    //The tweets that is displayed MAX 2 queries
    tweets: [],
    //List that contains all of the data the user has added to the search list
    allTweets: []
  
  
  },
  mutations: {
    SetTweets(state, response){
      state.allTweets.push(response)
    },

    DisplayTweet(state, index){
      state.tweets.push(state.allTweets[index]);
      state.searchesIndexInTweets[index] = state.tweets.length-1
    },

    RemoveTweets(state, index){
      state.tweets.splice(state.searchesIndexInTweets[index], 1);
      
      delete state.searchesIndexInTweets[index]
    
      console.log(state.searchesIndexInTweets)
      
    },

    NewSearch(state,SearchItem){
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
      console.log(state.searches)
    }
  },

  actions: {
    addNewSearch({commit}, SearchItem){
      commit("NewSearch",SearchItem);
    },

    async getResult(state, searchValue) {
      this.commit('loading')
      try{
        let api = new Backendapi();
        let response = await api.getMessages(searchValue);
        console.log(response.data)
        
        state.commit("SetTweets", response.data[searchValue]);
        
        console.log("done")
        
      } catch (err){
        this.commit('error',err)
      }
    },
    addTweetToDisplay(state, index){
      state.commit("DisplayTweet", index);
    },

    removeFromTweets(state, index){
      state.commit("RemoveTweets", index);
    },

    searchItemActive(state, index){
      state.commit("searchItemActive", index)
    }
  },
  modules: {

  },
  getters: {
    GetTweets: state => state.tweets,
    getSearchByIndex: (state) => (index) => {return state.searches[index]},
    

  }
});

