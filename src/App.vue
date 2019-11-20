<template>
  <div id="app">
    <main-header></main-header>
    <router-view />
    <main-footer></main-footer>
    <modal></modal>
  </div>
</template>

<script>
import MainHeader from './components/layout/AppHeader.vue'
import MainFooter from './components/layout/AppFooter.vue'
import Modal from './components/Modal.vue'

export default {
  name: 'App',
  components: {
    MainHeader,
    MainFooter,
    Modal
  }
};
</script>
<style>
body, html{
  padding: 0;
  margin: 0;
}
</style>