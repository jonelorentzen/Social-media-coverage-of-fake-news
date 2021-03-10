<template>
  <div>
    <div>
      <button type="button" class="btn btn-primary">{{ msg }}</button>
    </div>
    <search-box />
    <all-data />
  </div>
</template>

<script>
import axios from 'axios';
import SearchBox from './SearchBox.vue';


export default {
  name: 'Ping',
  components: {
    SearchBox,
  },
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
