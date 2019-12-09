<template>
  <div id="app">
    <div id="page">
      <main-header :isMobile="isMobile" :links="links" :categories="categories" @search="search"></main-header>
      <router-view :isMobile="isMobile" :offers="offers" :popular="popular" :posts="posts" />
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
          url: "/offers",
          label: "Акции"
        },
        {
          url: "/blog",
          label: "Блог"
        }
      ],
      categories: [],
      offers: [],
      popular: [],
      posts: [],
    };
  },
  async mounted() {
    this.categories = (await axios.post("http://localhost:5000/get-categories")).data;
    this.offers = (await axios.post("http://localhost:5000/get-offers")).data;
    this.popular = (await axios.post("http://localhost:5000/get-popular")).data;
    this.posts = (await axios.post("http://localhost:5000/get-posts")).data;
  },
  methods: {
    async search(query) {
      await axios.post("http://localhost:5000/find", { query });
      console.log(query);
    },
  },
  computed:{
    isMobile() {
      if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        return true
      } else {
        return true
        // return false
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