<template>
    <div class="container">
        <h2>Welcome @{{twitteruser}}</h2><br>

        <div>
            <h3>Please enter what you want to search for. Or choose an already made query below</h3>
            <select id="selected" v-model="selected">
                <option disabled>Premade searches</option>
                <option>Donald Trump</option>
                <option>Joe Biden</option>
                <option>Barack Obama is white</option>
                <option>Corona changes DNA</option>
                <option>Apple is made by Microsoft</option>
                <option>Humans waste too much water</option>
                <option>Jesus and I and are friends on Facebook</option>
                <option>The earth is flat</option>
            </select>
        <br>
            <input v-model="searchValue" class="form-control" type="text" placeholder="Search here">
            <button class="btn btn-primary" @click="addSearch();">Add search</button><br><br>

            <h4>Your Recent Searches</h4>
            <search-list/> <br>
            <button class="btn btn-primary" @click="gotoPage();">See results on DashBoard</button>
            
        </div>

    </div>
</template>

<script>
//here we import other components
// import SearchBox from '../components/SearchBox.vue';
// import store from '../store/index.js';
import SearchList from '../components/SearchList.vue';


export default {
    name: 'Home',
    components: {
        SearchList,

    },
    data() {
        return {
            twitteruser: 'Dönerkebab123',
            searchValue: '',
            selected: '',
            };
    },
    methods: {
        addSearch(){
            var dropValueElement = document.getElementById("selected");
            var text = this.searchValue

            if (text == "") {
                var option = dropValueElement.options[dropValueElement.selectedIndex].text
                this.$store.dispatch('addNewSearch',option)
                // this.$store.dispatch("getResult", option, this.active)
                this.searchValue = "";
                option = "";

            } else {
                text = this.searchValue
                this.$store.dispatch('addNewSearch',text)
                // this.$store.dispatch("getResult", text, this.active)
                this.searchValue = "";

            }
        },
        getResult(){
            this.$store.dispatch("getResult", this.$store.state.searches.active)
        },
        gotoPage() {
        this.$router.push('/Dashboard');
        },

    },



  };

</script>

<style>
.container{
    color: black;
}



</style>