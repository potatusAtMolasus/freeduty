<template>
  <section id="blogSection">
    <div class="wide-container">
      <div id="postGrid">
        <div class="post-wrap" v-for="post in posts" :key="post.id">
          <div class="inner-post-wrap">
            <h2 class="title">{{ post.title }}</h2>
          </div>
          <router-link class="post-link" :to="'/post/' + post.id">
            <img :src="getImgUrl(post.images[0])">
            <p>
              Перейти
              <i class="fa fa-arrow-right"></i>
            </p>
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "BlogSection",
  props: {
    isMobile: Boolean,
    posts: Array
  },
  methods:{
    getImgUrl(pic) {
      try{
        return require('../../assets/'+pic);
      } catch(e) {
        return '';
      }
    },
  },
};
</script>
<style scoped>

#blogSection{
  background-image: url('../../assets/patternWhite.png');
  background-color: #333;
}
#postGrid {
  padding: 30px;
  height: 60vh;
  margin: 20px auto;
  display: grid;
  grid-gap: 0.8em;
  grid-template-areas:
    "firstPost firstPost secondPost fourthPost"
    "firstPost firstPost secondPost fifthPost"
    "firstPost firstPost thridPost thridPost";
  background: transparent;

}
.post-wrap {
  background: #ccc;
  position: relative;
  padding: 0.7em;
  cursor: pointer;
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
  z-index: 300;
  background: #CCCCCC99;
  box-shadow: #CCCCCC99 2px 2px 5px 15px;
  color: #333;
  border-radius: 10px;
  padding: .3em;
}
.post-link img {
  position: absolute;
  margin: auto;
  z-index: 200;
  width: 100%;
  height: 100%;
}
.post-link p i {
  position: relative;
  right: -0.3em;
  transition: right 0.2s;
}
.post-link p:hover i {
  right: -0.6em;
}
.inner-post-wrap {
  background: #ccc;
  border: 2px solid red;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  display: flex;
  transition: all 0.4s ease-in-out;
  transform: scale(1);
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

#postGrid .post-wrap:nth-child(1) {
  grid-area: firstPost;
}
#postGrid .post-wrap:nth-child(2) {
  grid-area: secondPost;
}
#postGrid .post-wrap:nth-child(3) {
  grid-area: thridPost;
}
#postGrid .post-wrap:nth-child(4) {
  grid-area: fourthPost;
}
#postGrid .post-wrap:nth-child(5) {
  grid-area: fifthPost;
}
#blogSection{
  padding-top: 5em;
  overflow: auto;
}
@media(max-width: 800px){
  #blogSection{
    padding-top: 4em;
  }
  #postGrid .post-wrap:nth-child(4),
  #postGrid .post-wrap:nth-child(5) {
    display: none;  
  }
  #postGrid {
    grid-template-areas:
      "firstPost firstPost"
      "secondPost thridPost";
  }
}
@media(max-width: 500px){
  #blogSection{
    padding-top: 3em;
  }
  .wide-container{
    padding: 0;
  }
  #postGrid .post-wrap:nth-child(4),
  #postGrid .post-wrap:nth-child(5) {
    display: none;  
  }
  #postGrid {
    grid-template-areas:
      "firstPost"
      "secondPost"
      "thridPost";
  }
}
</style>
