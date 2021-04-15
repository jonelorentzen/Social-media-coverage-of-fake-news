<template>
    <div class="geochart-box-container">
        <div class="chartheader">
            <h3>Locations</h3>
            <div class="help-tip-container">
                <div class="help-tip">
                    <p>The geo chart represents the location of the users tweeting or interacting with the tweets. We only get the location that the user has defined, so this chart is not 100% accurate.</p>
                </div>
            </div>
        </div>
        <div class="geochart-box">
            <div class="geochart-container">
                <geo-chart :data="listdata" :messages="{empty: 'No data'}" width="600px"></geo-chart>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: "geochart",
    props:['listdata'],

    
}
</script>

<style scoped>
.geochart-box{
    align-items: center;
    border: 1px solid #dddfea;
    padding: 20px;
    
    height: 450px;
   
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
.geochart-container{
    padding-top: 35px;
}

</style>

