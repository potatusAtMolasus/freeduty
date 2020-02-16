<template>
  <div id="app">
    <div id="page">
      <main-header
        v-if="$route.name!=='landing'"
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
        :homeOffers="homeOffers"
        :popular="popular"
        :posts="posts"
        :foundData="foundData"
        :width="width"
        @filtersChanged="setFilters"
        @find="search"
        @pageSelected="getNewPage"
      />
    </div>
    <main-footer v-if="$route.name!=='landing'" :links="links" :categories="categories"></main-footer>
    <modal></modal>
    <loader :show="!loaded"></loader>
  </div>
</template>

<script>
import MainHeader from "./components/layout/AppHeader.vue";
import MainFooter from "./components/layout/AppFooter.vue";
import Modal from "./components/Modal.vue";
import Loader from "./components/Loader.vue";
import axios from "@/js/AxiosInstance.js";
import axiosNoLoad from "axios";

export default {
  name: "App",
  data() {
    return {
      links: [
        {
          url: "/home",
          label: "Главная"
        }, {
          url: "/search/all",
          label: "Каталог"
        }, {
          url: "/offers",
          label: "Акции"
        }, {
          url: "/about",
          label: "О нас"
        }, {
          url: "/contacts",
          label: "Контакты"
        }, {
          url: "/blog",
          label: "Блог"
        }
      ],
      scrollPosition: null,
      width: 0,
      categories: [],
      offers: [],
      homeOffers: [],
      popular: [],
      posts: [],

      foundData: [],
      activeFilters: { category: "" },
      currentPage: 1,
      loaded: false,
    };
  },
  async mounted() {
    window.addEventListener('resize', this.updateWidth);
    this.updateWidth();

    axios.interceptors.request.use(config => {
      this.loaded = false;
      return config;
    });

    axios.interceptors.response.use(response => {
      this.loaded = true;
      return response;
    });

    this.$router.beforeResolve((to, from, next) => {
      this.loaded = false;
      next();
    });

    this.$router.afterEach(() => {
      this.loaded = true;
    });

    window.addEventListener("scroll", this.updateScroll);

    this.categories = (await axios.post("get-categories")).data;
    this.offers = (await axios.post("all-offers")).data;
    this.homeOffers = (await axios.post("get-offers")).data;
    this.popular = (await axios.post("get-popular")).data;
    this.posts = (await axios.post("get-posts")).data;
    this.foundData = (await axios.post("find", {
      query: this.activeQuery,
      ...this.activeFilters
    })).data;
  },
  methods: {
    async search(query) {
      this.activeQuery = query;
      this.foundData = (await axiosNoLoad.post("http://127.0.0.1:5000/find", {
        query,
        ...this.activeFilters,
        page: this.currentPage,
      })).data;
    },
    updateScroll() {
      this.scrollPosition = window.scrollY;
    },
    updateWidth() {
      this.width = window.innerWidth;
    },
    async setFilters(newFilters) {
      this.activeFilters = newFilters;
      this.foundData = (await axiosNoLoad.post("http://127.0.0.1:5000/find", {
        query: this.activeQuery,
        ...this.activeFilters,
        page: this.currentPage
      })).data;
      // this.router.push({ path: 'search' })
    },
    async getNewPage(newPage){
      this.currentPage = newPage;
      this.foundData = (await axiosNoLoad.post("http://127.0.0.1:5000/find", {
        query: this.activeQuery,
        ...this.activeFilters,
        page: this.currentPage,
      })).data;
    },
  },
  computed: {
    isMobile() {
      if (
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        )
        || 
        this.width < 900
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
    Modal,
    Loader
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