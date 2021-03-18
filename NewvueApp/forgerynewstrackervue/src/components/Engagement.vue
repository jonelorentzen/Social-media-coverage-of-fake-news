<template>
    <div class="engagement-wrapper">

        <div class="engagement-container">

            <div class="topstats">
                <fa icon="comments" size="2x"/>
                <h1>{{activity.posts}}</h1>
                <p>Posts</p>
            </div>

            <div class="topstats">
                <fa icon="user" size="2x"/>
                <h1>{{activity.users}}</h1>
                <p>Users</p>
            </div>

            <div class="topstats" >
                <fa icon="heart" size="2x"/>
                <h1 class="display display-">{{activity.engagement}}</h1>
                <p>Engagement</p>
            </div>

        </div>

    </div>
</template>

<script>

export default {
    name: "activity",
    computed: {
      activity(){
        return this.$store.state.activity
      },
    }
}
</script>

<style scoped>
.engagement-wrapper{
    
    height: 150px;
    background-color: #ffd443;
    display: flex;
    justify-content: center;
    align-items: center;
    
}

.engagement-container{
    justify-content: space-evenly;
    margin: auto;
    display: flex;
   
    width: 100%;

    min-width: none;
    

}

.topstats{
    width: 100px;
    height: 70px;
    display: grid;
    grid-template-columns: 3em auto;
    grid-template-rows: 1fr 1em;
    margin-right: 120px;

}

</style>