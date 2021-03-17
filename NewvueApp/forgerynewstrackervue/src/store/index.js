import { createStore } from "vuex";
import Backendapi from '../backend_api/api.js';

export default createStore({
  state: {
    searches: [],
    tweets: [],
    BarChartList: [],
    LineChartList: [],
    TopPosts: [],
    TopUsers: []
  },
  mutations: {
    SetTweets(state, response){
      state.tweets = response

    },

    SetBarChartList(state, barchart) {
      state.BarChartList = barchart;
      },
   
    SetLineChartList(state, linechart) {
      state.LineChartList = linechart;
      },

    
    SetTopPosts(state, topposts) {
      state.TopPosts = topposts;
      },

    SetTopUsers(state, topusers) {
      state.TopUsers = topusers;
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
        console.log(response.data)
        console.log(response.data[searchValue]["barchart"])
        console.log(response.data[searchValue]["linechart"])
        console.log(response.data[searchValue]["topposts"])
        console.log(response.data[searchValue]["topusers"])

        state.commit("SetTweets", response);

        state.commit("SetBarChartList", response);
        state.commit("SetLineChartList", response);
        console.log("done")

        state.commit("SetBarChartList", response.data[searchValue]["barchart"]);
        state.commit("SetLineChartList", response.data[searchValue]["linechart"]);
        state.commit("SetTopPosts", response.data[searchValue]["topposts"]);
        state.commit("SetTopUsers", response.data[searchValue]["topusers"]);
        
        
        

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
    getSearchByIndex: (state) => (index) => {return state.searches[index]},
    GetTopPosts: state => state.TopPosts,
    GetTopUsers: state => state.TopUsers,

  }
});

