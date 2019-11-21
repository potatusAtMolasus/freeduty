<template>
  <header>
    <div id="headerContent">
      <div id="mainMenu">
        <div id="logoWrapper">
          <img src="../../assets/logo.png" id="logo" />
        </div>
        <div id="headerLinks">
          <router-link to="/home">Главная</router-link>
          <router-link to="/about">О нас</router-link>
          <router-link to="/stores">Адреса</router-link>
          <router-link to="/offers">Акции</router-link>
          <router-link to="/blog">Блог</router-link>
          <router-link to="/corporate">Корпоративным клиентам</router-link>
        </div>
      </div>



      <div id="categories">
        <router-link to="/category/1">Категория 1</router-link>
        <router-link to="/category/2">Категория 3</router-link>
        <router-link to="/category/3">Категория 2</router-link>
        <router-link to="/category/4">Категория 4</router-link>
      </div>
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
<style scoped>
#headerContent{

}
#mainMenu{
  display: flex;
}
#logoWrapper{
  flex: 1;
}
#headerLinks{
  display: inline;
  flex: 4;
}
#headerLinks a{
  display: inline-block;
}
#categories{

}

</style>