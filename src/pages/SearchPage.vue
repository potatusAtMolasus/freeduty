<template>
  <div id="searchView" :class="{'not-top': scrollPosition}">
    <filters @filterChange="filterChange"></filters>
    <found-data-view :data="foundData"></found-data-view>
  </div>
</template>

<script>
import FoundDataView from '@/pages/searchView/FoundDataView.vue';
import Filters from '@/pages/searchView/Filters.vue';

export default {
  props:{
    scrollPosition: Number,
    foundData: Array,
  },
  methods:{
    filterChange(newFilters){
      this.$emit("filtersChanged", newFilters);
    },
  },
  components:{
    FoundDataView,
    Filters,
  },
}
</script>

<style scoped>
#searchView{
  display: flex;
  justify-content: space-between;
  background-color: #E9E9E9;
  background-image: url('../assets/patternBlack.png');
}
#searchView.not-top {
  margin: 10% auto 0 auto; 
}
</style>