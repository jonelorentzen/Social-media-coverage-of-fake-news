<template>
     <div class="chart-box">
        <div class="chartheader">
            <h3><span>Sentiment</span></h3>
            <div class="help-tip-container">
                <div class="help-tip">
                    <p>The sentiment pie chart displays how many of the tweets that the text is positive, negative or netural.</p>
                </div>
            </div>
        </div>
        <div class="chart-container">
            <pie-chart :data="listdata" :messages="{empty: 'No data'}"></pie-chart>
        </div>
    </div>
</template>

<script>
export default {
    name:"PieChartReddit",
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
    font-weight: 900;
    font-size: 1.25em;
    line-height: 1.5;
}
.chart-container{
    border: 1px solid #dddfea;
    padding: 3em;
    padding-top: 4em;
    height: 450px;
}

</style>