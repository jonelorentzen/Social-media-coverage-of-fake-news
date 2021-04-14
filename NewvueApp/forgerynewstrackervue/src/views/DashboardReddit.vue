<template>
  <div class="container">

    <!-- Top of the view, included for both the single view and the comparison view -->
    <SearchList/>
    
    <div class="header">
        <Trackerheader class="dashboard-comp" :listdata='Display1.query' :listdata2='Display2.query'/>
        <MediaSelector class="media"/>
    </div>

    
    <EngagementReddit class="dashboard-comp" :listdata1='Display1' :listdata2='Display2' />
    

    <!-- Displayed when the user has not selected any query -->
    <div class="container_for_no_query" v-show="Display1.query == '' && Display2.query == ''">
        <h1>Activate of the queries you have chosen above or go to yourTrackers to add a search</h1>
    </div>

    <!-- Reddit view, only 1 query selected -->
    <div class="container_for_single_reddit"  v-show="Display1.query != '' &&  Display2.query == ''">
        <!-- <div class="container_for_linechart_reddit"> 
            <LineChartReddit :listdata1='Display1' :listdata2='Display2' v-if="Display1.query !== ''"/>
        </div>
        <div class="container_for_reddit">
            <WordCloudReddit :listdata='Display1.wordcloudreddit'/>
            <PieChartReddit :listdata='Display1.piechartreddit'/>
           
        </div>
        <div class="Post_user_container">
            <TopPostsReddit :listdata='Display1.toppostsreddit'/>
            <TopUsersReddit :listdata='Display1.topusersreddit'/>
        </div> -->

        <div class="row dashboard-comp">
            <div class="col-sm">
                <LineChartReddit :listdata1='Display1' :listdata2='Display2' v-if="Display1.query !== ''"/>
            </div>
        </div>

         <div class="row dashboard-comp">
            <div class="col-sm-6">
                <WordCloudReddit :listdata='Display1.wordcloudreddit'/>
            </div>
             <div class="col-sm-6">
                 <PieChartReddit :listdata='Display1.piechartreddit'/>
            </div>
        </div>

        <div class="row dashboard-comp">
            <div class="col-sm-6">
                <TopPostsReddit :listdata='Display1.toppostsreddit'/>
            </div>
             <div class="col-sm-6">
                 <TopUsersReddit :listdata='Display1.topusersreddit'/>
            </div>
        </div>

    </div>

    <!-- Reddit view, 2 queries are selected -->
    <div class="container_for_comparison_reddit"  v-show="Display1.query != '' &&  Display2.query != ''">
        <!-- <div class="container_for_linechart_reddit"> 
            <LineChartReddit :listdata1='Display1' :listdata2='Display2' v-if="Display1.query !== ''"/>
        </div>
        <div class="container_for_reddit">
            <WordCloudReddit :listdata='Display1.wordcloudreddit'/>
            <WordCloudReddit :listdata='Display2.wordcloudreddit'/>
        </div>
        <div class="container_for_reddit">
            <PieChartReddit :listdata='Display1.piechartreddit'/>
            <PieChartReddit :listdata='Display2.piechartreddit'/>
        </div>
        <div class="Post_user_container">
            <TopPostsReddit :listdata='Display1.toppostsreddit'/>
            <TopPostsReddit :listdata='Display2.toppostsreddit'/>
        </div>
         <div class="Post_user_container">
            <TopUsersReddit :listdata='Display1.topusersreddit'/>
            <TopUsersReddit :listdata='Display2.topusersreddit'/>
        </div> -->

        <div class="row dashboard-comp">
            <div class="col-sm">
                <LineChartReddit :listdata1='Display1' :listdata2='Display2' v-if="Display1.query !== ''"/>
            </div>
        </div>

        <div class="row dashboard-comp">
            <div class="col-sm-6">
                <WordCloudReddit :listdata='Display1.wordcloudreddit'/>
            </div>
             <div class="col-sm-6">
                 <WordCloudReddit :listdata='Display2.wordcloudreddit'/>
            </div>
        </div>

        <div class="row dashboard-comp">
            <div class="col-sm-6">
                <PieChartReddit :listdata='Display1.piechartreddit'/>
            </div>
             <div class="col-sm-6">
                 <PieChartReddit :listdata='Display2.piechartreddit'/>
            </div>
        </div>

        <div class="row dashboard-comp">
            <div class="col-sm-6">
                <TopPostsReddit :listdata='Display1.toppostsreddit'/>
            </div>
             <div class="col-sm-6">
                 <TopPostsReddit :listdata='Display2.toppostsreddit'/>
            </div>
        </div>

        <div class="row dashboard-comp">
            <div class="col-sm-6">
                <TopUsersReddit :listdata='Display1.topusersreddit'/>
            </div>
             <div class="col-sm-6">
                 <TopUsersReddit :listdata='Display2.topusersreddit'/>
            </div>
        </div>

    </div>


  </div>
</template>

<script>
//here we import other components

import SearchList from '../components/SearchList.vue';
import Trackerheader from '../components/Trackerheader';
import MediaSelector from '../components/MediaSelector';
import EngagementReddit from '../components/EngagementReddit';
import PieChartReddit from "../components/PieChartReddit"
import LineChartReddit from "../components/LineChartReddit"
import TopPostsReddit from "../components/TopPostsReddit"
import TopUsersReddit from "../components/TopUsersReddit"
import WordCloudReddit from "../components/WordCloudReddit"



export default {
  name: 'Dashboard',
  components: {
    SearchList,
    Trackerheader,
    MediaSelector,
    EngagementReddit,
    PieChartReddit,
    LineChartReddit,
    TopPostsReddit,
    TopUsersReddit,
    WordCloudReddit
    
    },
    
    computed:{
    Display1(){
        if(this.$store.getters.GetTweets[0] === undefined){
            return {"barchart": [], "topposts": {}, "topusers": {}, "geochart": {}, "query": '', "engagementreddit": {"posts":null,"users":null,"engagement":null,}, "linechart": {}, "linechartreddit":{}}
        }else{
            return this.$store.getters.GetTweets[0];
        }   
    },
    Display2(){
        if(this.$store.getters.GetTweets[1] === undefined){
            return {"barchart": [], "topposts": {}, "topusers": {}, "geochart": {}, "query": '', "engagementreddit": {"posts":null,"users":null,"engagement":null,}, "linechart": {}, "linechartreddit": {}}
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

    .header{
        display: flex;
    }

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
    .media{
        float: right;
    }

    .container_for_linechart_reddit{
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

    .container_for_reddit{
        display: flex;
        justify-content: space-between;
        padding-bottom: 25px;
       
    }
  

</style>