<template>
  <header>
    <h1>Верхушка</h1>
    <div id="mainMenu">
      <router-link to="/home">Главная</router-link>
      <router-link to="/about">Duty Free</router-link>
      <router-link to="/stores">Адреса Магазинов</router-link>
      <router-link to="/offers">Акции</router-link>
      <router-link to="/blog">Блог</router-link>
      <router-link to="/corporate">Корпоративным клиентам</router-link>
    </div>
    <div id="categories">
      <router-link to="/category/visky">Виски</router-link>
      <router-link to="/category/vine">Вино</router-link>
      <router-link to="/category/beer">Пиво</router-link>
      <router-link to="/category/konjack">Коньяк</router-link>
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
