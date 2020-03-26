<template>
  <div id="app">
    <div id="page">
      <main-header
        v-if="$route.matched[0].path!=='/landing'"
        :scrollPosition="scrollPosition"
        :isMobile="isMobile"
        :links="links"
        :categories="categories"
        @search="search"
      ></main-header>
      <router-view
        :scrollPosition="scrollPosition"
        :isMobile="isMobile"
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
    <main-footer v-if="$route.matched[0].path!=='/landing'" :links="links" :categories="categories"></main-footer>
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
        },
        {
          url: "/search/all",
          label: "Каталог"
        },
        {
          url: "/offers",
          label: "Акции"
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
          url: "/blog",
          label: "Блог"
        }
      ],
      scrollPosition: null,
      width: 0,
      categories: [],
      offers: {},
      homeOffers: [],
      popular: [],
      posts: [],

      foundData: {},
      activeFilters: { category: "" },
      currentPage: 1,
      loaded: false
    };
  },
  async mounted() {
    window.addEventListener("resize", this.updateWidth);
    this.updateWidth();

    axios.interceptors.request.use(config => {
      this.loaded = false;
      return config;
    });

    axios.interceptors.response.use(response => {
      this.loaded = true;
      return response;
    });

    window.addEventListener("scroll", this.updateScroll);

    this.categories = (await axios.post("get-categories")).data;
    this.homeOffers = (await axios.post("get-offers")).data;
    this.popular = (await axios.post("get-popular")).data;
    this.posts = (await axios.post("get-posts")).data.data;
  },
  methods: {
    async search(query, load = false) {
      this.activeQuery = query;
      if (load) {
        this.foundData = (
          await axios.post("find", {
            query,
            ...this.activeFilters,
            page: this.currentPage
          })
        ).data;
      } else {
        this.foundData = (
          await axiosNoLoad.post("https://dutyfreesochi.ru//find", {
            query,
            ...this.activeFilters,
            page: this.currentPage
          }, {
            withCredentials: true,
            credentials: 'same-origin',
            crossdomain: true,
            headers: {
              'Content-Type': 'application/json',
            }
          })
        ).data;
      }
    },
    updateScroll() {
      this.scrollPosition = window.scrollY;
    },
    updateWidth() {
      this.width = window.innerWidth;
    },
    async setFilters(newFilters) {
      this.activeFilters = newFilters;
      this.foundData = (
        await axiosNoLoad.post("https://dutyfreesochi.ru//find", {
          query: this.activeQuery,
          ...newFilters,
          page: this.currentPage
        }, {
          withCredentials: true,
          credentials: 'same-origin',
          crossdomain: true,
          headers: {
            'Content-Type': 'application/json',
          }
        })
      ).data;
    },
    async getNewPage(newPage) {
      this.currentPage = newPage;
      this.foundData = (
        await axios.post("find", {
          query: this.activeQuery,
          ...this.activeFilters,
          page: this.currentPage
        }, {
          withCredentials: true,
          credentials: 'same-origin',
          crossdomain: true,
          headers: {
            'Content-Type': 'application/json',
          }
        })
      ).data;
    }
  },
  computed: {
    isMobile() {
      if (
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        ) ||
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

ul {
  list-style: none;
}

a {
  text-decoration: none;
}
</style>
