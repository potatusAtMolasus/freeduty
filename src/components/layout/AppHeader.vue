<template>
  <header>
    <div id="HeaderMessage" :class="{'no-height': scrollPosition>0}">
      <p>Tommodi repellat. Voluptatum corporis consequuntur, fugiat quae libero, assumend porro ab</p>
      <p>A labore explicabo aliquam mollitia similique 8:12 safa 12:23 quasi debitis rem quod nobis. Consequuntur, quisquam.</p>
      <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad facilis voluptates deserunt voluptate</p>
    </div>

    <div id="headerContent">
      <div id="mainMenu">
        <div id="logoWrapper">
          <img src="../../assets/logo.png" id="logo" />
        </div>

        <div id="headerLinks" class="buttons">
          <router-link class="btn btn1" to="/home">
            <span class="circle"></span>
            <p class="text">Главная</p>
          </router-link>

          <router-link class="btn btn1" to="/about">
            <span class="circle"></span>
            <p class="text">О нас</p>
          </router-link>

          <router-link class="btn btn1" to="/stores">
            <span class="circle"></span>
            <p class="text">Адреса</p>
          </router-link>

          <router-link class="btn btn1" to="/offers">
            <span class="circle"></span>
            <p class="text">Акции</p>
          </router-link>

          <router-link class="btn btn1" to="/blog">
            <span class="circle"></span>
            <p class="text">Блог</p>
          </router-link>

          <router-link class="btn btn1" to="/corporate">
            <span class="circle"></span>
            <p class="text">Корпоративным клиентам</p>
          </router-link>
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

  data() {
    return {
      scrollPosition: null
    };
  },

  methods: {
    updateScroll() {
      this.scrollPosition = window.scrollY;
      console.log(window.scrollY);
    }
  },

  mounted() {
    window.addEventListener("scroll", this.updateScroll);
  },

  components: {
    SearchBar
  }
};
</script>
<style scoped>
header {
  width: 100%;
  position: fixed;
  z-index: 500;
}
#HeaderMessage {
  box-sizing: border-box;
  overflow: hidden;
  padding: 1.1em;
  background: black;
  transition: all 0.2s;
  height: 6em;
}
#HeaderMessage.no-height {
  height: 0;
  margin: 0;
  padding: 0;
}
#HeaderMessage p {
  line-height: 1.5em;
  font-size: 0.9em;
  text-align: center;
  margin: 0;
  color: white;
}

/* #headerContent{} */

#mainMenu {
  display: flex;
}
#logoWrapper {
  flex: 1;
}
/* #logoWrapper img{
  width: 100%;
} */

#headerLinks {
  display: flex;
  justify-content: left;
  flex: 4;
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
/* #headerLinks a:not(:first-child) {
  border-left: 1px solid #ddd;
} */
#headerLinks a p {
  margin: auto;
  text-align: center;
}
#headerLinks a:hover {
  position: relative;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1), 0 2px 3px rgba(0, 0, 0, 0.2);
}
#headerLinks a:hover:before {
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
}

/* #categories{} */
</style>
<style scoped>
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
  height: .5rem;
  width: .5rem;
  border-radius: 100%;
  position: absolute;
  bottom: .5rem;
  z-index: -1;
  transition: 0.25s;
}
.buttons .btn1 .text {
  position: relative;
  left: 0;
  transition: 0.5s;
}
.buttons .btn1:hover {
  color: white;
}
.buttons .btn1:hover .circle {
  transform: scale(50);
}

</style>
