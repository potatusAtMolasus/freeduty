<template>
  <div id="app">
    <div id="page">
      <main-header
        :scrollPosition="scrollPosition"
        :isMobile="isMobile"
        :links="links"
        :categories="categories"
        @search="search"
      ></main-header>
      <router-view
        :scrollPosition="scrollPosition"
        :isMobile="isMobile"
        :offers="offers"
        :popular="popular"
        :posts="posts"
        :foundData="foundData"
        @filtersChanged="setFilters"
      />
    </div>
    <main-footer :links="links" :categories="categories"></main-footer>
    <modal></modal>
  </div>
</template>

<script>
import MainHeader from "./components/layout/AppHeader.vue";
import MainFooter from "./components/layout/AppFooter.vue";
import Modal from "./components/Modal.vue";
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      links: [
        {
          url: "/home",
          label: "Главная"
        },
        {
          url: "/about",
          label: "О нас"
        },
        {
          url: "/contacts",
          label: "Контакты"
        },
        {
          url: "/offers",
          label: "Акции"
        },
        {
          url: "/blog",
          label: "Блог"
        }
      ],
      scrollPosition: null,
      categories: [],
      offers: [],
      popular: [],
      posts: [],

      foundData: [],
      activeFilters: { category: '' },
    };
  },
  async mounted() {
    window.addEventListener("scroll", this.updateScroll);

    this.categories = (await axios.post(
      "http://localhost:5000/get-categories"
    )).data;
    this.offers = (await axios.post("http://localhost:5000/get-offers")).data;
    this.popular = (await axios.post("http://localhost:5000/get-popular")).data;
    this.posts = (await axios.post("http://localhost:5000/get-posts")).data;
    this.foundData = (await axios.post("http://localhost:5000/find", { query: this.activeQuery, ...this.activeFilters })).data;
  },
  methods: {
    async search(query) {
      this.activeQuery = query;
      this.foundData = (await axios.post("http://localhost:5000/find", { query, ...this.activeFilters })).data;
      this.$router.push({ path: '/search/0/' });
    },
    updateScroll() {
      this.scrollPosition = window.scrollY;
    },
    async setFilters(newFilters){
      this.activeFilters = newFilters;
      this.foundData = (await axios.post("http://localhost:5000/find", { query: this.activeQuery, ...this.activeFilters })).data;
      // this.router.push({ path: 'search' })
    }
  },
  computed: {
    isMobile() {
      if (
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        )
      ) {
        return true;
      } else {
        // return true
        return false;
      }
    }
  },
  components: {
    MainHeader,
    MainFooter,
    Modal
  }
};
</script>
<style>
@import url("https://fonts.googleapis.com/css?family=Roboto&display=swap");
* {
  font-family: "Roboto", sans-serif;
}
/* body.modal-open {
  overflow: hidden;
  height: 100px;
} */
body,
html {
  padding: 0;
  margin: 0;
  min-height: 100vh;
  overflow-x: hidden;
}
#app {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: space-between;
}

.container,
.wide-container {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}
ul {
  list-style: none;
}
a {
  text-decoration: none;
}
@media (min-width: 576px) {
  .container {
    max-width: 540px;
  }
  .wide-container {
    max-width: 540px;
  }
}

@media (min-width: 768px) {
  .container {
    max-width: 720px;
  }
  .wide-container {
    max-width: 840px;
  }
}

@media (min-width: 992px) {
  .container {
    max-width: 960px;
  }
  .wide-container {
    max-width: 1040px;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1140px;
  }
  .wide-container {
    max-width: 1300px;
  }
}

.container-fluid {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}
</style>