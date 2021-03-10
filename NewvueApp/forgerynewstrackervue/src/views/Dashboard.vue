<template>
  <div class="container">

    <Trackerheader/>
    
    <Engagement/>
    <div class="container_for_linechart">
    <LineChart id="linechart" :listdata='LineChartData'/>
    </div>
    
    <div class="container_for_barchart">
    <BarChart id="Barchart" :listdata='BarChartData'/>
    </div>
    
    
      <div class="Post_user_container">
        
        <topPosts/>
       
        
        <mostinfluentialusers />
  

      </div>
    
  

  </div>
</template>

<script>
//here we import other components

import BarChart from '../components/BarChart'
import LineChart from '../components/LineChart'
import topPosts from '../components/Topposts'
import mostinfluentialusers from '../components/MostInfluentialUsers'
import Trackerheader from "../components/Trackerheader"
import Engagement from "../components/Engagement"



export default {
  name: 'Dashboard',
  components: {
    BarChart,
    LineChart,
    topPosts,
    mostinfluentialusers,
    Trackerheader,
    Engagement
    
  },
  data(){
    return{
       BarChartData: [['Likes', 345], ['Retweeets', 247],['Replies', 47],['Quotes', 27]],
       LineChartData: {'2017-05-13T:13:03:00': 1, '2017-05-13T:14:03:00': 2,'2017-05-13T:15:03:00': 3,'2017-05-13T:16:03:00': 4,}

    };
  },

};
</script>

<style>
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