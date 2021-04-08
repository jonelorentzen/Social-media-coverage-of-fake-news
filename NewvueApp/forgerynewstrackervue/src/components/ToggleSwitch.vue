<template>
    <label for="toggle_button">
        <span v-if="isActive" class="toggle__label">On</span>
        <span v-if="!isActive" class="toggle__label">Off</span>

        <input type="checkbox" id="toggle_button"  v-model="checkedValue"  @change="check($event)">
        <span class="toggle__switch"></span>
    </label>
</template>
<script>

export default {
    props: {
        defaultState: {
            type: Boolean, 
            default: false
        },
        searchIndex: {
            type: Number,
            default: -1
        }
    },

    data() {
        return {
            currentState: this.defaultState,
            checked: [],
            max: 2
            
        }
    },
    computed: {
        isActive() {
            return this.$store.getters.getSearchByIndex(this.searchIndex).active
        },

        checkedValue: {
            get() {
                return this.$store.getters.getSearchByIndex(this.searchIndex).active
            },
            set() {
                this.checked.push(this.searchIndex)
                this.$store.dispatch("searchItemActive",this.searchIndex) 
            }
        }
    },
    methods: {
        //Want to call this function with the index of query in the searchlist. Then connect it with the dictionary that stores the index in the tweets list to the index
        //in the search list. Dont know how to get the index of the query that is untoggled. 
        //The idea is if the checkbox is untoggled, it calls this function with the index, for ex: the searchlist=[0, 1X, 2, 3X], tweets=[1,3] and index= {1:0, 3:1}.
        //
        //You untoggle 3, here and the function check with the parameter 3. In the store it checks the index dict first to find the index for tweets.
        //With index[3] you get back 1, then you pop(1) from the tweet list to remove the data also remove the key 3 from the index dict.
        //
        //When you toggle on there should be a check if the API has been called, if not the index of the searchlist should be sent to a function in
        //the store, that adds the 

        check: function(event){
            if (event.target.checked == true){
               this.$store.dispatch("addTweetToDisplay", this.searchIndex)
            } else{
                this.$store.dispatch("removeFromTweets", this.searchIndex);
            }  
        }
    },

}
</script>

<style scoped>
.toggle__button {
    vertical-align: middle;
    user-select: none;
    cursor: pointer;
}
.toggle__button input[type="checkbox"] {
    opacity: 0;
    position: absolute;
    width: 1px;
    height: 1px;
}
.toggle__button .toggle__switch {
    display:inline-block;
    height:12px;
    border-radius:6px;
    width:40px;
    background: #BFCBD9;
    box-shadow: inset 0 0 1px #BFCBD9;
    position:relative;
    margin-left: 10px;
    transition: all .25s;
}

.toggle__button .toggle__switch::after, 
.toggle__button .toggle__switch::before {
    content: "";
    position: absolute;
    display: block;
    height: 18px;
    width: 28px;
    border-radius: 50%;
    left: 0;
    top: -3px;
    transform: translateX(0);
    transition: all .25s cubic-bezier(.5, -.6, .5, 1.6);
}

.toggle__button .toggle__switch::after {
    background: #4D4D4D;
    box-shadow: 0 0 1px #666;
}
.toggle__button .toggle__switch::before {
    background: #4D4D4D;
    box-shadow: 0 0 0 3px rgba(0,0,0,0.1);
    opacity:0;
}
</style>