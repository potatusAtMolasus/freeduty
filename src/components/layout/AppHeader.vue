<template>
  <header>
    <h1>Верхушка</h1>
    <div id="mainMenu">
      <router-link to="/home">Главная</router-link>
      <router-link to="/about">О нас</router-link>
      <router-link to="/stores">Адреса</router-link>
      <router-link to="/offers">Акции</router-link>
      <router-link to="/blog">Блог</router-link>
      <router-link to="/corporate">Корпоративным клиентам</router-link>
    </div>
    <div id="categories">
      <router-link to="/category/1">Категория 1</router-link>
      <router-link to="/category/2">Категория 3</router-link>
      <router-link to="/category/3">Категория 2</router-link>
      <router-link to="/category/4">Категория 4</router-link>
      <search-bar></search-bar>
    </div>
  </header>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";

export default {
  name: "MainHeader",
  components: {
    SearchBar
  }
};
</script>
