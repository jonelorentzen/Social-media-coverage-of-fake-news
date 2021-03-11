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
  
  computed:{
    BarChartData() {
      return this.$store.getters.GetBarChartList;
    },
    LineChartData() {
      return this.$store.getters.GetLineChartList;
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