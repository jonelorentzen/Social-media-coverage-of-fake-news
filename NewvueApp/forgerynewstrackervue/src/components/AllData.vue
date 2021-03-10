<template>
<!-- https://www.youtube.com/watch?v=LvOYCjpMQ10&ab_channel=ModusCreate%2CInc. -->
    <div>
        {{ alldata }}
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'AllData',
    components: {

    },
    data() {
        return {
            alldata: '',
        };
    },
    methods: {
        getMessage() {
            const path = 'http://localhost:5000/showinfo';
            axios.post(path, {id:5}).then((res) => {
                this.alldata = res.data;
            })
            .catch((error) => {
                console.error(error);
            });
        },
    },
    created() {
        this.getMessage();
    },
}
</script>