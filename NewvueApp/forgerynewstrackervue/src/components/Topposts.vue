<template>
    <div class="influential-posts-container">
    <div class="post-wrapper" v-for="(data,index) in topPosts" :key="index">
      <div class="profile-info">
          <img id="profile-picture" v-bind:src="data.img">
          <p class="tweet-username">@{{data.username}}</p>
          <p id="date">{{data.date}}</p>
      </div>
      <div class="tweet-stats">
          <p id="retweets">{{data.retweets}}</p>
          <img id="retweet-image" src="../assets/clipart2858379.png"> 
          <p id="likes">{{data.likes}}</p>
          <img id="like-image" src="../assets/PikPng.com_red-heart-emoji-png_1669725.png">
      </div>
          <p class="tweet-text">"{{data.text}}"</p>
      </div>
      
    </div>
    
    
</template>

<script>
export default {
    name: "topPosts",
    computed: {
      topPosts(){
        return this.$store.state.TopPosts
      }
    }

}
</script>

<style scoped>



.influential-posts-container{  
  width: 660px;
  height: 528px;
  position: relative;
  
  line-height: 1.4em;
  margin-right: 0;
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