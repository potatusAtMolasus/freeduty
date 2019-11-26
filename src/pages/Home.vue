<template>
  <div class="content">
    <main>
      <banner></banner>
      <offers-section :offers="offers"></offers-section>
      <popular-section :popularItems="popular"></popular-section>
      <blog-section></blog-section>
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
    popular: Array
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