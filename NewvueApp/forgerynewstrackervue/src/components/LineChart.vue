<template>
    <div>
        <area-chart :data="listdata" :colors="['#d00']" xtitle="Tweeted at" ytitle="Cumulative Tweets"></area-chart>
    </div>
</template>

<script>

export default {
    name:"LineChart",
    props: ['listdata']
}
</script>
