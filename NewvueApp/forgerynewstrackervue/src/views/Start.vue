<template>
  <div class="container">
    <h1>Hi, Welcome to Forgery News Tracker</h1>
    <img src="../assets/Forgery_News_tracker_NEW.png" width="500px" height="500px"><br>
    <button class="btn btn-primary" @click="gotoPage()">Redirect to next page</button><br><br>
    <search-box/>
  </div>
</template>

<script>
// import Ping from '../components/Ping.vue';
import SearchBox from '../components/SearchBox.vue';

export default {
  name: 'Start',
  components: {
    SearchBox,
  },
  methods: {
    gotoPage() {
      this.$router.push('/ping');
    },
  },
};
</script>
