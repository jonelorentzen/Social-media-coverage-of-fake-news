<template>
<!-- https://www.npmjs.com/package/vue3-carousel -->
<!-- https://www.photopea.com/ -->
<!-- an image should be this size: 1100x850 -->
  <carousel :items-to-show="1"  wrapAround="true" :snapAlign="center" :transition="150" class="carousel">
    <slide v-for="slide in slides" :key="slide" class="carousel">
    <img :src="require(`../assets/${slide.imgName}`)" :alt="hello">
    </slide>

    <template #addons>
      <navigation />
      <pagination />
    </template>
  </carousel>
</template>

<script>
// If you are using PurgeCSS, make sure to whitelist the carousel CSS classes
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';

export default {
  name: 'App',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data(){
      return{
          slides:[{
              imgName: "yourtrackersTut.png"
          },
          {
              imgName: "Searchlist.png"
          },
          {
              imgName: "timeline.png"
          },
          {
              imgName: "totalinter.png"
          },
          {
              imgName: "locations.png"
          },
          {
              imgName: "sentiment.png"
          },
          {
              imgName: "NodeNetwork.png"
          },
          {
              imgName: "Subreddits.png"
          },
          {
              imgName: "andMore.png"
          },

         ]
              
          
      }
  }
};
</script>

<style scoped>
    /* .carousel{
        width: 1500px;
        height: 80%;
    } */
</style>