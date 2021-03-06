import { createStore } from "vuex";
import Backendapi from '../backend_api/api.js';

export default createStore({
  state: {
    //List with objects that contain the title and if the title is active or not 
    searches: [],
   
    //The tweets that is displayed MAX 2 queries
    tweets: [],

    //List that contains all of the data the user has added to the search list
    allTweets: []

  },
  mutations: {
  
    SetTweets(state, response){
      state.allTweets.push(response)
      console.log(response)
      if(response == "No data"){
        state.searches[state.allTweets.length-1].data = false
        state.searches[state.allTweets.length-1].loaded = true
      }else{
        state.searches[state.allTweets.length-1].data = true
        state.searches[state.allTweets.length-1].loaded = true
      }
     console.log(state.searches)
    },

    DisplayTweet(state, idx){
      for (let i in state.allTweets){
        if (state.searches[idx]["title"] == state.allTweets[i]["query"]){
          state.tweets.push(state.allTweets[i]);
        }
      }
      state.searches[idx].active = true
      state.searches[idx].index = state.tweets.length -1
    
    },

    RemoveTweets(state, idx){
      state.searches[idx].active = false 
      state.tweets.splice(state.searches[idx].index, 1);
      state.searches[idx].index = null
      if(state.tweets.length == 1){
        for(let i in state.searches){
          if(state.searches[i].active == true){
            state.searches[i].index = 0
          }
        }
      }
    },

    NewSearch(state,SearchItem){
      state.searches.push({
        title: SearchItem,
        active: false,
        loaded: false,
        index: null,
        data: null

      })
    },
  },

  actions: {
    async getResult(state, searchValue) {
      
      try{
        let api = new Backendapi();
        console.log("now its loading");
        
        let response = await api.getMessages(searchValue);
        console.log(response.data)

        if(response.data == "No data"){
          state.commit("SetTweets", response.data);
        }else{
          state.commit("SetTweets", response.data[searchValue]);
        }

       
        
      
      } catch (err){
        this.commit('error',err)
      }
    },
     addNewSearch({commit}, SearchItem){
      commit("NewSearch",SearchItem);
  
    },

    addTweetToDisplay(state, index){
      state.commit("DisplayTweet", index);
    },

    removeFromTweets(state, index){
      state.commit("RemoveTweets", index);
    },
  },
  modules: {

  },
  getters: {
    GetTweets: state => state.tweets,
  
    

  }
});

