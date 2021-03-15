<template>
  <div><p>{{title.title}}</p></div>
</template>

<script>
export default {
    props:["title"]

}
</script>

<style scoped> 

div{

  border: 1px black solid;
  height: 100px;

}
div p{
  text-align: center;
  
  

}
</style>