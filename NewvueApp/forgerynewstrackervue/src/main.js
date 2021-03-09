import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import Chartkick from 'vue-chartkick'
import Chart from 'chart.js'

Chartkick.configure({language: "de", mapsApiKey: "AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY"})


createApp(App)
  .use(store)
  .use(router)
  .use(Chartkick.use(Chart))
  .mount("#app");
