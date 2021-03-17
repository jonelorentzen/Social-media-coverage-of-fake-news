<template>
    <label for="toggle_button">
        <span v-if="isActive" class="toggle__label">On</span>
        <span v-if="!isActive" class="toggle__label">Off</span>

        <input type="checkbox" id="toggle_button" v-model="checkedValue">
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
            firstTime: false 
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
                // hit api only ones, not reapeded api call if toggle swithed on again. 
    
                this.$store.dispatch("searchItemActive",this.searchIndex) 
                this.$emit('change', this.$store.getters.getSearchByIndex(this.searchIndex).active);
                if (this.firstTime == false){
                    this.$store.dispatch("getResult", this.$store.getters.getSearchByIndex(this.searchIndex).title)
                    this.firstTime = true
                }
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