<template>
    <div class="logo-container">
        <div class="logo">
            <img :src="'' + require('@/assets/twitterlogo.png') + ''" alt="" @click="gotoTwitter()" id="twitter">
        </div>
        <div class="logo">
            <img :src="'' + require('@/assets/redditlogo.png') + ''" alt="" @click="gotoReddit()" id="reddit">
        </div>
    </div>
    
    
</template>

<script>
export default {
    name: "topUsers",
    props:['listdata'],
     methods: {
        gotoTwitter() {
            this.$router.push('/dashboard');
    },
        gotoReddit() {
            this.$router.push('/dashboardreddit');
    },
  }
}
</script>

<style scoped>

.logo-container{
    display: flex;
    width: 150x;
   
    
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