<template>
  <div class="container">
      <!-- https://github.com/draftbit/twitter-lite -->
      <div>
          <p>Login with twitter. You will login with own account and then get a PIN code which you copy. This PIN code needs to be pasted in the field to autheticate your user </p>
      </div>
      <div>
          
           <button class="btn btn-secondry" @click="onSignIn()">
            <a>
                <img :src="'' + require('@/assets/sign-in-twitter.png') + ''" alt=""><br>
            </a>
            </button>
          
        

      </div>
  </div>
</template>

<script>
import TwitterLogin from '../backend_api/twitter.js';


export default {
    name:  'LoginPage',
     methods:{
       
       onSignIn(){
          let signIn = new TwitterLogin()
          signIn.Login()
        }
    }
}
</script>

<style>

</style>