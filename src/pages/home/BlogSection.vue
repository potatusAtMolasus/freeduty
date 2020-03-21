<template>
  <section id="blogSection">
    <div class="wide-container">
      <div class="title-section">
        <div class="title-wrap">
          <h2 class="title">Блог</h2>
          <span class="line"></span>
        </div>
      </div>

      <div id="postGrid">
        <div class="col">
          <div v-if="posts[0]" class="post-wrap">
            <router-link class="post-link" :to="'/post/' + posts[0].id">
              <img :src="posts[0].image_url" />
              <div class="inner">
                <div class="title-wrap">
                  <span v-if="!isMobile">
                    {{ posts[0].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[0].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                </div>
              </div>
            </router-link>
          </div>

          <div v-if="posts[1]" class="post-wrap">
            <router-link class="post-link" :to="'/post/' + posts[1].id">
              <img :src="posts[1].image_url" />
              <div class="inner">
                <div class="title-wrap">
                  <span v-if="!isMobile">
                    {{ posts[1].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[1].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                </div>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col">
          <div v-if="posts[2]" class="post-wrap">
            <router-link class="post-link" :to="'/post/' + posts[2].id">
              <img :src="posts[2].image_url" />
              <div class="inner">
                <div class="title-wrap">
                  <span v-if="!isMobile">
                    {{ posts[2].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[2].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                </div>
              </div>
            </router-link>
          </div>

          <div v-if="posts[3]" class="post-wrap">
            <router-link class="post-link" :to="'/post/' + posts[3].id">
              <img :src="posts[3].image_url" />
              <div class="inner">
                <div class="title-wrap">
                  <span v-if="!isMobile">
                    {{ posts[3].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[3].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                </div>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col">
          <div v-if="posts[4]" class="post-wrap">
            <router-link class="post-link" :to="'/post/' + posts[4].id">
              <img :src="posts[4].image_url" />
              <div class="inner">
                <div class="title-wrap">
                  <span v-if="!isMobile">
                    {{ posts[4].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[4].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                </div>
              </div>
            </router-link>
          </div>

          <div v-if="posts[5]" class="post-wrap">
            <router-link class="post-link" :to="'/post/' + posts[5].id">
              <img :src="posts[5].image_url" />
              <div class="inner">
                <div class="title-wrap">
                   <span v-if="!isMobile">
                    {{ posts[5].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[5].caption.slice(0, 30) + '...' }}
                    <i class="fa fa-arrow-right"></i>
                  </span>
                </div>
              </div>
            </router-link>
          </div>
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
  methods: {
    getImgUrl(pic) {
      return pic || require("../../assets/image.jpg");

      // try{
      //   return require('../../assets/'+pic);
      // } catch(e) {
      //   return '';
      // }
    }
  }
};
</script>
<style scoped>
.wide-container {
  box-sizing: border-box;
}
#blogSection {
  background-image: url("../../assets/patternBlack.png");
  background-size: 300px;
  background-color: rgba(180, 180, 180, 0.9);
}

#postGrid {
  padding: 0;
  /* height: 70vh; */
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
  /* background: #ccc; */
  background: #f005;
  position: relative;
  padding: 0.1em;
  cursor: pointer;
}
.post-link {
  width: 100%;
  /* height: 100%; */
  /* position: absolute; */
  /* top: 0; */
  /* left: 0; */
  background: #333;
  /* opacity: 0.8; */
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
  background: #cccccc00;
  /* border: 2px solid #999; */
  color: #333;
  /* padding: 0.6em; */
  width: 100%;
  height: 100%;
  display: flex;
  /* opacity: 0; */
  transition: all 0.2s;
  position: absolute;
}
.inner .title-wrap {
  position: relative;
  margin: auto;
  transition: all 0.2s;
  top: 100%;
}
.post-link img {
  /* position: absolute; */
  margin: auto;
  z-index: 200;
  width: 100%;
  /* height: 100%; */
  transform: scale(1.02);
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
.fa-arrow-right {
  padding-left: 0.2em;
}
/* .post-wrap:hover .inner-post-wrap {
  transform: scale(0);
}
.post-wrap:hover .post-link {
  transform: scale(1);
} */
.post-wrap:hover img {
  transform: scale(1.2);
}
.post-wrap:hover .inner {
  background: #cccccc99;
}

.post-wrap:hover .inner .title-wrap {
  top: 0;
}
.inner-post-wrap .title {
  margin: auto;
}
/* 
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
} */
.title-section {
  width: 100%;
  display: flex;
  overflow: hidden;
  position: relative;
}
.title-section .title-wrap {
  background: black;
  direction: inline-block;
  padding: 0.25em 18em 0.25em 6em;
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
  width: 6em;
  position: absolute;
  right: 0;
  top: 0;
  display: block;
  clip-path: polygon(70% 0, 100% 0, 100% 100%, 0 100%);
}

.inner .title-wrap span {
  width: 50%;
  display: block;
  margin: auto;
  background: #333c;
  padding: 1em;
  color: #ccc;
}

#blogSection {
  padding: 5em 0;
  overflow: auto;
}
#postGrid {
  display: flex;
  justify-content: center;
}
.col {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
@media (max-width: 800px) {
  .post-wrap{
    padding: 0.5em;
    background: transparent;
  }
  .post-link {
    padding: 0;
    margin: 0;
    float: none;
    display: inline-block !important;
  }
  #postGrid .col:nth-child(3) {
    display: none;
  }

  #blogSection .wide-container {
    max-width: unset;
  }
  #blogSection {
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
@media (max-width: 500px) {
  #postGrid {
    flex-direction: column;
  }
  #postGrid {
    height: auto;
    padding: 2em 0.2em;
    margin: 0;
    grid-gap: 0.6em;
  }
  #blogSection {
    padding-top: 0em;
  }
  .wide-container {
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
  .post-wrap {
    /* padding: 8rem; */
  }
  .post-wrap .inner-post-wrap {
    transform: scale(0);
  }
  .post-wrap .post-link {
    transform: scale(1);
  }
  .inner {
    display: none;
  }
}
</style>
