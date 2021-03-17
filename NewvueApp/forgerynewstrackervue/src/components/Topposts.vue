<template>


   <!-- <div class="topposts_box">
     <div class="topposts_header">
       <h3><span>Top Posts</span></h3>
     </div>
     <div class="topposts_container">
       <div class="toppostsRows_wrapper" v-for="data in data_list" :key="data">
         <div class="toppostsRow">
           <div class="profile-info">
            <img id="profile-picture" v-bind:src="data.img">
            <p class="tweet-username">@{{data.username}}</p>
            <p id="date">{{data.date}}</p>
          </div>
      <div class="tweet-stats">
          <p id="retweets">{{data.retweets}}</p>
          <img id="retweet-image" src="static/clipart2858379.png"> 
          <p id="likes">{{data.retweets}}</p>
          <img id="like-image" src="static/PikPng.com_red-heart-emoji-png_1669725.png">
      </div>
          <p class="tweet-text">"{{data.text}}"</p>
         </div>
       </div>
       <div class="topposts_footer">

       </div>
     </div>
   </div> -->


    
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

.topposts_box{
  grid-column: span 6 / auto;
}

.topposts_header h3{
  font-size: 1.1em;
  line-height: 1.25;
  font-weight: 900;
  color: #44496b;
  font-family: Quicksand,Helvetica,Arial,sans-serif;
  margin: 0;
}

.topposts_container{
  padding: 0;
  display: flex;
  flex: 1;
  flex-direction: column;
  transition: .2s ease-in-out;
  border: 1px solid #dddfea;
  
}

.toppostsRows_wrapper{
  padding-bottom: 1.9em;
}

.toppostsRow{
  display: flex;
  flex-direction: row;
  padding: 1em 2em;
  margin-top: -1px;
  min-height: 6.75em;
  border-top: 1px solid #edeef4;
  border-bottom: 1px solid #edeef4;
  cursor: pointer;
  
}


.influential-posts-container{  
  width: 660px;
  height: 528px;
  position: relative;
  margin:auto;
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