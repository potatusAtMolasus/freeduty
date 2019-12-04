<template>
  <div class="content">
    <main>
      <banner></banner>
      <offers-section :isMobile="isMobile" :offers="offers"></offers-section>
      <popular-section :isMobile="isMobile" :popularItems="popular"></popular-section>
      <blog-section :isMobile="isMobile" :posts="posts.slice(0, 5)"></blog-section>
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
    offers: Array,
    popular: Array,
    posts: Array,
    isMobile: Boolean,
  },
  components: {
    Banner,
    OffersSection,
    PopularSection,
    BlogSection
  }
};
</script>
<style scoped>
#page {
  display: flex;
  height: 100vh;
}
</style>