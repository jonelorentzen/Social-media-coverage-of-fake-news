<template>
    <div>
    <div class="table-container" v-if="titles.length>0">
        <table class="table table-striped">
            <tr>
                <td>
        
                <justlist class="row" v-for="(title, index) in titles" :key="index" :title="title"/>
                </td>
               
                
            </tr>
        </table>
        
    </div>
    <div v-else>

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