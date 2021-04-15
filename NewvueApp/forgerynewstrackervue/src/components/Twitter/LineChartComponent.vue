<template>

    <div class="chart-box">
        <div class="chartheader">
            <h3><span>Timeline</span></h3>
            <div class="help-tip-container">
                <div class="help-tip">
                    <p>The line chart shows the total tweets, retweets, replies and quotes over time. For every tweet, retweet, reply and quote the line increments by one. </p>
                </div>
            </div>
        </div>

        <div class="chart-container" v-show="listdata2.query != ''">
        <line-chart :data="[{'name': listdata1.query, 'data': listdata1.linechart }, {'name': listdata2.query, 'data': listdata2.linechart }]" :colors="['#000', '#666']" :dataset="{borderWidth: 2}" xtitle="Tweeted at" ytitle="Cumulative Tweets" :messages="{empty: 'No data'}"></line-chart>
        </div>
        <div class="chart-container" v-show="listdata2.query == ''">
        <line-chart :data="[{'name': listdata1.query, 'data': listdata1.linechart }]" :colors="['#000', '#0000FF']" :dataset="{borderWidth: 2}" xtitle="Tweeted at" ytitle="Cumulative Tweets" :messages="{empty: 'No data'}"></line-chart>
        </div>

    </div>

</template>

<script>

export default {
    props: ['listdata1', 'listdata2'],
    
    
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
    font-weight: 900;
    font-size: 1.25em;
    line-height: 1.5;
}
.chart-container{
    border: 1px solid #dddfea;
    padding: 3em;
    padding-top: 4em;
}


</style>
