<template>
  <main>
    <div class="container">
      <h2 blog-title>Блог</h2>
      <div id="postsWrap">
        <div class="post-wrap" v-for="post in posts" :key="post.id">
          <div class="inner-post-wrap">
            <h2 class="title">{{ post.title }}</h2>
          </div>
          <router-link class="post-link" :to="'/post/' + post.id">
            <img :src="getImgUrl(post.image)">
            <p>
              Перейти
              <i class="fa fa-arrow-right"></i>
            </p>
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
  },
  methods:{
    getImgUrl(pic) {
      try{
        return require('../assets/'+pic);
      } catch(e) {
        return '';
      }
    },
  },
};
</script>

<style scoped>
main{
  background-image: url('../assets/patternWhite.png');
  background-color: #ccc;
}
.container{
  background-color: #999;
  padding: 3em 1em;
}
#postsWrap{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
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
.inner-post-wrap {
  background: #ccc;
  border: 2px solid red;
  width: 100%;
  height: 100%;
  display: flex;
  transition: all 0.4s ease-in-out;
  transform: scale(1);
  box-sizing: border-box;
  z-index: 300;
  top: 0;
  left: 0;
}
.post-wrap:hover .inner-post-wrap {
  transform: scale(0);
}
.post-wrap:hover .post-link {
  transform: scale(1);
}
.inner-post-wrap .title {
  margin: auto;
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
  transform: scale(0);
  z-index: 100;
  display: flex;
  transition: all 0.4s ease-in-out;
  color: white;
}
.post-link p {
  margin: auto;
  text-decoration: none;
  text-transform: uppercase;
}
.post-link p i {
  position: relative;
  right: -0.3em;
  transition: right 0.2s;
}
.post-link p:hover i {
  right: -0.6em;
}
</style>
