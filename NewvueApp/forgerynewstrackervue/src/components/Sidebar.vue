<template>
    <div class="border-right" id="sidebar-wrapper">
      <div class="list-group list-group-flush">

        <a @click="gotoDASHBOARD()" class="list-group-item list-group-item-action">Dashboard</a>
        <a @click="gotoYT()" class="list-group-item list-group-item-action">Your Trackers</a>
        <a @click="gotoABOUTus()" class="list-group-item list-group-item-action">About us</a>

      </div>
    </div>
</template>

<script>
export default {
    name: "Sidebar",
    methods: {
      gotoYT(){
        this.$router.push('/yourtrackers')
      },
      gotoABOUTus(){
        this.$router.push('/about')
      },
      gotoDASHBOARD(){
        this.$router.push('/dashboard')
      }
    }
}
</script>

<style scoped>
#wrapper {
    overflow-x: hidden;
 }

#sidebar-wrapper {
  min-height: 100vh;
  margin-left: -15rem;
  -webkit-transition: margin .25s ease-out;
  -moz-transition: margin .25s ease-out;
  -o-transition: margin .25s ease-out;
  transition: margin .25s ease-out;
  background-color: #30344C;
}

#sidebar-wrapper .sidebar-heading {
  padding: 0.875rem 1.25rem;
  font-size: 1.2rem;
}

#sidebar-wrapper .list-group {
  width: 15rem;
}

#page-content-wrapper {
  min-width: 100vw;
}

#wrapper.toggled #sidebar-wrapper {
  margin-left: 0;
}

@media (min-width: 768px) {
  #sidebar-wrapper {
    margin-left: 0;
  }

  #page-content-wrapper {
    min-width: 0;
    width: 100%;
  }

  #wrapper.toggled #sidebar-wrapper {
    margin-left: -15rem;
  }
  a{
    background-color: #30344C;
    color: #FFFFFF80;
  }
}
</style>