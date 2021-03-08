<template>
    <div class="container">
        <h2>Welcome back @{{twitteruser}}</h2><br>
        <div>
            <h3>Please enter what you want to search for. Or choose an already made query below</h3> <br>
            <search-box/><br>
            <select v-model="selected">
                <option disabled value="">Please select one</option>
                <option>Trump</option>
                <option>Barack Obama is white</option>
                <option>Corona changes DNA</option>
                <option>Apple is made by Microsoft</option>
            </select>
            <span>Selected: {{ selected }}</span>
            
            <h3></h3>

        </div>
        
    </div>
</template>

<script>
//here we import other components
import SearchBox from '../components/SearchBox.vue';

export default {
    name: 'Home',
    components: {
        SearchBox,
    },
    data: function() {
        return {
            twitteruser: 'Dönerkebab123',
            }
},
};
</script>