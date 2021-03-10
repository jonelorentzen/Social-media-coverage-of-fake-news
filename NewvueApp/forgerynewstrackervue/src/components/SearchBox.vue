<template>
    <div>
        <input v-model="searchValue" class="form-control"
        @keyup.enter="sendData()" type="text" placeholder="Search here">
    </div>
</template>

<script>
export default {
  name: 'SearchBox',
  data() {
    return {
      searchValue: '',
    };
  },
  methods: {
    sendData() {
      console.log(this.searchValue);
      return "daddad"
    },
  },
};
</script>

