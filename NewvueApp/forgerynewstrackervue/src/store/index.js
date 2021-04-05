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
    SetLinks(state, response){
      state.links = response
    },
    SetNodes(state, response){
      state.nodes = response 
    },
    SetTweets(state, response){
      state.allTweets.push(response)
    },

    DisplayTweet(state, index){
      state.tweets.push(state.allTweets[index]);
      state.searchesIndexInTweets[index] = state.tweets.length-1
      console.log(state.tweets)
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
        loaded: false,
      })
    },

    loading(state,index){
      state.searches[index].loaded = true
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
    loading({commit},index){
      commit('loading',index)
    },
    async getResult(state, searchValue,) {
      
      try{
        let api = new Backendapi();
        let response = await api.getMessages(searchValue);
        console.log(response.data)

        
        state.commit("SetTweets", response.data[searchValue]);
        
        //set loading screen
        
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

