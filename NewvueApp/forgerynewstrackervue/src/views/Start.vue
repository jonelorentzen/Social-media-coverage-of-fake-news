<template>
  <div class="container">
    <h1>Hi, Welcome to Forgery News Tracker</h1>
    <img src="../assets/Forgery_News_tracker_NEW.png" width="500px" height="500px"><br>
    <button class="btn btn-primary" @click="gotoPage()">Redirect to next page</button><br><br>
    <search-box/>
    <GeoChart/>
  </div>
</template>

<script>
// import Ping from '../components/Ping.vue';
import SearchBox from '../components/SearchBox.vue';
import GeoChart from '../components/GeoChart.vue'

export default {
  name: 'Start',
  components: {
    SearchBox,
    GeoChart
  },
  methods: {
    gotoPage() {
      this.$router.push('/ping');
    },
  },
};
</script>
