<template>
  <aside>
    <my-filter id="categoryFilter" :options="categories" :checked="[category]" title="Категория"></my-filter>
    <my-filter id="brandFilter" :options="brands" title="Брэнд"></my-filter>
    <my-filter id="coutryFilter" :options="countries" title="Страна"></my-filter>
  </aside>
</template>

<script>
import Filter from '@/components/Filter.vue';
import axios from "axios";

export default {
  data(){
    return {
      category: this.$route.params.id,
      categories: [],
      brands: [],
      countries: [],
    };
  },
  async mounted(){
    const filters = (await axios.post("http://localhost:5000/get-filters")).data; 
    this.categories = filters.categories;
    this.brands = filters.brands;
    this.countries = filters.countries;
  },
  components:{
    MyFilter: Filter
  },
}
</script>

<style>
aside{
  margin: 1em 2em;
  max-height: 90vh;
  flex: 1;
  position: -webkit-sticky;
  position: sticky;
  top: 0;
}
</style>