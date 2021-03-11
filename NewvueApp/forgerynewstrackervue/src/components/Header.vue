<template>
    <header id="absolute-main-header">
        <div id="inner">
            <div id="header-container">
                <nav class="navbar navbar-expand-lg navbar-dark">
                    <div class="container-fluid">
                        <a class="navbar-brand" @click="gotoHOME()">Forgery News Tracker</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav mr">
                            <li class="nav-item">
                            <a class="nav-link active nav-link-light" aria-current="page" @click="gotoHOME()">Home</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" @click="gotoABOUTus()">About Us</a>
                            </li>
                            <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Help
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="#">FAQ</a></li>
                                <li><hr class="dropdown-divider"></li>
                                <li><a class="dropdown-item" href="#">Tutorial</a></li>
                            </ul>
                            </li>
                        </ul>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    name: "Header",
    methods:{
        gotoHOME(){
            this.$router.push('/')
      },
      gotoABOUTus(){
        this.$router.push('/about')
      },
    }
    
}
</script>

<style scoped>
.navbar{
    min-height: 100px;
    font-size: 30px;
    background-color: #26293C;
    color: #FFFFFFBF;
}
.container-fluid{
    color: #FFFFFFBF;

}
.navbar-brand{
    font-size: 40px;
}
.nav.navbar-nav.navbar-right li a {
    color: white;
}
</style>