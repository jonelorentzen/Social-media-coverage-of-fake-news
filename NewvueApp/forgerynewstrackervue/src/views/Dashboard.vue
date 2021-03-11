<template>
  <div class="container">

    <dir class="recent-searches">
      <h5>Selected Trackers: </h5>
      <search-list/>
    </dir>
    <LineChart id="linechart" :listdata='LineChartData'/>
    <BarChart :listdata='BarChartData'/>

  </div>
</template>

<script>
//here we import other components

import BarChart from '../components/BarChart'
import LineChart from '../components/LineChart'
import SearchList from '../components/SearchList';



export default {
  name: 'Dashboard',
  components: {
    BarChart,
    LineChart,
    SearchList,
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
    .recent-searches{
      float: right;
    }
    .container{
      margin: 50px;
    }

    #linechart{
        padding-bottom: 50px;

    }


</style>