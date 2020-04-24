<template>
  <div id="searchView">
    <filters @filterChange="filterChange"></filters>
    <found-data-view
      @pageSelected="getNewPage"
      @find="find"
      :current-page="page"
      :max-page="maxPage"
      :data="displaydata"
    ></found-data-view>
  </div>
</template>

<script>
import FoundDataView from "@/pages/searchView/FoundDataView.vue";
import Filters from "@/pages/searchView/Filters.vue";

export default {
  props: ["scrollPosition", "foundData"],
  data() {
    let displaydata = this.foundData ? this.foundData.data : [];
    let page = this.foundData ? this.foundData.current_page : 1;
    let maxPage = this.foundData ? this.foundData.last_page : 1;
    return {
      displaydata,
      page,
      maxPage,
      pages: []
    };
  },
  mounted() {
    this.$emit("pageSelected", 1);
    this.$emit("find", "");
  },
  watch: {
    foundData() {
      this.displaydata = this.foundData.data;
      this.page = this.foundData.current_page;
      this.maxPage = this.foundData.last_page;
    }
  },
  methods: {
    getNewPage(i) {
      this.$emit("pageSelected", i);
    },
    filterChange(newFilters) {
      console.log(newFilters);
      
      this.$emit("filtersChanged", newFilters);
    },
    find(query) {
      this.$emit("find", query, true);
    }
  },
  components: {
    FoundDataView,
    Filters
  }
};
</script>

<style scoped>
#searchView {
  display: flex;
  justify-content: space-between;
  background-color: #e9e9e9;
  background-image: url("../assets/patternBlack.png");
  background-size: 300px;
}
#searchView.not-top {
  margin: 10% auto 0 auto;
}
@media (max-width: 500px) {
  #searchView {
    flex-direction: column;
  }
}
</style>

