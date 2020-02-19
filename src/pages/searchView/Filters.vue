<template>
  <aside>
    <price-filter v-model="priceBorders" :min="priceDefaults.lowest" :max="priceDefaults.highiest" :title="'Цена'" ref="priceFilter"></price-filter>
    <my-filter
      v-model="checkedCategories"
      id="categoryFilter"
      ref="categoryFilter"
      :options="categories"
      :checked="[category]"
      title="Категория"
    ></my-filter>
    <my-filter v-model="checkedBrands" id="brandFilter" ref="brandFilter" :options="brands" title="Брэнд"></my-filter>
    <my-filter v-model="checkedCountries" id="coutryFilter" ref="coutryFilter" :options="countries" title="Страна"></my-filter>
    <div class="clear-filtes">
      <button @click="reset" class="reset-btn">
        <span>Очистить фильтры</span>
      </button>
    </div>
  </aside>
</template>

<script>
import Filter from "@/components/Filter.vue";
import PriceFilter from "@/components/FilterPrice.vue";
import axios from "@/js/AxiosInstance.js";

export default {
  data() {
    return {
      category: this.$route.params.id,
      categories: [],
      brands: [],
      countries: [],
      priceDefaults: {},
      checkedCategories: [],
      checkedBrands: [],
      checkedCountries: [],
      priceBorders: [],
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
    priceBorders(){
      this.throwValue();
    },
  },
  async mounted() {
    const filters = (await axios.post("get-filters")).data;
    this.categories = filters.categories;
    this.brands = filters.brands;
    this.countries = filters.countries;
    this.priceDefaults = filters.price || {lowest: 1, highiest: 20000};
  },
  methods:{
    throwValue(){
      this.$emit("filterChange", {
        categories: this.checkedCategories,
        brands: this.checkedBrands,
        countries: this.checkedCountries,
        lowestPrice: this.priceBorders[0],
        highiestPrice: this.priceBorders[1],
      });
    },
    reset(){
      this.checkedCategories = [];
      this.checkedBrands = [];
      this.checkedCountries = [];
      this.priceBorders = [];

      this.$refs.categoryFilter.reset();
      this.$refs.brandFilter.reset();
      this.$refs.coutryFilter.reset();
      this.$refs.priceFilter.reset();
    },
  },
  components: {
    MyFilter: Filter,
    PriceFilter
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

.reset-btn{
  text-decoration: none;
  color: #222;
  padding: 18px 40px;
  margin: 0px 0 10px 0;
  background: linear-gradient(180deg, #bbb 5%, #E9E9E9 150%);
  border: 2px solid #222;
  font-size: 18px;
  position: relative;
  transition: color .3s;
  width: 100%;
  cursor: pointer;
}
.reset-btn:after{
  content: '';
  display: block;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0px;
  transition: height .3s;
  background: #222;
  z-index: 100;
}
.reset-btn span{
  position: relative;
  z-index: 200;
}
.reset-btn:hover:after{
  height: 100%;
}
.reset-btn:hover{
  color: white;
}
@media (max-width: 1300px) {
  aside {
    margin: 1em .2em;  
  }
}
@media (max-width: 500px) {
  aside {
    max-height: unset;
  }
}
</style>