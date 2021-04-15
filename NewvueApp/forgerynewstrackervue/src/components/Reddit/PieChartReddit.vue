<template>
     <div class="chart-box">
       <div class="chartheader">
        <h3>Percentage of Votes Reddit</h3>
        <div class="help-tip-container">
                <div class="help-tip">
                    <p>The pie chart displays the ratio between upvotes versus downvotes. </p>
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
}
.post_texts{
  margin-top: .2em;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  font-size: .9em;
  line-height: 1.5;
  overflow: hidden;
  font-weight: 500;
  color: #8086ae;
  padding-right: 50px;
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
