<template>
  <main id="blogPage">
    <div class="container">

      <div class="title-section">
        <div class="title-wrap">
          <h2 class="title">Блог</h2>
          <span class="line"></span>
        </div>
      </div>
      
      <div id="postsWrap">
        <div class="post-wrap" v-for="post in posts" :key="post.id">
          <router-link class="post-link" :to="'/post/' + post.id">
            <img :src="getImgUrl(post.image_url)">
            <div class="inner">
              <div class="title-wrap">
                <span v-if="!isMobile">Перейти</span>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  props:{
    posts: Array,
    scrollPosition: Number,
    isMobile: Boolean,
  },
  methods:{
    getImgUrl(pic) {
      return pic || require('../assets/image.jpg');

      // try{
      //   return require('../assets/'+pic);
      // } catch(e) {
      //   return '';
      // }
    },
  },
};
</script>

<style scoped>
main{
  background-image: url('../assets/patternWhite.png');
  background-size: 300px;
  background-color: #ccc;
}
.container{
  max-width: 960px;
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  background-color: #999;
  padding: 3em 0em;
}
#blogPage.padded-top .container{
  padding-top: 15em;
}
#postsWrap{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 1em;
}
.title-section {
  width: 100%;
  display: flex;
  overflow: hidden;
  position: relative;
}
.title-section .title-wrap {
  background: black;
  direction: inline-block;
  padding: 0.25em 9em 0.25em 6em;
  clip-path: polygon(0 0, 100% 0, 85% 100%, 0 100%);
  position: relative;
  left: -1em;
  display: flex;
}
.title {
  color: #ccc;
}
.line {
  background: red;
  height: 100%;
  width: 4em;
  position: absolute;
  right: 0;
  top: 0;
  display: block;
  -webkit-clip-path: polygon(70% 0, 100% 0, 100% 100%, 0 100%);
  clip-path: polygon(70% 0, 100% 0, 100% 100%, 0 100%);
}

.post-wrap {
  flex: 1 0 350px;
  height: 350px;
  background: #ccc;
  position: relative;
  box-sizing: border-box;
  cursor: pointer;
  padding: 0.7em;
  margin: .45em;
  box-shadow: #888 2px 2px 10px 5px;
}
.post-link img {
  position: absolute;
  margin: auto;
  z-index: 200;
  width: 100%;
  height: 100%;
}

.post-wrap:hover .post-link {
  transform: scale(1);
}
.inner-post-wrap .title {
  margin: auto;
}

.post-link {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: #333;
  opacity: 0.8;
  transform: scale(1);
  z-index: 100;
  display: flex;
  transition: all 0.4s ease-in-out;
  color: white;
  overflow: hidden;
}
.inner {
  text-decoration: none;
  text-transform: uppercase;
  z-index: 300;
  background: #CCCCCC00;
  /* border: 2px solid #999; */
  color:#333;
  padding: .6em;
  width: 100%;
  height: 100%;
  display: flex;
  /* opacity: 0; */
  transition: all 0.2s;
}
.inner .title-wrap{
  transition: all 0.2s;
  position: relative;
  top: 100%;
  margin: auto;
}
.post-link p i {
  position: relative;
  right: -0.3em;
  transition: right 0.2s;
}
.post-link p:hover i {
  right: -0.6em;
}
.post-wrap img{
  transition: all .2s linear;
}

.post-wrap:hover img{
  transform: scale(1.2);
}
.post-wrap:hover .inner {
  background: #CCCCCC99;

  /* opacity: 1; */
}
.post-wrap:hover .inner .title-wrap{
  top: 0;
}
@media(max-width: 776px){
  #postsWrap{
    flex-direction: column;
  }
  #blogPage.padded-top .container {
    padding-top: 3em;
  }
  .inner{
    box-sizing: border-box;
  }
  .post-wrap{
    box-sizing: border-box;
  }
}
@media(max-width: 500px){
  .container{
    padding: 3em 0em;
  }
}
</style>
