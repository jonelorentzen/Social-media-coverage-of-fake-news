<template> 
    <div v-if="titles.length > 0" class="query-container">
        <table>
            <tr v-for="(title, index) in titles" v-bind:key="index"  v-on:click="check(index)" :style="title.active ? { 'background-color': '#32CD32' } : null">
                
                <td v-show="title.loaded == true">{{title.title}}</td> 
                
                <br>
                    <div v-show="title.loaded == false"><img class="loadingspin" src="../assets/loading-spinnr.gif" alt=""></div>
            </tr>
        </table>
    </div>
    
</template>

<script>


export default {
    name: "SearchList",
    computed: {
        titles(){
            return this.$store.state.searches;
        }
    },  
    methods: {
        check: function(index){
            if(this.titles[index].active == false){
                this.$store.dispatch("addTweetToDisplay", index)
            }else{
                this.$store.dispatch("removeFromTweets", index);
            }
        },
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
    height: 75px;
}

.toggle_container.active {
    background: #009427;
}
.loadingspin{
    width: 60px;
}

</style>