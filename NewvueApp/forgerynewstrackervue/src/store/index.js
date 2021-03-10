import { createStore } from "vuex";
// import Backendapi from '../backend_api/api.js';

export default createStore({
  state: {
    searches: [{
      title: "Jesus and I are friends on Facebook"
    },
    {
      title: "Caffelatte doesn´t have any milk inside it"
    },
    {
      title: "Drinking vodka can cure cancer."
    }
  ]
  },
  mutations: {},
  actions: {
  },
  modules: {}
});

// async getResult() {
//   console.log(this.searchValue)
//   let api = new Backendapi();
//   let response = await api.getMessages(this.searchValue);
//   console.log(response)
// },