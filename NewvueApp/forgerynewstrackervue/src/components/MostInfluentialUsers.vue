<template>
    <div class="influential-users-with-headline">
    <div class="influential-users-container">

        <div class="user-wrapper" v-for="(data,index) in topUsers" :key="index">
            <div class="user-info">
            <img id="profile-picture" v-bind:src="data.img">
            <p class="tweet-username">@{{data.username}}</p>
        </div>
        <div id="follower-count">
            <p id>{{data.followers}} Followers</p>
            </div>
        </div>
    

        </div>
    </div>
</template>

<script>
export default {
    name: "topusers",
    computed: {
      topUsers(){
        return this.$store.state.TopUsers
      }
    }
  
}
</script>

<style scoped>

.nav-bar {
  background: linear-gradient(-90deg, #84CF6A, #16C0B0);
  height: 60px;
  margin-bottom: 15px;
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