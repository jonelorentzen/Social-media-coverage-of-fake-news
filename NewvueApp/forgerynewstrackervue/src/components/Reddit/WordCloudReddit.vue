<template>

<div class="entire_container">
  <div class="chartheader">
      <h3>Popular Subreddits</h3>
      <div class="help-tip-container">
                <div class="help-tip">
                    <p>The top subreddits are displayed here, the size of the subreddit is relative to how many posts from the selected query are posted in the subreddit. 
                        You can click any of the subreddits to check out the subreddit in Reddit.
                    </p>
                </div>
            </div>
    </div>
  <div class="toppostsbox">
        <div class="toppostswrapper">
          <div class="postrow">
            
            <ul class="cloud" role="navigation" aria-label="Webdev word cloud">
                <li v-for="(entry, index) in listdata" v-bind:key="index" @click="gotopost(listdata[index]['subreddit'])"><a :data-weight="listdata[index]['value']">{{listdata[index]["subreddit"]}}</a></li>
            </ul>

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
      gotopost(id){
        window.open(`https://www.reddit.com/r/${id}`)
      }
    } 
}
</script>

<style scoped>

.entire_container{
  display: flex;
  flex-direction: column;
  height: 100%;
  
}

.toppostsbox{
  border: 1px solid #dddfea;
  padding: 20px;
  height: 100%;
}

.postrow{
  width: 600px;
  font-family: tiempos headline,Georgia,times new roman,Times,serif;
}

.chartheader{
    height: 45px;
    display: flex;
}
.chartheader h3{
    font-weight: 900;
    font-size: 1.25em;
    line-height: 1.5;
}


ul.cloud {
  list-style: none;
  padding-left: 0;
  padding-top: 75px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

ul.cloud a {
  --size: 4;
  --color: #a33;
  color: var(--color);
  font-size: calc(var(--size) * 0.25rem + 0.5rem);
  display: block;
  padding: 0.125rem 0.25rem;
  position: relative;
  text-decoration: none;
}

ul.cloud a[data-weight="1"] { --size: 4; }
ul.cloud a[data-weight="2"] { --size: 6; }
ul.cloud a[data-weight="3"] { --size: 8; }
ul.cloud a[data-weight="4"] { --size: 10; }
ul.cloud a[data-weight="5"] { --size: 13; }


ul[data-show-value] a::after {
  content: " (" attr(data-weight) ")";
  font-size: 1rem;
}

ul.cloud li:nth-child(2n+1) a { --color: #181; }
ul.cloud li:nth-child(3n+1) a { --color: #33a; }
ul.cloud li:nth-child(4n+1) a { --color: #c38; }

ul.cloud a:focus {
  outline: 1px dashed;
}

ul.cloud a::before {
  content: "";
  position: absolute;
  top: 0;
  left: 50%;
  width: 0;
  height: 100%;
  background: var(--color);
  transform: translate(-50%, 0);
  opacity: 0.15;
  transition: width 0.25s;
}

ul.cloud a:focus::before,
ul.cloud a:hover::before {
  width: 100%;
}

@media (prefers-reduced-motion) {
  ul.cloud * {
    transition: none !important;
  }
}

</style>