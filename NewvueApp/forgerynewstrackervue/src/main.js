import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import Chartkick from 'vue-chartkick';
import Chart from 'chart.js';


createApp(App)
  .use(store)
  .use(router)
  .use(Chartkick.use(Chart))
  .mount("#app");
