<template>
  <div class="container">
    <LineChart id="linechart" :listdata='LineChartData'/>
    <BarChart :listdata='BarChartData'/>

  </div>
</template>

<script>
//here we import other components

import BarChart from '../components/BarChart'
import LineChart from '../components/LineChart'



export default {
  name: 'Dashboard',
  components: {
    BarChart,
    LineChart
    
  },
  data(){
    return{
       LineChartData: {'2017-05-13T:13:03:00': 1, '2017-05-13T:14:03:00': 2,'2017-05-13T:15:03:00': 3,'2017-05-13T:16:03:00': 4,}

    };
  },
  computed:{
    BarChartData() {
      return this.$store.getters.GetBarChartList;
    }
  },

};
</script>

<style>
    .container{
      margin: 50px;
    }

    #linechart{
        padding-bottom: 50px;

    }


</style>