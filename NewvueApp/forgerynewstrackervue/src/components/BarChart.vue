<template>
    <div>
        <column-chart :data="listdata" :colors="['#l00']"></column-chart>
    </div>
</template>

<script>

export default {
    name:"BarChart",
    props: ['listdata']
}
</script>
