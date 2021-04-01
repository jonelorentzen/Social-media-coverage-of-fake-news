<template>
  <div class="container">
          <h3>Users</h3>
          <div>
              <users/>
          </div>
          <div>
              <button @click="gotoPage()">Create new Account</button>
          </div>

  </div>
</template>

<script>
// import Sidebar from '../components/Sidebar.vue';
import Users from '../components/Users.vue';

export default {
    name: 'LandingPage',
    components:{
        // Sidebar,
        Users,
    },
    data(){
        return{
            Sidebar: true
        }
    },
    methods: {
    gotoPage() {
      this.$router.push('/LoginPage');
    },
  }
    // computed:{
    //     UserData() {
    //   return this.$localStorage.name('Users')
    // },
    // }
}
</script>

<style>

</style>