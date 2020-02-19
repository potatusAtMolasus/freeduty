<template>
  <div class="content">
    <main>
      <banner></banner>
      <offers-section :homeOffers="homeOffers" :isMobile="isMobile" :offers="offers"></offers-section>
      <popular-section :isMobile="isMobile" :width="width" :popularItems="popular"></popular-section>
      <blog-section :isMobile="isMobile" :posts="homePosts"></blog-section>
    </main>
  </div>
</template>

<script>
import OffersSection from "@/pages/home/OffersSection.vue";
import PopularSection from "@/pages/home/PopularSection.vue";
import BlogSection from "@/pages/home/BlogSection.vue";
import Banner from "@/pages/home/Banner.vue";

export default {
  props: {
    offers: Object,
    homeOffers: Array,
    popular: Array,
    posts: Object,
    isMobile: Boolean,
    width: Number,
  },
  components: {
    Banner,
    OffersSection,
    PopularSection,
    BlogSection
  },
  computed:{
    homePosts(){
      return this.posts.data ? this.posts.data.slice(0, 5) : []
    }
  },
};
</script>
<style scoped>
#page {
  display: flex;
  height: 100vh;
}
</style>