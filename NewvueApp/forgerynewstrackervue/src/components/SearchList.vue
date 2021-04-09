<template> 
    <div v-if="titles.length > 0" class="query-container">
        <table>
            <tr v-for="(title, index) in titles" v-bind:key="index"  v-bind:class='{ "not_selected": title.active == false, "selected": title.active == true, "non_clickable": tweets_displayed == 2 && title.active == false}'
            v-on:click="check(index)">
                
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
    background-color: #C0C0C0;
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