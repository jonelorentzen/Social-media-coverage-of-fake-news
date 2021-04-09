<template>
    <button class="btn btn-secondry" @click="onSignIn()">
            <a href="https://api.twitter.com/oauth/request_token">
                <img :src="'' + require('@/assets/sign-in-twitter.png') + ''" alt=""><br>
            </a>
            </button>
</template>

<script>
// import Twitter from 'twitter-lite';

export default {
    name: 'signInBtn',
    methods:{
        onSignIn(){

        }
    }
}
</script>

<style>

</style>