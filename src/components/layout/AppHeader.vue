<template>
  <header>
    <header-message :scrollPosition="scrollPosition"></header-message>
    <div id="headerContent">
      <main-menu :scrollPosition="scrollPosition" :links="links" :categories="categories" @search="search"></main-menu>
      <categories :scrollPosition="scrollPosition" :categories="categories"></categories>
    </div>
  </header>
</template>

<script>
import HeaderMessage from "@/components/layout/header/HeaderMessage.vue";
import MainMenu from "@/components/layout/header/MainMenu.vue";
import Categories from "@/components/layout/header/Categories.vue";

export default {
  name: "MainHeader",

  props: {
    links: Array,
    categories: Array,
  },

  data() {
    return {
      scrollPosition: null,
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
  }
};
</script>
<style scoped>
header {
  width: 100%;
  position: fixed;
  z-index: 500;
}
</style>
