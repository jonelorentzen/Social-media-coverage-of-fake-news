<template>
  <div class="container">

    <Trackerheader class="dashboard-comp"/>
    
    <Engagement class="dashboard-comp"/>
    
    
    <div class="container_for_linechart">
    <LineChart class="dashboard-comp" id="linechart" :listdata='LineChartData'/>
    </div>
   
    
    
    <div class="container_for_barchart">
    <BarChart class="dashboard-comp" id="Barchart" :listdata='BarChartData'/>
    </div>
    
    
      <div class="Post_user_container">
        
        <topPosts class="dashboard-comp"/>
       
        
        <mostinfluentialusers class="dashboard-comp"/>
  
    </div>

    
 
  

  </div>
</template>

<script>
//here we import other components

//Alle delene på komponentene skal ha grid-column: span 12 / auto;

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

<style scoped>
    .dashboard-comp{
      margin: 20px;
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

    #linechart{
        padding-bottom: 50px;
        

    }
    .Post_user_container{
      display: flex;
      max-height: 80%;
    }


</style>