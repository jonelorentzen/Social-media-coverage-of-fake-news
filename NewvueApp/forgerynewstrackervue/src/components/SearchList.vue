<template>
    
    <div v-if="titles.length > 0" class="query-container">
        <table>
            <tr v-for="(title, index) in titles" v-bind:key="index">

                <td>{{title.title}}</td> 
                <br>
                <div :class="{'active': title.active}" class="toggle_container">
                    <toggle-switch :searchIndex="index" @change="triggerToggleEvent"/>
                </div>
            </tr>
        </table>
    </div>
    
</template>

<script>
import ToggleSwitch from '../components/ToggleSwitch.vue';


export default {
    name: "SearchList",
   components:{
       ToggleSwitch
   },
    computed: {
        titles(){
            return this.$store.state.searches;
        }
    },
    data(){
        return{
            toggleActive: false
        }
    },
    methods: {
        triggerToggleEvent(value) {
            this.toggleActive = value;
        }
    },
    
};
</script>

<style>

.query-container{
    width: 100%;
    border: 1px black solid;
}
   
table{
    width: 100%;
}

table tr{
    border-bottom: 1px black solid;
}

.toggle_container.active {
    background: #009427;
}
   

</style>