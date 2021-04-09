<template> 
    <div v-if="titles.length > 0" class="query-container">
        <table>
            <tr v-for="(title, index) in titles" v-bind:key="index"  v-on:click="check(index)" :style="title.active ? { 'background-color': '#32CD32' } : null">
            <transition name="slide-fade">
                
                <td v-show="title.loaded == true">{{title.title}}</td> 
            </transition>
                
                <br>
                    <div v-show="title.loaded == false"><img class="loadingspin" src="../assets/spinner-transparent.gif" alt=""></div>
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
.slide-fade-enter-active {
  transition: all 1.2 ease-out;
}

.slide-fade-leave-active {
  transition: all 1.2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}

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