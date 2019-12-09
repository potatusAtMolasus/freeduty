<template>
  <div id="mobileMenuWrap">
    <div id="mobileMenuToggle" :class="{toggled:show, top: !scrollPosition&&!show}" @click="show=!show">
      <span id="overlay-button">
        <span></span>
      </span>
    </div>
    <transition name="left">    
      <div id="mobileMenu" v-if="show">
        
        <div id="mobileLinks">
          <router-link v-for="i in links" :key="i.url" :to="i.url" >
            <p class="text" @click="show=false"><span>{{i.label}}</span></p>
          </router-link>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  props:{
    links: Array,  
    scrollPosition: Number,
  },
  data() {
    return {
      show: false,
    };
  },
  // watch:{
  //   show(){
  //     // if(this.show){
  //     //   document.querySelector('body').classList.add('modal-open');
  //     // } else {
  //     //   document.querySelector('body').classList.remove('modal-open');
  //     // }
  //   }
  // }
};
</script>

<style scoped>
a{
  color: #000;
}
#mobileMenuToggle {
  position: fixed;
  top: .5em;
  left: .5em;
  display: flex;
  width: 4em;
  height: 4em;
  border-radius: 50%;
  background: #666;
  z-index: 300;
  cursor: pointer;
}
#mobileMenuToggle.top{
  top: 6.5em;
}
#overlay-button {
  z-index: 5;
  cursor: pointer;
  user-select: none;
  margin: auto;
}
#overlay-button span {
  height: 4px;
  width: 2.2em;
  border-radius: 2px;
  background-color: white;
  position: relative;
  display: block;
  transition: all 0.1s ease-in-out;
}
#overlay-button span:before {
  top: -10px;
  visibility: visible;
}
#overlay-button span:after {
  top: 10px;
}
#overlay-button span:before,
#overlay-button span:after {
  height: 4px;
  width: 2.2em;
  border-radius: 2px;
  background-color: white;
  position: absolute;
  content: "";
  transition: all 0.1s ease-in-out;
}
.toggled#mobileMenuToggle {
  box-shadow: #222 2px 2px 15px 5px;
}

.toggled #overlay-button span,
.toggled #overlay-button span:before,
.toggled #overlay-button span:after,
#mobileMenuToggle:hover span,
#mobileMenuToggle:hover span:before,
#mobileMenuToggle:hover span:after {
  background: #333332;
}
.toggled #overlay-button span:before {
  transform: rotate(45deg) translate(7px, 7px);
  opacity: 1;
}
.toggled #overlay-button span:after {
  transform: rotate(-45deg) translate(7px, -7px);
}
#mobileMenuToggle.toggled #overlay-button span,
#mobileMenuToggle.toggled:hover span {
  background: transparent;
}

#mobileMenu{
  position: fixed;
  width: 100vw;
  height: 100vh;
  display: flex;
  background: #333332;
  top: 0;
  left: 0;
}
#mobileLinks {
  margin: auto;
  text-align: center;
}
#mobileLinks a{
  margin: auto;
  text-align: center;
  margin: 2em;
  cursor: pointer;
}
#mobileLinks a span{
  margin: auto;
  width: 0;
  position: relative;
}
#mobileLinks a span:after{
  display: block;
  content: '';
  width: 100%;
  height: 2px;
  position: absolute;
  background: #555;
  bottom: -0.3em;
  left: 0;
}

#mobileLinks a.router-link-active span:after{
  display: block;
  content: '';
  width: 100%;
  height: 2px;
  position: absolute;
  background: red;
  bottom: -0.3em;
  left: 0;
}

.left-enter-active#mobileMenu,
.left-leave-active#mobileMenu{
  transition: left 0.5s;
}
.left-enter#mobileMenu,
.left-leave-to#mobileMenu{
  left: -100vw;
}
</style>
