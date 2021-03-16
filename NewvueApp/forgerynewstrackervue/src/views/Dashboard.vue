<template>
  <div class="container">


    <dir class="recent-searches">
      <h5>Selected Trackers: </h5>
      <search-list/>
    </dir>

    <Trackerheader/>
    
    <Engagement/>
    <div class="container_for_linechart">

    <LineChart id="linechart" :listdata='LineChartData'/>
    </div>
    
    <div class="container_for_barchart">
    <BarChart id="Barchart" :listdata='BarChartData'/>
    </div>
    
    
      <div class="Post_user_container">
        
        <topPosts id="TopPosts"/>
       
        
        <mostinfluentialusers id="TopUsers"/>
  

      </div>
    
  

  </div>
</template>

<script>
//here we import other components

import BarChart from '../components/BarChart'
import LineChart from '../components/LineChart'

import SearchList from '../components/SearchList.vue';

import topPosts from '../components/Topposts'
import mostinfluentialusers from '../components/MostInfluentialUsers'
import Trackerheader from "../components/Trackerheader"
import Engagement from "../components/Engagement"




export default {
  name: 'Dashboard',
  components: {
    BarChart,
    LineChart,
    SearchList,
    topPosts,
    mostinfluentialusers,
    Trackerheader,
    Engagement
    

  },
   computed:{
    BarChartData() {
      return this.$store.getters.GetBarChartList;
    },
    LineChartData() {
      return this.$store.getters.GetLineChartList;
    },
    TopPostsData() {
      return this.$store.getters.GetTopPosts;
    },
    TopUsersData() {
      return this.$store.getters.GetTopUsers;
    },
    yourTrackers(){
      return this.$store.state.searches -1;
    },


  },
  data(){

  },
};
</script>

<style>
    .recent-searches{
      float: right;
    }
    .container{
      margin: 50px;
      display: grid;
      
    }

    #linechart{

        padding-bottom: 50px;
        

    }
    .Post_user_container{
      display: flex;
      max-height: 80%;
    }


</style>