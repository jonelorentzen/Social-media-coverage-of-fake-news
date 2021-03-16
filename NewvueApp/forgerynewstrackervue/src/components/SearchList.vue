<template>
    
    <div v-if="titles.length > 0" class="query-container">
        <table>
            <tr v-for="(title, index) in titles" v-bind:key="index">
                <td>{{title}}</td> 
            </tr>
        </table>
    </div>
    
</template>

<script>


export default {
    name: "SearchList",
    components: {
        
    },
    computed: {
        titles(){
            return this.$store.state.searches;
        }
    },
    data(){
        return{
            active: true,
        }
    },
};
</script>

<style>

.query-container{
    width: 100%;
    border: 1px black solid;
}
   
table{
    width: 100%;
    

}

table tr{
    
    border-bottom: 1px black solid;

}


   

</style>