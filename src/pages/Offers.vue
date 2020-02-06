<template>
  <main id="offersPage" :class="{'padded-top': scrollPosition !== 0}">
    <div class="wide-container">
      <div class="title-section">
      <div class="title-wrap">
  
        <h2 class="title">Акции</h2>
        <span class="line"></span>
      </div>
      </div>
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
    offers: Array,
    scrollPosition: Number,
  },
  components: {
    Item
  }
};
</script>
<style scoped>
main {
  background-color: #280909;
}
#offersPage{
  background-image: url('../assets/patternBlack.png');
}
#offersPage.padded-top .wide-container{
  padding-top: 15em;
}
#offersPage .wide-container {
  background: #7d6b6ba6;
  padding: 3em 0em;
}
#offerWrap {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 1em;
}
.title-section{
  width: 100%;
  display: flex;
  overflow: hidden;
  position: relative;
}
.title-wrap{
  background: black;
  direction: inline-block;
  padding: .25em 8em .25em 6em;
  clip-path: polygon(0 0, 100% 0, 85% 100%, 0 100%);
  position: relative;
  left: -1em;
  display: flex;
}
.title{
  color: #ccc;
}
.line{
  background: red;
  height: 100%;
  width: 4em;
  position: absolute;
  right: 0;
  top: 0;
  display: block;
  clip-path: polygon(70% 0, 100% 0, 100% 100%, 0 100%);
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
  #offersPage .wide-container {
    padding: 3em 0em;
  }
}
</style>

