<template>
  <div class="container">

    <!-- Top of the view, included for both the single view and the comparison view -->
    <SearchList/>
    <Trackerheader class="dashboard-comp" :listdata='Display1.query' :listdata2='Display2.query'/>
    
    <Engagement class="dashboard-comp" :listdata1='Display1' :listdata2='Display2' />
    
    <div class="container_for_linechart">
        <LineChart class="dashboard-comp" id="linechart" :listdata1='Display1' :listdata2='Display2' v-show="Display1.query && Display2.query !== {}"/>
    </div>

    <!-- Displayed when the user has not selected any query -->
    <div class="container_for_no_query" v-show="Display1.query == '' && Display2.query == ''">
        <h1>Activate of the queries you have chosen above or go to yourTrackers to add a search</h1>
    </div>


    <!-- Single view, when the user has only selected one query -->
     <div class="container_for_single_query" v-show="Display1.query != '' &&  Display2.query == '' ">
        <div class="container_for_barchart_single">
            <BarChartBig  class="dashboard-comp" id="Barchart" :listdata='Display1.barchart'/>
        </div>
        
        <div class="container_for_geochart_and_node">
            <div class="container_for_geochart_single" >
                <GeoChartSingle id="Geochart" :listdata='{"US": 69}'/>
            </div>
            <div class="container_for_nodegraph_single" v-if="Display1.query != ''">
                <Sigmagraph :listdata='Display1'/>
            </div>
        </div>
        
        <div class="Post_user_container">
            <topPosts class="dashboard-comp insight" :listdata='Display1.topposts'/>
            <mostinfluentialusers class="dashboard-comp insight" :listdata='Display1.topusers' />
        </div>
    </div>

    <!-- Comparison view, when the user has selected two query -->
    <div class="container_for_comparison" v-show="Display1.query && Display2.query !== ''">
        <div class="container_for_barchart">
            <BarChart  class="dashboard-comp" id="Barchart" :listdata='Display1.barchart'/>
            <BarChart class="dashboard-comp" id="Barchart" :listdata='Display2.barchart'/>
        </div>
        
        <div class="container_for_geochart">
            <GeoChart id="Geochart" :listdata='{"US": 69}'/>
            <GeoChart id="Geochart" :listdata='{"US": 69}'/>
        </div>

        <div v-if="Display1.query != '' && Display2.query != ''" class="container_for_nodenetwork">
            <Sigmagraph class="nodenetwork_double_comp" :listdata='Display1'/>
            <Sigmagraph class="nodenetwork_double_comp" :listdata='Display2'/>
        </div>

        <div class="Post_container">
            <topPosts class="dashboard-comp insight" :listdata='Display1.topposts'/>
            <topPosts class="dashboard-comp insight" :listdata='Display2.topposts'/> 
        </div>

        <div class="Post_user_container"> 
            <mostinfluentialusers class="dashboard-comp insight" :listdata='Display1.topusers' />
            <mostinfluentialusers class="dashboard-comp insight" :listdata='Display2.topusers'/>
        </div>
    </div>

  </div>
</template>

<script>
//here we import other components
import BarChart from '../components/BarChart'
import BarChartBig from '../components/BarChartBig'
import LineChart from '../components/LineChartComponent'
import SearchList from '../components/SearchList.vue';
import topPosts from '../components/Topposts'
import mostinfluentialusers from '../components/MostInfluentialUsers'
import Trackerheader from "../components/Trackerheader"
import Engagement from "../components/Engagement"
import GeoChart from "../components/GeoChartComponent"
import GeoChartSingle from "../components/GeoChartSingle"
import Sigmagraph from "../components/Sigmagraph"


export default {
  name: 'Dashboard',
  components: {
    BarChart,
    BarChartBig,
    LineChart,
    SearchList,
    topPosts,
    mostinfluentialusers,
    Trackerheader,
    Engagement,
    GeoChart,
    GeoChartSingle,
    Sigmagraph
    
    },
    
    computed:{
    Display1(){
        if(this.$store.getters.GetTweets[0] === undefined){
            return {"barchart": [], "topposts": {}, "topusers": {}, "geochart": {}, "query": '', "activity": {"posts":null,"users":null,"engagement":null,}, "linechart": {}}
        }else{
            return this.$store.getters.GetTweets[0];
        }   
    },
    Display2(){
        if(this.$store.getters.GetTweets[1] === undefined){
            return {"barchart": [], "topposts": {}, "topusers": {}, "geochart": {}, "query": '', "activity": {"posts":null,"users":null,"engagement":null,}, "linechart": {}}
        }else{
            return this.$store.getters.GetTweets[1];
        }
    },
    yourTrackers(){
      return this.$store.state.searches -1;
    },
  },

};
</script>


<style scoped>

    .dashboard-comp{
      margin-bottom: 20px;
    }
    .insight{
      max-width: 50%;
      
    }
    .container{
      margin: auto;
      display: grid;
      min-height: 100vh;
      grid-column-gap: 1.5em;
      grid-row-gap: 1.5em;
      grid-auto-rows: min-content;
      font-family: Quicksand,Helvetica,Arial,sans-serif;
      font-weight: 500;
      font-size: 16px;
      color: #26293c;
    }

    .container_for_barchart{
        display: flex;
        justify-content: space-between;
        width: 100%;
        padding-bottom: 50px;

    }

    #linechart{
        padding-bottom: 50px;
    }
    .Post_user_container{
      display: flex;
      justify-content: space-between;
    }
    .Post_container{
        display: flex;
        justify-content: space-between;
        width: 100%;

    }



    .container_for_geochart{
        display: flex;
        justify-content: space-between;
        padding-bottom: 25px;


    }

    .container_for_nodenetwork{
        display: flex;
        justify-content: space-between;
    }
    .nodenetwork_double_comp{
        width: 50%;
    }


    .container_for_geochart_single{
        padding-bottom: 50px;
        width: 50%;

    }

    .container_for_nodegraph_single{
        width: 50%;
    }

   
   .container_for_geochart_and_node{
       display: flex;
       justify-content: space-between;
   }




</style>