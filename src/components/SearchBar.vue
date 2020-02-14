<template>
  <div id="searchWrap" v-click-outside="()=>showFull=searchQuery.length">


    <div :class="{searchBox: true, showFull: showFull}">
      <div class="field">
        <input v-model="searchQuery" class="searchInput" @keyup="typing" type="text" @keyup.enter="find" placeholder="Поиск" />
        <button class="searchButton" @click="searchClicked">
          <i v-if="showFull" class="fa fa-arrow-right" aria-hidden="true"></i>
          <i v-if="!showFull" class="fa fa-search" aria-hidden="true"></i>
        </button>
      </div>


      <div id="dropDownList" :class="{'show': showFull}">
        <div v-for="item in dropdownList" :key="item.id" class="list-item">
          <router-link :to="'/item/' + item.id">

            <div class="item-wrap" @click="searchQuery='';showFull=false;dropdownList=[]">
              <span class="image">
                <img :src="getImgUrl(item.image)" :alt="item.title">
              </span>
              <span class="title">{{item.title}}</span>
              <span class="price">{{item.sale ? item.salePrice : item.price}}</span>
            </div>
          </router-link>  
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/js/AxiosInstance.js";

export default {
  name: "SearchBar",
  data() {
    return {
      searchQuery: "",
      showFull: false,
      timeout: null,
      dropdownList: [],
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
        this.dropdownList = []
        return;
      }
      var self = this;
      // this.timeout = setTimeout(() => self.$emit('search', self.searchQuery), 1000);
      this.timeout = setTimeout(() => self.find(self.searchQuery), 1000);
    },
    async find(query){      
      this.dropdownList = (await axios.post("find", { query, category: '' })).data;
      this.$router.push({ path: "/search/" });
    },
    getImgUrl(pic) {
      try{
        return require('../assets/'+pic);
      } catch(e) {
        return '';
      }
    },
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
  border-radius: 40px;
  position: relative;
}
.field{
  height: 40px;
  z-index: 100;
  height: 40px;
  border-radius: 40px;
  padding: 10px;
  z-index: 200;
  position: relative;
}

.showFull .field, .showFull.searchBox{
  background: #2f3640;
}
.showFull.searchBox .searchInput {
  width: 150px;
  padding: 0 6px;
}

.showFull.searchBox .searchButton {
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
  z-index: 100;
  position: absolute;
  right: .75em;
}
.showFull.searchBox .searchButton{
  position: absolute;
  right: .5em;
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
  width: 40px;
  z-index: 100;
  display: flex;
}

#dropDownList{
  position: absolute;
  background-color: #ccccccc4;
  border-radius: 40px;
  padding-top: 60px;
  z-index: 50;
  overflow: hidden;
  top: 0px;
  max-height: 0;
  transition: all .5s linear; 
  width: 100%;
  opacity: 0;
}
#dropDownList.show{
  max-height: 1000px;
  opacity: 1;
}
.list-item{
  height: 80px;
  width: 100%;
  border-bottom: 1px solid #888;
}
.item-wrap{
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: 80px;
  padding: 5px;
  box-sizing: border-box;
  cursor: pointer;
}
.item-wrap:hover{
  background: #888c;
}

.image{
  width: 50%;
}
.image img{
  width: 100%;
}
.title{
  padding: 0 10px;
  line-height: 1.5em;
  height: 3em;
  overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-box-orient: vertical;
   -webkit-line-clamp: 2;
}
.price{
  color: #a90000;
}


@media screen and (max-width: 620px) {
  .showFull.searchBox > .searchInput {
    width: 150px;
    padding: 0 6px;
  }
}
</style>