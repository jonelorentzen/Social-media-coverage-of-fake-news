<template>
   
    <div class="influential-posts-container">
    <div class="post-wrapper" v-for="data in data_list" :key="data">
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
    
</template>

<script>
export default {
    name: "topPosts",
    data(){
        return {
            data_list : [{"author_id": 1245312, "retweets": 6969, "number": 1, "img": "https://cdn2.thecatapi.com/images/iQpCnqHXc.jpg", 
    "username": "Catman", "text": "The recent studies shows that cats are able to get infected by COVID-19", "date": "Feb 12",
    "followers": 6.9, "verified": true}, 
    {"author_id": 134626, "retweets": 1234, "number": 2, "img": "https://www.w3schools.com/images/w3schools_green.jpg", 
    "username": "w3school", "text": "Here at W3 schools you can learn to code programs for COVID-19 or other things!", "date": "Feb 20",
    "followers": 6.9, "verified": true}, 
    {"author_id": 43568234, "retweets": 888, "number": 3, "img": "https://pbs.twimg.com/profile_images/1349837426626330628/CRMNXzQJ_normal.jpg", 
    "username": "PONTUS", "text":"Today I announced our Administration will: - Expand COVID-19 testing for schools and underserved communities - Increase manufacturing of testing supplies - Increase genome sequencing to track emerging strains",
    "date": "Feb 21", "followers": 6.9, "verified": true}] ,
    user_list: [{"img": "https://cdn2.thecatapi.com/images/iQpCnqHXc.jpg", "username": "Catman",  "date": "Feb 12", "followers": 69.6, "verified": true},
    {"img": "https://www.w3schools.com/images/w3schools_green.jpg", "username": "w3school", "date": "Feb 20", "followers": 2.1, "verified": true},
    {"img": "https://pbs.twimg.com/profile_images/1349837426626330628/CRMNXzQJ_normal.jpg", "username": "PONTUS", "followers": 19.7, "verified": true},
    {"img": "https://pbs.twimg.com/profile_images/1349837426626330628/CRMNXzQJ_normal.jpg", "username": "PONTUS", "followers": 19.7, "verified": true},
    {"img": "https://pbs.twimg.com/profile_images/1349837426626330628/CRMNXzQJ_normal.jpg", "username": "PONTUS", "followers": 19.7, "verified": true},
    {"img": "https://pbs.twimg.com/profile_images/1349837426626330628/CRMNXzQJ_normal.jpg", "username": "PONTUS", "followers": 19.7, "verified": true},
    {"img": "https://pbs.twimg.com/profile_images/1349837426626330628/CRMNXzQJ_normal.jpg", "username": "PONTUS", "followers": 19.7, "verified": true},
    {"img": "https://pbs.twimg.com/profile_images/1349837426626330628/CRMNXzQJ_normal.jpg", "username": "PONTUS", "followers": 19.7, "verified": true},
    {"img": "https://pbs.twimg.com/profile_images/1349837426626330628/CRMNXzQJ_normal.jpg", "username": "PONTUS", "followers": 19.7, "verified": true}]
        }
    },
    mounted(){
        console.log("DATALIST", this.data_list)
    }
}
</script>

<style scoped>





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