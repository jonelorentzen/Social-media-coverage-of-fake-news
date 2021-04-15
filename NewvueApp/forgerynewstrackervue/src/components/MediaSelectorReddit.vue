<template>

    <div class="media-container">
        <h1 class="display-1">
            Choose social media:
        </h1>
    
        
        <div  class="logo-container">    
            <div class="logo">
                <img :src="'' + require('@/assets/twitterlogo.png') + ''" alt="" @click="gotoTwitter()" id="twitter">
            </div>
            <div class="logo">
                <img :src="'' + require('@/assets/redditlogo.png') + ''" alt="" @click="gotoReddit()" id="reddit">
                <fa class="checkmarkreddit" icon="check-circle"/>
            </div>    
        </div>
    </div>

    


    
    
    
</template>

<script>
export default {
    name: "topUsers",
    data(){
        return{
            isReddit: false,
            isTwitter: true
        }     
    },
    props:['listdata'],
     methods: {
        gotoTwitter() {
            this.isReddit = !this.isReddit
            this.isTwitter = !this.isTwitter
            console.log("Reddit", this.isReddit)
            console.log("Twitter", this.isTwitter)
            this.$router.push('/dashboard');
            
    },
        gotoReddit() {
            this.isReddit = !this.isReddit
            this.isTwitter = !this.isTwitter
            console.log("Reddit", this.isReddit)
            console.log("Twitter", this.isTwitter)
            this.$router.push('/dashboardreddit');
            

            
    },
  }
}
</script>

<style scoped>

.display-1{
margin: 0;
max-width: 100%;
overflow: hidden;
-o-text-overflow: ellipsis;
text-overflow: ellipsis;
white-space: nowrap;
padding-right: .5em;
font-size: .8rem;
color: #bec1d6;
font-family: Quicksand,Helvetica,Arial,sans-serif;
font-weight: 700;
text-transform: uppercase;
line-height: 1.25;
margin-top: .35em;
}

.media-container{
    display: flex;
    flex-direction: column;
    margin-left: auto;
    
}
.logo-container{
    display: flex;
    width: 150x;
   margin-left: auto;
   position: relative;
    
}

.checkmarktwitter{
    position: absolute;
    top: 5px;
    left: 40px;
    color: #6af011;
}

.checkmarkreddit{
    position: absolute;
    top: 5px;
    right: 5px;
    color: #6af011;
}


.logo{
    border: 3.5px #dddfea solid;
    border-radius: 10px;
}

img{
    width: 50px;
    height: 50px;
}


#check{
    width: 25px;
    height: 25px;
}
#reddit{}



</style>