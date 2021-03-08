import { createWebHistory } from 'vue-router';
import Ping from '../components/Ping.vue';
import Home from '../views/Home.vue'
import { createRouter } from 'vue-router';
// import Start from '../views/Start.vue';
import BarChart from '../components/BarChart.vue'

// here we create our routes
export default createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [{
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/barchart',
    name: 'barchart',
    component: BarChart,
  }
  ],
});
