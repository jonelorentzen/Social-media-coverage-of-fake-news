<template>
     <div class="chart-box">
        <div class="chartheader">
            <h3><span>Total Interactions</span></h3>
            <div class="help-tip-container">
                <div class="help-tip">
                    <p>This bar chart represents all the likes, retweets, replies and quotes from all of the tweets.</p>
                </div>
            </div>
        </div>

        <div class="chart-container">
        <column-chart :data="listdata" :colors="['#l00']" :messages="{empty: 'No data'}" width="1200px"></column-chart>
        </div>
    </div>
</template>

<script>

export default {
    name:"BarChart",
    props: ['listdata']
}
</script>

<style scoped>
.chart-box{
    margin: 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    width: 100%;
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
    width: 100%;
    align-content: center;
}

</style>

