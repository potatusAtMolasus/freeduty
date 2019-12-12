<template>
  <div id="searchWrap" v-click-outside="()=>showFull=searchQuery.length">
    <div :class="{searchBox: true, showFull: showFull}">
      <input v-model="searchQuery" class="searchInput" @keyup="typing" type="text" placeholder="Поиск" />
      <button class="searchButton" @click="searchClicked">
        <i v-if="showFull" class="fa fa-arrow-right" aria-hidden="true"></i>
        <i v-if="!showFull" class="fa fa-search" aria-hidden="true"></i>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      searchQuery: "",
      showFull: false,
      timeout: null
    };
  },
  methods: {
    // async 
    searchClicked() {
      if (!this.showFull){
        this.showFull = true;
      }
      else{
        this.$emit('search', this.searchQuery);
      }
    },
    typing(){
      clearTimeout(this.timeout);
      if (this.searchQuery.length < 4){
        return;
      }
      var self = this;
      this.timeout = setTimeout(() => self.$emit('search', self.searchQuery), 1000);
    }
  }
};
</script>
<style scoped>
#searchWrap {
  position: relative;
  width: 320px;
  display: flex;
  justify-content: right;
}
.searchBox {
  margin: auto 2em;
  background: red;
  height: 40px;
  border-radius: 40px;
  padding: 10px;
}

.showFull.searchBox {
  background: #2f3640;
}

.showFull.searchBox > .searchInput {
  width: 150px;
  padding: 0 6px;
}

.showFull.searchBox > .searchButton {
  background: white;
  color: #2f3640;
}

.searchButton {
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: red;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: 0.4s;
  outline: none;
}
button:active, button:focus, a:active, a:focus {
  outline: none;
}
.searchInput {
  border: none;
  background: none;
  outline: none;
  float: left;
  padding: 0;
  color: white;
  font-size: 16px;
  transition: 0.4s;
  line-height: 40px;
  width: 0px;
}

@media screen and (max-width: 620px) {
  .showFull.searchBox > .searchInput {
    width: 150px;
    padding: 0 6px;
  }
}
</style>