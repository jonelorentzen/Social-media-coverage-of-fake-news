import { createWebHistory } from 'vue-router';
import Ping from '../components/Ping.vue';
import Home from '../views/Home.vue';
import Yourtrackers from '../views/Yourtrackers.vue';
import { createRouter } from 'vue-router';
// import Start from '../views/Start.vue';
import Dashboard from '../views/Dashboard.vue';
import Dashboard2 from '../views/Dashboard2.vue';
import About from '../views/About.vue';
import FAQ from '../views/FAQ.vue';

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
    path: '/yourtrackers',
    name: 'Yourtrackers',
    component: Yourtrackers
  },
  {
    path: '/dashboardONHOLD',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/dashboard',
    name: 'Dashboard2',
    component: Dashboard2
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
   path: '/faq',
    name: 'faq',
    component: FAQ
  }

  ]
});
