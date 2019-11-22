<template>
  <div id="app">
    <div id="page">
      <main-header></main-header>
      <router-view />
    </div>
    <main-footer></main-footer>
    <modal></modal>
  </div>
</template>

<script>
import MainHeader from "./components/layout/AppHeader.vue";
import MainFooter from "./components/layout/AppFooter.vue";
import Modal from "./components/Modal.vue";

export default {
  name: "App",
  components: {
    MainHeader,
    MainFooter,
    Modal
  }
};
</script>
<style>
@import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');
* {
  font-family: 'Roboto', sans-serif;
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

.container, .wide-container {
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
  .wide-container{
    max-width: 540px;
  }
}

@media (min-width: 768px) {
  .container {
    max-width: 720px;
  }
  .wide-container{
    max-width: 840px;
  }
}

@media (min-width: 992px) {
  .container {
    max-width: 960px;
  }
  .wide-container{
    max-width: 1040px;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1140px;
  }
  .wide-container{
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