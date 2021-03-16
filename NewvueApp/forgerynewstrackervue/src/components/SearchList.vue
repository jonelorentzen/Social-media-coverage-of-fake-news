<template>
    <div>
    <div v-if="titles.length > 0"> 
        <table >
            <tr>
                <td>
                <justlist class="row" v-for="(title, index) in titles" :key="index" :title="title"/>
                </td>
            </tr>
        </table>
    </div>
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