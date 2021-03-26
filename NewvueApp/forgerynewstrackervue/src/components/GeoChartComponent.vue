<template>
    <div class="geochart-box">

    <div class="geochart-container">
        <geo-chart :data="barchart"></geo-chart>
    </div>
    </div>
</template>

<script>

export default {
    name: "geochart",
    computed: {
      barchart(){
        return this.$store.state.GeoChartDict
      },}
    
}
</script>

<style scoped>
.geochart-box{
    align-items: center;
    
    
}
.geochart-container{
    border: 1px solid #dddfea;
    

}

</style>

