<template>
  <main>
    <div id="sortWrap">
      <div class="selector-wrap">
        <span>Сортировать по </span>
        <div > 
          <combobox :options="comboOptions" v-model="sortBy"></combobox>
        </div>
      </div>
    </div>
    <div id="wrap">
      <div v-for="i in items" :key="i.id">
        <item :item="i"></item>
      </div>
    </div>
  </main>
</template>

<script>
import Item from "@/components/Item.vue";
import Combobox from '@/components/Combobox.vue';

export default {
  props: {
    data: Array,
  },
  data(){
    return {
      items: [],
      sortBy: '',
      comboOptions: [
        {label: 'По возрастанию цены', value: 'priceIncr'},
        {label: 'По уменьшению цены', value: 'priceDecr'},
        {label: 'По популярности', value: 'popularity'},
      ]
    }
  },
  watch:{
    data(){
      this.items = this.data;
    },
    sortBy(){
      console.log(this.sortBy)
      if(this.sortBy === 'popularity') {
        this.items = this.items.sort((a, b)=>b.popularity - a.popularity);
      }
      else if(this.sortBy === 'priceIncr')
        this.items = this.items.sort((a, b)=>{
          const aPrice = a.sale ? a.salePrice : a.price;
          const bPrice = b.sale ? b.salePrice : b.price;
          return aPrice - bPrice;
        });
      else if(this.sortBy === 'priceDecr')
        this.items = this.items.sort((a, b)=>{
          const aPrice = a.sale ? a.salePrice : a.price;
          const bPrice = b.sale ? b.salePrice : b.price;
          return bPrice - aPrice;
        });
    },
  },
  components: {
    Item,
    Combobox,
  },
};
</script>
<style scoped>
main {
  flex: 3;
  margin: 0 2em 0 0;
  background-color: #ccccccee;
}

#sortWrap{
  padding: 1em;
  display: flex;
  justify-content: right;
  position: relative;
  width: auto;
  height: 2em;
}
.selector-wrap{
  display: flex;
  position: absolute;
  z-index: 200;
}
.selector-wrap span{
  padding-right: 1em; 
  position: relative;
  top: 1em;
}
.selector-wrap>div{
  position: relative;
}
.outer-wrap {
  background: white;
  margin: 0.5em 0.5em;
}
.combo-wrap{
  display: inline;
}
#wrap {
  padding: 1em;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-gap: 0em;
}
@media (max-width: 500px) {
  main {
    margin: 0;
  } 
  #wrap {
    padding: 1em;
    grid-template-columns: 1fr 1fr;
  }
  .selector-wrap span{
    padding-right: 0;
  } 
}
</style>
