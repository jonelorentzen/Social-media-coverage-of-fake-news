<template> 
    <div v-if="titles.length > 0" class="query-container">
        <table>
            <tr v-for="(title, index) in titles" v-bind:key="index"  v-bind:class='{ "not_selected": title.active == false, "selected": title.active == true, "non_clickable": tweets_displayed == 2 && title.active == false}'
            v-on:click="check(index)">
                
                <td v-show="title.loaded == true">{{title.title}}</td> 
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
        },
        tweets_displayed(){
            return this.$store.state.tweets.length;

        }
    },  
    methods: {
        check: function(index){
            if(this.tweets_displayed == 2 && this.titles[index].active == false){
                alert("You cannot add more than 2 queries at the same time. Please remove one of the already selected to add this query.")
    
            }else{
                if(this.titles[index].loaded == true){
                    if(this.titles[index].active == false){
                    this.$store.dispatch("addTweetToDisplay", index)
                    console.log(this.tweets_displayed)
                }else{
                    this.$store.dispatch("removeFromTweets", index);
                    console.log(this.tweets_displayed)
                }}
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
table td{
    font-family: tiempos headline,Georgia,times new roman,Times,serif;
    font-size: 1.5em;
}

tr:hover{
    opacity: 0.8;
}

.toggle_container.active {
    background: #009427;
}
.loadingspin{
    width: 60px;
}

.not_selected{
    background-color: white;
}

.selected{
    background-color: #32CD32;

}

.non_clickable{
    background-color: #C0C0C0;
}
</style>