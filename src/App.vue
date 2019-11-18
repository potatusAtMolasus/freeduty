<template>
  <div id="app">
    <main-header></main-header>
    <router-view />
    <main-footer></main-footer>
  </div>
</template>

<script>
import MainHeader from './components/layout/AppHeader.vue'
import MainFooter from './components/layout/AppFooter.vue'

export default {
  name: 'App',
  components: {
    MainHeader,
    MainFooter
  }
};
</script>
