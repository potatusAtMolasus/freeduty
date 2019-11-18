<template>
  <div id="search-wrap">
    <input type="text" id="searchField" v-bind="searchQuery" />
    <button @click="searchClicked">Поиск</button>
  </div>
</template>

<script>
export default {
    name: 'SearchBar',
    data(){
        return {
            searchQuery: ''
        }
    },
    watch:{
        searchQuery(){
            alert(this.searchQuery);
        }
    },
    methods: {
        searchClicked: function(){
            alert(`clicked searc btn. Query: ${this.searchQuery}`);
        }
    }
}
</script>
