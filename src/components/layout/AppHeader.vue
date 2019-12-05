<template>
  <header :class="{'fixed': scrollPosition>0||$route.path=='/home'}">
    <header-message :scrollPosition="scrollPosition"></header-message>
    <div id="headerContent">
      <main-menu 
        v-if="!isMobile"
        :scrollPosition="scrollPosition"
        :links="links"
        :categories="categories"
        @search="search"
      ></main-menu>
      <categories v-if="!isMobile" :scrollPosition="scrollPosition" :categories="categories"></categories>

      <mobile-menu v-if="isMobile"></mobile-menu>

    </div>
  </header>
</template>

<script>
import HeaderMessage from "@/components/layout/header/HeaderMessage.vue";
import MainMenu from "@/components/layout/header/MainMenu.vue";
import MobileMenu from "@/components/layout/header/MobileMenu.vue";
import Categories from "@/components/layout/header/Categories.vue";

export default {
  name: "MainHeader",

  props: {
    links: Array,
    categories: Array,
    isMobile: Boolean,
  },

  data() {
    return {
      scrollPosition: null
    };
  },

  methods: {
    updateScroll() {
      this.scrollPosition = window.scrollY;
      console.log(window.scrollY);
    },
    search(query) {
      this.$emit("search", query);
    }
  },

  mounted() {
    window.addEventListener("scroll", this.updateScroll);
  },

  components: {
    HeaderMessage,
    MainMenu,
    Categories,
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
  z-index: 500;
}
</style>
