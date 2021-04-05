<template>
    <div class="geochart-box-container">
        <div class="header">
            Locations
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
    padding: 10px;   
    height: 400px;
    padding-top: 25px;
}

.geochart-container{
    align-items: center;
    width: 650px;
    margin: auto;
    
}

.header{
  display: flex;
  padding: 10px;
  font-family: Quicksand,Helvetica,Arial,sans-serif;
  font-weight: 900;
  font-size: 1.25em;
  line-height: 1.5;
  color: #26293c;
}

</style>

