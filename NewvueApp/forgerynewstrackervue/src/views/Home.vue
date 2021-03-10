<template>
  <div class="container">
    <h1>Hi, Welcome to Forgery News Tracker</h1>
    <!-- this how u put images in site -->
    <img :src="'' + require('@/assets/Forgery_News_tracker_NEW.png') + ''" alt=""><br>
    <!-- <img src="..assets/Forgery_News_tracker_NEW.png" width="500px" height="500px"><br> -->
    <button class="btn btn-primary" @click="getResult()">Get result</button><br><br>
     <input v-model="searchValue" class="form-control"
        type="text" placeholder="Search here">
    <button class="btn btn-primary" @click="gotoPage()">Redirect to next page</button><br><br>

    <search-box/>
    <bar-chart/>
  </div>
</template>

<script>

//here we import other components
import SearchBox from '../components/SearchBox.vue';
import Backendapi from '../backend_api/api.js';

export default {
  name: 'Home',
  components: {
    SearchBox,
  },
  methods: {
    gotoPage() {
      this.$router.push('/ping');
    },
    async getResult() {
      console.log(this.searchValue)
      let api = new Backendapi();
      let response = await api.getMessages(this.searchValue);
      console.log(response)
    },

  },
  data() {
    return {
      searchValue: '',
    };
  },
};
</script>