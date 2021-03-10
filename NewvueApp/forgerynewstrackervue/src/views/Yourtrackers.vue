<template>
    <div class="container">
        <h2>Welcome back @{{twitteruser}}</h2><br>
        <div>
            <h3>Please enter what you want to search for. Or choose an already made query below</h3> <br>
            <input v-model="searchValue" class="form-control" type="text" placeholder="Search here">
              <button class="btn btn-primary" @click="getResult()">Get result</button><br><br>
        
            <select v-model="selected">
                <option disabled value="">Please select one</option>
                <option>Trump</option>
                <option>Barack Obama is white</option>
                <option>Corona changes DNA</option>
                <option>Apple is made by Microsoft</option>
            </select>

            
            <h3></h3>

        </div>
        
    </div>
</template>

<script>
//here we import other components
// import SearchBox from '../components/SearchBox.vue';



export default {
    name: 'Home',
    components: {
        
    },
    data() {
        return {
            twitteruser: 'Dönerkebab123',
            searchValue: '',
            };
    },
    methods: {

    },
    

  }
</script>

<style>
.container{
    color: black;
}



</style>