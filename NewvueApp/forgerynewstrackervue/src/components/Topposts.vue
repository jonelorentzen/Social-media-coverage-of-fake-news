<template>



  <div class="toppostsbox">
      
        <div class="toppostswrapper">
          <div class="postrow" v-for="(post, index) in topPosts" v-bind:key="index">
            <div class="profilepicture_container">
                <img class="profilepicture" v-bind:src="topPosts[index].img">
              </div>
            
            <div class="postrow_wrapper">
              
              <div class="postinfo_wrapper">
                
                <div class="postinfo_container">
                  
                  <p class="postinfo">
                    <strong>@{{topPosts[index].username}}</strong>
                  </p>
  
                  <p>{{topPosts[index]["date"]}}</p>
                </div>

                <div class="post_engagement">
                  <fa class="retweets" icon="retweet"/>
                    <p >{{topPosts[index].retweets}}</p>

                  <fa class="likes" icon= "heart"/>
                    <p >{{topPosts[index].likes}}</p>
                </div>

              </div>

              <p class="post_texts">
                {{topPosts[index].text}}
              </p>
            
            </div>


          </div>
          
    
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
    },
    props:['listdata']

}
</script>

<style scoped>

.toppostsbox{
  max-width: 50%;
  display: flex;
  justify-content:space-evenly;
  flex-wrap: wrap;
  border: 1px solid #dddfea;
  padding: 20px;
  width: 100%;
  margin-right: 10px;
}


.toppostswrapper{
  
}
.postrow{
  border: 1px solid grey;
  width: 600px;
  height: 150px;
  margin-bottom: 10px;
  display: flex;
  padding: 30px;
  
}

.postrow:hover{
  background-color: whitesmoke;
}
.profilepicture{
  width: 50px;
  height: 60px;
  border-radius: 15px;
}

.profilepicture_container{
  margin: auto;
  font-size: 1.25em;
  margin-right: .75em;
  margin-top: .25em;
  
}
.postrow_wrapper{
  margin: auto;
}

.postinfo_wrapper{
  display: flex;
}

.post_engagement{
  display: flex;
  
  position: absolute;
  left: 807px;
}
.retweets{
color: #00acee;
}

.likes{
  color: #cf2945;
}

.postinfo_container{
  display: flex;
  margin-right: 150px;
  font-size: .85em;
  color: #828282;
  
}
.postinfo{
  font-weight: 600;
  font-size: 1.1em;
  white-space: nowrap;
  max-width: -webkit-calc(100% - .1em);
  max-width: calc(100% - .1em);
  overflow: hidden;
  -o-text-overflow: ellipsis;
  text-overflow: ellipsis;
  font-weight: 700;
  color: #44496b;
}

.post_engagement{
  font-size: .9em;
  display: inline-flex;

}
.post_engagement p{
  margin-left: 5px;
  margin-right: 10px;
}

.post_texts{
  margin-top: .2em;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  font-size: .9em;
  line-height: 1.5;
  overflow: hidden;
  font-weight: 500;
  color: #8086ae;
}


</style>