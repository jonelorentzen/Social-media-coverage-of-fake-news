<template>
  <div class="about">
    <div class="logo">
            <img :src="'' + require('@/assets/logo-main-2.png') + ''" alt=""><br>
    </div>
    <div>
      <h1>About us!</h1>
      
      <p> We are a group of 3 students studying computer science at the University of Stavanger. This website is our bacheor thesis. Enjoy!</p>

    </div>
    

  </div>
</template>

<script>
export default {
    name: 'About',
    
};
</script>


<style scoped>
.about{
  width: 100%;
  color: black;
  text-align: center;
  padding-top: 75px;

}

img{
    height: 300px;
}

h1{
  padding-top: 100px;
  font-weight: 2em;
}

p{
  padding-top: 50px;
}
</style>