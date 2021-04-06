<template>

    <div class="chart-box">
        <div class="chartheader">
            <h3><span>Timeline</span></h3>
        </div>

        <div class="chart-container">
        <area-chart :data="listdata" :colors="['#l00']" xtitle="Tweeted at" ytitle="Cumulative Tweets"></area-chart>
        </div>

    </div>

</template>

<script>

export default {
    name:"LineChart",
    props: ['listdata']
}
</script>

<style scoped>
.chart-box{
    margin: 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}
.chartheader{
    height: 45px;
    display: flex;
}
.chartheader h3{
    font-size: 1.1em;
    line-height: 1.25;
}
.chart-container{
    border: 1px solid #dddfea;
    padding: 3em;
    padding-top: 4em;
}
</style>
