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


.help-tip-container{
    z-index: 100;
    padding: 2.5px 0px 0px 5px;
}
.help-tip{
    text-align: center;
    background-color: #BCDBEA;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    font-size: 14px;
    line-height: 25px;
    cursor: default;
}

.help-tip:before{
    content:'?';
    font-weight: bold;
    color:#fff;
}

.help-tip:hover p{
    display:block;
    transform-origin: 100% 0%;
    -webkit-animation: fadeIn 0.3s ease-in-out;
    animation: fadeIn 0.3s ease-in-out;

}

.help-tip p{    /* The tooltip */
    display: none;
    text-align: left;
    background-color: #1E2021;
    padding: 20px;
    width: 300px;
    border-radius: 3px;
    box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.2);
    right: -4px;
    color: #FFF;
    font-size: 13px;
    line-height: 1.4;
}

.help-tip p:before{ /* The pointer of the tooltip */
    content: '';
    width:0;
    height: 0;
    border:6px solid transparent;
    border-bottom-color:#1E2021;

}

.help-tip p:after{ /* Prevents the tooltip from being hidden */
    width:100%;
    height:40px;
    content:'';
   
}

/* CSS animation */

@-webkit-keyframes fadeIn {
    0% { 
        opacity:0; 
        transform: scale(0.6);
    }

    100% {
        opacity:100%;
        transform: scale(1);
    }
}

@keyframes fadeIn {
    0% { opacity:0; }
    100% { opacity:100%; }
}
</style>
