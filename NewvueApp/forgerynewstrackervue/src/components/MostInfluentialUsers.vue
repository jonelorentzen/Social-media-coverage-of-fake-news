<template>
    
    
    <div class="mostinfluentialcontainer">
       
      <div class="influencercontainer" v-for="(user, index) in topUsers" v-bind:key="index">
      <div class="influencerwrapper">
        <div class="influencerusernamecontainer">
          <p class="influencername"> <strong>{{user.username}}</strong></p>
          <fa class="twitter-icon" :icon="['fab', 'twitter']"></fa>
        </div>
        <div class="influencerinfo_wrapper">
                 
          <div class="influencerfollowercount_container">
            <p>{{user.followers}} Followers</p> 
          </div>
          
          <div class="influencerfollowingcount_container">
            <p> </p>
          </div>
        
        </div>
      </div>
    </div>

      

    </div>
    

   
   
 
</template>

<script>
export default {
    name: "topUsers",
    computed: {
      topUsers(){
        return this.$store.state.TopUsers
      }
    }
  
}
</script>

<style scoped>

.mostinfluentialcontainer{
  max-width: 50%;
  display: flex;
  justify-content:space-evenly;
  flex-wrap: wrap;
  border: 1px solid #dddfea;
  padding: 20px;
  margin-left: 10px;
  
}

.influencercontainer{
  border: 1px solid grey;
  width: 150px;
  height: 150px; 
  display: grid;
  
  flex-basis: 33%;
  
}
.influencerwrapper{
  width: -webkit-calc(100% - 4em);
  width: calc(100% - 4em);
  margin: auto;
}
.influencercontainer:hover{
  background-color: whitesmoke;
}
.influencerusernamecontainer{
  display: inline-flex;
}
.influencername{
  font-weight: 600;
  font-size: .9em;
  white-space: nowrap;
  max-width: -webkit-calc(100% - .1em);
  max-width: calc(100% - .1em);
  overflow: hidden;
  -o-text-overflow: ellipsis;
  text-overflow: ellipsis;
  font-weight: 700;
  color: #44496b;

}
.influencerfollowercount_container{

  font-size: .85em;
  color: #828282;
  color: #8086ae;
}
.influencerfollowingcount_container{
  font-size: .85em;
  color: #828282;
  color: #8086ae;
}

img{
  width: 20px;
}

.nav-bar {
  background: linear-gradient(-90deg, #84CF6A, #16C0B0);
  height: 60px;
  margin-bottom: 15px;
}

.twitter-icon{
  color: #00acee;
}


.influential-posts-container{  
  width: 660px;
  height: 528px;
  position: relative;
  margin:0 auto;
  line-height: 1.4em;
}

.post-wrapper{
  border: 1px lightgrey solid;
  padding: 10px 14px;
  position: relative;
}

.profile-info{
  display: inline-flex;
  align-items: center;
  font-size: 20px;
}

#headline{
  padding: 8px;

}
#profile-picture{
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.tweet-text{
  color: #8086AE;
  font-size: .9em;
}

.tweet-username{
  text-overflow: ellipsis;
  font-weight: 700;
  color: #44496b;
  padding-left: 5px;
}

.tweet-stats{
  position: absolute;
  top: 0px;
  right: 20px;
  display: inline-flex;
  align-items: center;
}

#retweet-image{
  width: 18px;
  height: 12px;
  padding-right: 7px; 
}

#like-image{
  width: 15px;
  height: 12px;
}

#date{
  font-size: .7em;
  padding-top: 1.1px;
  padding-left: 7px;
  color: #8086AE;
}


.influential-users-container{
  width: 640px;
  height: 483px;
  display: flex;                       
  flex-wrap: wrap;                    
  justify-content: space-around;
}
.user-wrapper{
  border: 1px lightgrey solid;
  width: 32%;
  height: 10px;
  padding-bottom: 18%; 
  margin-bottom: 2%; 
}

.user-info{
  display: inline-flex;
  align-items: center;
  font-size: 20px;
  margin: 7px;
}

#follower-count{
  padding-left: 50px;
  color: #8086AE;

}
</style>