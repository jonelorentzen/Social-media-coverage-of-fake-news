<template>
    <div>
        <justlist v-for="(title, index) in titles" :key="index" :title="title"/>
    </div>
</template>

<script>
import Justlist from '../components/JustList.vue'

export default {
    name: "SearchList",
    components: {
        Justlist,
    },
    computed: {
        titles(){
            return this.$store.state.searches;
        }
    },
};
</script>

<style>

</style>