<template>
  <section id="popularSection">
    <div class="wide-container">
      <div id="popuplarWrap">
        <div id="popularTitleWrapWrap">
          <div id="popularTitleWrap">
            <h2>Популярное</h2>
          </div>
        </div>

        <div id="popularItemsWrap">
          <carousel
            :autoplay="false"
            :loop="false"
            :centerMode="true"
            :perPage="4"
            :paginationEnabled="false"
          >
            <slide v-for="i in popularItems" :key="i.id">
              <item :popularData="i"></item>
            </slide>
          </carousel>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Item from "@/components/Item.vue";
export default {
  name: "PopularSection",
  props: {
    popularItems: Array
  },
  components: {
    Item
  }
};
</script>
<style scoped>
#popularSection{
  background: #888

}
#popuplarWrap {
  position: relative;
  overflow: visible;
  padding: 4em;

}
#popularTitleWrapWrap {
  position: absolute;
  top: -3em;
  display: flex;
  width: 100%;
  z-index: 200;
}
#popularTitleWrap {
  position: relative;
  padding: 1em 10em;
  background: black;
  color: #ddd;
  margin: auto;
}
#popularItemsWrap{
  z-index: 300;
}
</style>