<template>
  <header :class="{'fixed': scrollPosition>0||$route.path=='/home'}">
    <div id="headerContent">
      <main-menu 
        v-if="!isMobile"
        :scrollPosition="scrollPosition"
        :links="links"
        :categories="categories"
        @search="search"
      ></main-menu>


      <mobile-menu :scrollPosition="scrollPosition" :links="links" v-if="isMobile"></mobile-menu>

    </div>
  </header>
</template>

<script>
import MainMenu from "@/components/layout/header/MainMenu.vue";
import MobileMenu from "@/components/layout/header/MobileMenu.vue";

export default {
  name: "MainHeader",

  props: {
    links: Array,
    categories: Array,
    isMobile: Boolean,
    scrollPosition: Number,
  },

  methods: {
    search(query) {
      this.$emit("search", query);
    }
  },
  components: {
    MainMenu,
    MobileMenu
  }
};
</script>
<style scoped>
header.fixed {
  position: fixed;
}
header {
  width: 100%;
  position: relative;
  z-index: 99999;
}
</style>
