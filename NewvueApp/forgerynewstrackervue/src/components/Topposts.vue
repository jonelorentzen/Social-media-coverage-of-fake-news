<template>


<div class="entire_container">
  <div class="header">
      Top Posts
    </div>
  <div class="toppostsbox">
        <div class="toppostswrapper">
          <div class="postrow" v-for="(post, index) in listdata" v-bind:key="index" @click="gotopost(listdata[index].username, listdata[index].id)">
            
           
            <div class="profilepicture_container">
                <img class="profilepicture" v-bind:src="listdata[index].img">
              </div>
            
            <div class="postrow_wrapper">
              
              <div class="postinfo_wrapper">
                
                <div class="postinfo_container">
                  
                  <p class="postinfo">
                    <strong>@{{listdata[index].username}}</strong>
                  </p>
  
                  <p class="date">{{listdata[index]["date"]}}</p>
                </div>

                <div class="post_engagement">
                  <fa class="retweets" icon="retweet"/>
                    <p >{{listdata[index].retweets}}</p>

                  <fa class="likes" icon= "heart"/>
                    <p >{{listdata[index].likes}}</p>
                </div>

              </div>

              <p class="post_texts">
                {{listdata[index].text}}
              </p>
            
            </div>

            
          </div>
    </div>
  </div>

  </div>
    

       
</template>

<script>
export default {
    name: "topPosts",
    props:['listdata'],
    methods:{
      gotopost(username, id){
        window.open(`https://twitter.com/${username}/status/${id}`)
      }
    } 
   

}
</script>

<style scoped>

.entire_container{
  display: flex;
  flex-direction: column;
}
.header{
  display: flex;
  padding: 10px;
  font-family: Quicksand,Helvetica,Arial,sans-serif;
  font-weight: 900;
  font-size: 1.25em;
  line-height: 1.5;
  color: #26293c;
}

.toppostsbox{
  
  display: flex;
  justify-content:space-evenly;
  flex-wrap: wrap;
  border: 1px solid #dddfea;
  padding: 20px;
  width: 99%;
  margin-right: 10px;
}


.postrow{
  border: 1px solid grey;
  width: 600px;
  height: 150px;
  margin-bottom: 10px;
  display: flex;
  padding: 20px;
  transition: all 0.3s;
  
}

.postrow:hover{
  background-color: whitesmoke;
}
.profilepicture{
  width: 50px;
  height: 60px;
  border-radius: 50%;
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
  font-size: .9em;
  display: inline-flex;
 
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
  margin-right: 10px;

}
.date{
  padding-top: 1px;
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
  padding-right: 50px;
}


</style>