<template>
  <div id="mainMenu" :class="{ 'main-not-top': scrollPosition||$route.path!='/home' }">
    <router-link to="/home">
      <div id="logoWrapper">
        <img src="../../../assets/logo.png" id="logo" />
      </div>
    </router-link>
    <div id="headerLinks" class="buttons">
      <router-link v-for="i in links" :key="i.url" class="btn btn1" :to="i.url">
        <span class="circle"></span>
        <p class="text">{{i.label}}</p>
      </router-link>
    </div>
    <search-bar @search="search"></search-bar>
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";

export default {
  props: {
    links: Array,
    categories: Array,
    scrollPosition: Number
  },
  data() {
    return {
      showCategories: false
    };
  },
  methods: {
    search(query) {
      this.$emit("search", query);
    }
  },
  components: {
    SearchBar
  }
};
</script>
<style scoped>
#mainMenu {
  display: flex;
  justify-content: center;
  background: rgba(0,0,0,0.9);
  width: auto;
  padding-left: 10%;
}
#mainMenu #logoWrapper{
  padding: .6em .5em;
}
/* .main-not-top#mainMenu{ */
/*  */
/* } */
.padding#mainMenu #logoWrapper{
  padding: .15em;
}

#logoWrapper {
  flex: 1;
}

#logoWrapper img {
  height: 70px;
}

#logo {
  max-width: 180px;
}

#headerLinks {
  display: flex;
  justify-content: left;
  /* flex: 4; */
}
#headerLinks a {
  display: inline-flex;
  line-height: 100%;
  height: 50%;
  width: 13%;
  word-wrap: break-word;
  text-decoration: none;
  color: #ddd;
  background: transparent;
  transition: all 0.2s;
}
/* Стили для глянцевого эффекта */
#headerLinks a p {
  margin: auto;
  text-align: center;
}
#headerLinks a:hover,
#headerLinks a.router-link-active {
  position: relative;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1), 0 2px 3px rgba(0, 0, 0, 0.2);
}
#headerLinks a:hover:before,
#headerLinks a.router-link-active:before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: linear-gradient(
      180deg,
      rgba(255, 255, 255, 0.15),
      rgba(0, 0, 0, 0.25)
    ),
    linear-gradient(
      to left top,
      rgba(255, 255, 255, 0.397),
      rgba(255, 255, 255, 0.1) 50%,
      rgba(255, 255, 255, 0.226) 50%,
      rgba(255, 255, 255, 0)
    );
  z-index: 250;
}

/* Стили для анимации кружка */
.buttons {
  display: flex;
  align-items: center;
  justify-content: center;
}
.buttons .btn {
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Raleway", sans-serif;
  font-weight: 300;
  padding: 1rem 2rem;
  margin: 0 1rem;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.buttons .btn1 {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 2rem 1rem 2rem;
}
.buttons .btn1 .circle {
  background-color: red;
  height: 0.5rem;
  width: 0.5rem;
  border-radius: 100%;
  position: absolute;
  bottom: 0.5rem;
  z-index: -1;
  transition: 0.25s;
  z-index: 200;
}
.buttons .btn1 .text {
  position: relative;
  left: 0;
  transition: 0.5s;
  z-index: 300;
}
.buttons .btn1:hover,
#headerLinks .btn1.router-link-active {
  color: white;
}
.buttons .btn1:hover .circle,
#headerLinks a.router-link-active .circle {
  transform: scale(50);
}

/* Стили для категорий */
#dropdown {
  position: relative;
  display: block;
  overflow: visible;
}
#dropdown i {
  position: relative;
  color: red;
  top: 0;
  left: -0.2em;
  transition: all 0.2s;
}
#categoriesUl {
  position: absolute;
  top: 100%;
  display: flex;
  flex-direction: column;
  width: 100%;
  margin: auto;
  padding-left: 0;
}
#categoriesUl .btn {
  width: 100%;
}
#categoriesUl a.btn {
  box-sizing: border-box;
  background: #454545cc;
}
i.rotate {
  transform: rotate(180deg);
}
#dropdown p {
  margin-left: 5px;
}
#dropdown:hover i {
  top: 0.2em;
}

@media (max-width: 1500px) {
  #headerLinks .btn1{
    margin: 0;
  }
}
@media (max-width: 1200px) {
  #headerLinks .btn1{
    padding: 0.5em;
  }
}

</style>