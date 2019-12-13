<template>
  <aside>
    <my-filter
      v-model="checkedCategories"
      id="categoryFilter"
      :options="categories"
      :checked="[category]"
      title="Категория"
    ></my-filter>
    <my-filter v-model="checkedBrands" id="brandFilter" :options="brands" title="Брэнд"></my-filter>
    <my-filter v-model="checkedCountries" id="coutryFilter" :options="countries" title="Страна"></my-filter>
  </aside>
</template>

<script>
import Filter from "@/components/Filter.vue";
import axios from "axios";

export default {
  data() {
    return {
      category: this.$route.params.id,
      categories: [],
      brands: [],
      countries: [],
      checkedCategories: [],
      checkedBrands: [],
      checkedCountries: []
    };
  },
  watch: {
    checkedCategories() {
      this.throwValue();
    },
    checkedBrands() {
      this.throwValue();
    },
    checkedCountries() {
      this.throwValue();
    },
  },
  async mounted() {
    const filters = (await axios.post("http://localhost:5000/get-filters"))
      .data;
    this.categories = filters.categories;
    this.brands = filters.brands;
    this.countries = filters.countries;
  },
  methods:{
    throwValue(){
      this.$emit("filterChange", {
        categories: this.checkedCategories,
        brands: this.checkedBrands,
        countries: this.checkedCountries
      });
    }
  },
  components: {
    MyFilter: Filter
  }
};
</script>

<style>
aside {
  margin: 1em 2em;
  max-height: 90vh;
  flex: 1;
  position: -webkit-sticky;
  position: sticky;
  top: 0;
}
@media (max-width: 500px) {
  aside {
    max-height: unset;
  }
}
</style>