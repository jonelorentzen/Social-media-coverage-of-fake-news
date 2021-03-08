<template>
    <div>
        <line-chart :data="chartData"></line-chart>
    </div>
</template>

<script>

export default {
    name: "BarChart",
    data(){
        return{
            chartData: {
                '2017-05-13T:13:03:00': 1,
                '2017-05-13T:14:03:00': 2,
                '2017-05-13T:15:03:00': 3,
                '2017-05-13T:16:03:00': 4,
            }
        }
    }
  
}
</script>
