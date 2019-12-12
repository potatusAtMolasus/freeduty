<template>
  <main id="offersPage">
    <div class="container">
      <h2>Акции</h2>
      <div id="offerWrap">
        <offer v-for="i in offers" :key="i.id" :offerData="i"></offer>
      </div>
    </div>
  </main>
</template>

<script>
import Offer from "@/components/Item.vue";

export default {
  props: {
    offers: Array
  },
  components: {
    Offer
  }
};
</script>
<style>
main {
  background-color: #ccc;
}
#offersPage .container {
  background: #999;
  padding: 3em 1em;
}
#offerWrap {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
#offerWrap .offer-wrap.outer {
  margin: 1em;
}
#offerWrap .offer-wrap {
  background: white;
  box-shadow: none;
}
#offerWrap .offer-wrap {
  background: white;
  box-shadow: none;
  border: 1px solid red;
}
#offerWrap .offer-wrap:hover {
  box-shadow: none;
}
#offerWrap .offer-wrap:hover .discount{
  transform: none;
}
#offerWrap .offer-wrap:hover .discount img{
  filter: none; 
}
</style>
<style scoped>
main {
  background-image: url('../assets/patternBlack.png');
}
</style>

