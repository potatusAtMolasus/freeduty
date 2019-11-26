<template>
  <section id="offersSection">
    <div class="wide-container">
      <h2 id="offers-title">Наши Акции</h2>

      <div id="offersContent">
        <div
          id="offersText"
        >Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate asperiores placeat consequatur? Eos excepturi soluta placeat reiciendis rerum. Delectus eaque ea nemo eveniet fugiat qui pariatur ab illum error aspernatur deleniti cumque animi laboriosam tempora eligendi rem corporis quae, esse atque nam accusamus aliquam. Soluta accusantium recusandae velit quia dolorem!</div>
        <div id="offersWrap">
          <carousel
            :autoplay="false"
            :loop="false"
            :centerMode="true"
            :perPage="3"
            :paginationEnabled="false"
          >
            <slide v-for="i in offers" :key="i.id">
              <offer :offerData="i"></offer>
            </slide>
          </carousel>
        </div>
      </div>

      <div id="watchOffersWrap">
        <router-link id="offersBtn" to="/offers">Все акции</router-link>
      </div>
    </div>
  </section>
</template>

<script>
import Offer from "@/components/Offer.vue";

export default {
  name: "OffersSection",
  props: {
    offers: Array
  },
  components: {
    Offer
  }
};
</script>
<style scoped>
#offersContent {
  display: flex;
  justify-content: space-between;
}
#offersWrap {
  margin: 3em;
}
.VueCarousel-wrapper {
  padding: 30px 15px;
}
#offersWrap {
  flex: 3;
  overflow: hidden;
}
#offersText {
  flex: 1;
  background: black;
  height: 100%;
  width: 30%;
  color:#ddd;
  padding: 1.5em;
  line-height: 1.5em;
}
</style>
