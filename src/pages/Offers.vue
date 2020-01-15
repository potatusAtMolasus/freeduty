<template>
  <main id="offersPage">
    <div class="container">
      <h2>Акции</h2>
      <div id="offerWrap">
        <item v-for="i in offers" :key="i.id" :item="i"></item>
      </div>
    </div>
  </main>
</template>

<script>
import Item from "@/components/Item.vue";

export default {
  props: {
    offers: Array
  },
  components: {
    Item
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
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  flex-wrap: wrap;
  justify-content: space-between;
}
@media(max-width: 992px){
  #offerWrap {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
  }
}
@media(max-width: 768px){
  #offerWrap {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
  }
}
@media(max-width: 576px){
  #offerWrap {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
  #offersPage .container {
    padding: 3em 0em;
  }
}
</style>
<style scoped>
main {
  background-image: url('../assets/patternBlack.png');
}
</style>

