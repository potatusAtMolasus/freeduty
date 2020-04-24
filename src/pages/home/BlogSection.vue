<template>
  <section id="blogSection">
    <div id="blogTitleWrap">
      НОВОСТИ
    </div>
    <div class="wide-container">
      <div id="postGrid">
        <div class="col">
          <div v-if="posts[0]" class="post-wrap">
            <router-link class="post-link" :to="'/post/' + posts[0].id">
              <img :src="posts[0].image_url" />
              <div class="inner">
                <div class="title-wrap">
                  <span v-if="!isMobile">
                    {{ posts[0].caption.slice(0, 80) + '...'  }}
                    
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[0].caption.slice(0, 80) + '...' }}
                    
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
                    {{ posts[1].caption.slice(0, 80) + '...' }}
                    
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[1].caption.slice(0, 80) + '...' }}
                    
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
                    {{ posts[2].caption.slice(0, 80) + '...' }}
                    
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[2].caption.slice(0, 80) + '...' }}
                    
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
                    {{ posts[3].caption.slice(0, 80) + '...' }}
                    
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[3].caption.slice(0, 80) + '...' }}
                    
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
                    {{ posts[4].caption.slice(0, 80) + '...' }}
                    
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[4].caption.slice(0, 80) + '...' }}
                    
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
                    {{ posts[5].caption.slice(0, 80) + '...' }}
                    
                  </span>
                  <span v-if="isMobile" class="title">
                    {{ posts[5].caption.slice(0, 80) + '...' }}
                    
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
  #blogTitleWrap {
    top: -53px;
    z-index: 800;
    width: 100%;
    position: absolute;
    justify-content: center;
    color: #ffffff;
    text-align: center;
    font-size: 1.75rem;
    font-weight: normal;
    text-transform: uppercase;
    font-family: roboto, Arial, sans-serif;


    font-style: normal;
    line-height: 1.5;
    cursor: auto;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    margin-bottom: 20px;
    overflow: hidden;
    left: 0;
    right: 0;
  }

.wide-container {
  max-width: 960px;
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  box-sizing: border-box;
}
#blogSection {
  background: #e9e9e9 url('../../assets/patternWhite.png') repeat center -638px;
  background-size: 300px;
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
  margin-bottom: 0;
  transition: all 0.2s;
  top: 100%;
  width: 100%;
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

.title-section .title-wrap {
  background: black;
  direction: inline-block;
  padding: 0.25em 18em 0.25em 6em;
  clip-path: polygon(0 0, 100% 0, 85% 100%, 0 100%);
  position: relative;
  left: -1em;
  display: flex;
  margin-bottom: 0;
}

.title {
  color: #ccc;
}

.inner .title-wrap span {
  word-break: break-all;
  font-size: 0.9em;
  height: 70px;
  display: block;
  background: #333c;
  padding: 1em;
  color: #ffffff;
}

#blogSection {
  padding: 2em 0;
  position: relative;
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
  .post-wrap:hover .inner {
    background: initial;
  }

  .inner {
    position: relative;
  }

  #blogTitleWrap {
    position: relative;
    color: #000000;
    top: 4px;
    margin-bottom: 2px;
  }

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
    padding: 0;
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
  .post-wrap:hover .inner {
    background: initial;
  }
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

  .post-wrap .post-link {
    transform: scale(1);
  }
  .inner {
    position: relative;
  }

  #blogTitleWrap{
    margin-bottom: -35px;
  }
}
</style>
