<template>
    <div>
        <column-chart :data="listdata" :colors="['#666']"></column-chart>
    </div>
</template>

<script>

export default {
    name:"BarChart",
    props: ['listdata']
}
</script>
