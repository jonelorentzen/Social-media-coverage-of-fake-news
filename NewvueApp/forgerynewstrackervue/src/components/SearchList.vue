<template>
    <div styl>
        <table class="table table-striped">
            <tr>
                <justlist v-for="(title, index) in titles" :key="index" :title="title"/> <br>
            </tr>
        </table>
        
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