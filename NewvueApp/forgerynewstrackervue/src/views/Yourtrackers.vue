<template>

    <div class="container">
        <div class="logo">
            <img :src="'' + require('@/assets/logo2.png') + ''" alt=""><br>
        </div>
        <div class="row">
            <div class="col-2">
            </div>
            <div class="col-3" id="select-container">
                <div class="items-container">
                        <transition name="slide-fade">
                            <p v-if="show">Use our premade searches.</p>
                        </transition>
                            <div class="select">
                                <select id="selected" v-model="selected">
                                    <option disabled>Premade searches</option>
                                    <option>Donald Trump</option>
                                    <option>Joe Biden</option>
                                    <option>Barack Obama is white</option>
                                    <option>Corona changes DNA</option>
                                    <option>Apple is made by Microsoft</option>
                                    <option>Humans waste too much water</option>
                                    <option>The earth is flat</option>
                                </select>
                            </div>
                            
                    </div>
            </div>
            
            <div class="col-md-auto" id="item">
                <div class="items-container">
                <transition name="slide-fade">
                    <p v-if="show">
                        Write your own search.
                    </p>
                </transition>
                    <input v-model="searchValue" class="form-control" type="text" placeholder="Search here">
                
                </div>
            </div>

        

        </div>
        <div class="add-container"><button class="btn btn-primary" id="add-search" @click="addSearch();">Add search</button> </div>
        <div class="bottom">

            <button @click="showTut()" style="display: none">show tutorial</button>

            <h4 v-show="searchlist_length>0">Your Recent Searches</h4>
            <search-list/> <br>
            <button class="btn btn-primary" @click="gotoPage();">See results on Dashboard</button>
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
        gotoPage() {
        this.$router.push('/Dashboard');
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
   
    padding: 40px;
}
#item{
    

}

#select-container{
    

}


.items-container{
    
    
    
}
.add-container{
    padding-top: 20px;
}

.bottom{
    padding-top: 50px;
}

#add-search{
    width: 200px;
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
    width: 450px;
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
    width: 15em;
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

