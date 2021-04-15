<template>

    <div class="container">
        <div class="logo">
            <img :src="'' + require('@/assets/logo-main-2.png') + ''" alt=""><br>
        </div>

        <div class="row">
            <div class="col-md-auto" id="item">
                <div class="items-container">
                <transition name="slide-fade">
                    <p v-if="show">
                        Write your own search.
                    </p>
                </transition>
                    <input v-model="searchValue" class="form-control" type="text" placeholder="Search here" maxlength="256">
                </div>
            </div>

        </div>

        <div class="row">
            <div class="col-6" id="select-container">
                <div class="items-container">
                        <transition name="slide-fade">
                            <p v-if="show">Use our premade searches.</p>
                        </transition>
                            <div class="select">
                                <select id="selected" v-model="selected">
                                    <option disabled>Premade searches</option>
                                    <option>America is the greatest country in the world</option>
                                    <option>Joe Biden is not president</option>
                                    <option>Covid-19 vaccine is dangerous</option>
                                    <option>Covid-19 is a hoax</option>
                                    <option>Corona virus is a hoax</option>
                                    <option>Barack Obama is white</option>
                                    <option>Corona changes DNA</option>
                                    <option>DMX received COVID vaccine days before heart attack </option>
                                    <option>Crypto is a scam</option>
                                </select>
                            </div> 
                    </div>
            </div>
        </div>
    
        <div class="row add-button">
            <button class="btn btn-secondary" id="add-search" @click="addSearch();">Add search</button> 
        </div>
        
        <div class="bottom" v-show="searchlist_length>0">
            <h4>Your Recent Searches</h4>
            <search-list/> <br>
            <button class="btn btn-primary" @click="gotoTwitter();">See results on Twitter</button>
            <button class="btn btn-danger" @click="gotoReddit();">See results on Reddit</button>
        </div>

    </div>
</template>

<script>
//here we import other components
import SearchList from '../components/SearchList.vue';


export default {
    name: 'Home',
    components: {
        SearchList,

    },
    computed:{
        searchlist_length(){
            return this.$store.state.searches.length
            
        }},

    data() {
        return {
            twitteruser: 'Dönerkebab123',
            searchValue: '',
            selected: '',
            show: false,

            };
    },
    methods: {
        showTut(){
            this.show = true
        },

        addSearch(){
            var dropValueElement = document.getElementById("selected");
            var text = this.searchValue

            if (text == "") {
                var option = dropValueElement.options[dropValueElement.selectedIndex].text
                this.$store.dispatch('addNewSearch',option)
                this.$store.dispatch("getResult", option)
                this.searchValue = "";
                option = "";

            } else {
                text = this.searchValue
                this.$store.dispatch('addNewSearch',text)
                this.$store.dispatch("getResult", text)
                this.searchValue = "";
            }
        },
        getResult(){
            this.$store.dispatch("getResult", this.$store.state.searches.active, )
        },
        gotoTwitter() {
        this.$router.push('/dashboard');
        },
        gotoReddit() {
        this.$router.push('/dashboardreddit');
        },
    },
    mounted(){
        this.showTut()
    }
  };

</script>

<style scoped>

.container{
    color: black;

}
.logo{
    padding: 25px;
}
.row{
   padding-top: 20px;
    align-items: center;
    justify-content: center;
}

img{
    height: 400px;
}

.add-button{
    padding-top: 40px;
}
#add-search{
    width: 150px;
}
h2{
    margin-bottom: 30px;
}
p{
    text-align: left;
}
.show-info-txt{
    text-align: center;
}
h4{
   text-align: left;
}
input{
    width: 700px;
    height: 45px;
    text-align: center;
    display: block;
}
/* Reset Select */
select {
  -webkit-appearance: none;
  -moz-appearance: none;
  -ms-appearance: none;
  appearance: none;
  outline: 0;
  box-shadow: none;
  border: 0 !important;
  background: #c2c2c2;
  background-image: none;
}
/* Remove IE arrow */
select::-ms-expand {
  display: none;
}
/* Custom Select */
.select {
    align-content: center;
    text-align: center;
    position: relative;
    display: flex;
    height: 3em;
    line-height: 3;
    background: #414447;
    overflow: hidden;
    border-radius: .25em;
}
select {
  flex: 1;
  padding: 0 .5em;
  color: #fff;
  cursor: pointer;
}
/* Arrow */
.select::after {
  content: '\25BC';
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 1em;
  background: #696262;
  cursor: pointer;
  pointer-events: none;
  -webkit-transition: .25s all ease;
  -o-transition: .25s all ease;
  transition: .25s all ease;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 2.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.slide-fade-enter-active {
  transition: all 2.5s ease-out;
}

.slide-fade-leave-active {
  transition: all 2.5s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(40px);
  opacity: 0;
}

</style>

