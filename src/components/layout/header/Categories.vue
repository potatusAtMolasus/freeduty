<template>
  <div id="categories" class="wide-container" v-if="scrollPosition<=0&&$route.path=='/home'">
    <router-link v-for="i in categories" :key="i.url" :to="i.url">
        <p>{{i.label}}</p>
    </router-link>
  </div>
</template>

<script>
export default {
  props:{
    scrollPosition: Number,
    categories: Array,
  },
}
</script>
<style scoped>
/* Стили для категорий */
#categories {
  margin-top: 4em;
  display: flex;
  justify-content: space-between;
}
#categories a {
  text-decoration: none;
}
#categories a p {
  color: #ddd;
  transition: color 0.1s;
}
#categories a:hover p {
  color: red;
}
</style>