<template>
  <section id="blogSection">
    <div class="wide-container">
      <div id="postGrid">
        <div class="post-wrap" v-for="post in posts" :key="post.id">
          <!-- <div class="inner-post-wrap">
            <h2 class="title">{{ post.title }}</h2>
          </div> -->
          <router-link class="post-link" :to="'/post/' + post.id">
            <img :src="post.image_url">
            <div class="inner">
              <div class="title-wrap">
                <span v-if="!isMobile">Перейти</span>
                <span v-if="isMobile" class="title">{{ post.title }}</span>
                <i class="fa fa-arrow-right"></i>
              </div>
            </div>
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
      return pic || require('../../assets/image.jpg');

      // try{
      //   return require('../../assets/'+pic);
      // } catch(e) {
      //   return '';
      // }
    },
  },
};
</script>
<style scoped>
.wide-container{
  box-sizing: border-box;
}
#blogSection{
  background-image: url('../../assets/patternBlack.png');
  background-color: rgba(180, 180, 180, 0.9);
}

#postGrid {
  padding: 0;
  height: 70vh;
  margin: 0;
  display: grid;
  grid-gap: 0;
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
  background: #CCCCCC99;
  /* border: 2px solid #999; */
  color:#333;
  padding: .6em;
  width: 100%;
  height: 100%;
  display: flex;
  opacity: 0;
  transition: all 0.2s;
}
.inner .title-wrap{
  margin: auto;
}
.post-link img {
  position: absolute;
  margin: auto;
  z-index: 200;
  width: 100%;
  height: 100%;
  transform: scale(1);
  transition: all 0.2s;
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
.fa-arrow-right{
  padding-left: .2em;
}
/* .post-wrap:hover .inner-post-wrap {
  transform: scale(0);
}
.post-wrap:hover .post-link {
  transform: scale(1);
} */
.post-wrap:hover img{
  transform: scale(1.2);
}
.post-wrap:hover .inner {
  opacity: 1;
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
  padding: 5em 0;
  overflow: auto;
}
@media(max-width: 800px){
  #blogSection .wide-container{
    max-width: unset;
  }
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

  #postGrid{
    height: auto;
    padding: 2em 0.2em;
    margin: 0;
    grid-gap: 0.6em;
  }
  #blogSection{
    padding-top: 0em;
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
  .post-wrap{
    padding: 8rem;
  }
  .post-wrap .inner-post-wrap {
    transform: scale(0);
  }
  .post-wrap .post-link {
    transform: scale(1);
  }
  .inner{
    display: none;
  }
}
</style>
