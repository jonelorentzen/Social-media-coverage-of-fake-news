<template>
    <div>
        <line-chart :data="listdata" :colors="['#d00']" xtitle="Tweeted at" ytitle="Cumulative Tweets"></line-chart>
    </div>
</template>

<script>

export default {
    name:"LineChart",
    props: ['listdata']
}
</script>
