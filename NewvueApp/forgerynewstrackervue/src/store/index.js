import { createStore } from "vuex";
import Backendapi from '../backend_api/api.js';

export default createStore({
  state: {},
  mutations: {},
  actions: {
    async getResult() {
      console.log(this.searchValue)
      let api = new Backendapi();
      let response = await api.getMessages(this.searchValue);
      console.log(response)
    },

  },
  modules: {}
});
