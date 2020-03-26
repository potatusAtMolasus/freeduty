<template>
  <main>
    <div id="postWrap">
      <div id="postContent">
        <div>
          <div v-for="i in [currentPost.image_url]" :key="i">
            <div class="imageWrap">
              <img
                :src="getImgUrl(i)"
                alt="Не удалось загрузить картинку, посетите страницу в instagram"
              />
            </div>
          </div>
        </div>
        <p id="text">{{ currentPost.caption }}</p>
      </div>
      <!-- <div id="navigation">
        <router-link id="prev" v-if="prevPost" :to="'/post/' + prevPost.id">
          <div :style="{ 'background-image': 'url('+getImgUrl(prevPost.image_url)+')' }">
            <p>{{ prevPost.title }}</p>
          </div>
        </router-link>

        <router-link id="next" v-if="nextPost" :to="'/post/' + nextPost.id">
          <div :style="{ 'background-image': `url(${getImgUrl(nextPost.image_url)})` }">
            <p>{{ nextPost.title }}</p>
          </div>
        </router-link>
      </div> -->
    </div>
  </main>
</template>

<script>
import axios from "@/js/AxiosInstance.js";

export default {
  props: {
    posts: Array,
    scrollPosition: Number
  },
  data() {
    return {
      // nextPost: {},
      // prevPost: {},
      currentPost: {}
    };
  },
  mounted() {
    this.getPosts();
  },
  watch: {
    posts() {
      this.getPosts();
    },
    $route() {
      this.getPosts();
    }
  },
  methods: {
    async getPosts() {
      
      this.currentPost = (await axios.post("post", {id: this.$route.params.id})).data;

      // let postId = this.posts.findIndex(
      //   post => post.id === Number(this.$route.params.id)
      // );
      // if (postId === -1) return;

      // this.nextPost = postId === -1 ? {} : this.posts[postId + 1];
      // this.prevPost = postId === -1 ? {} : this.posts[postId - 1];
      // this.currentPost = this.posts[postId];
    },
    getImgUrl(pic) {
      return pic || require("../assets/image.jpg");

      // try {
      //   return require("../assets/" + pic);
      // } catch (e) {
      //   return "";
      // }
    }
  }
};
</script>

<style scoped>
main {
  background: #e9e9e9 url('../assets/patternWhite.png') repeat center -638px;
  background-size: 300px;
  width: 100%;
  display: flex;
  padding: 1em;
  box-sizing: border-box;
}
#postWrap.top {
  margin: 20% auto;
}
#postWrap {
  margin: 5% auto;
  background: #fff;
  max-width: 800px;
}
.imageWrap img {
  width: 100%;
  display: block;
}
#navigation {
  display: flex;
  width: 100%;
  height: 5.5em;
}
#prev,
#next {
  width: 50%;
  height: 100%;
}
#prev div,
#next div {
  height: 100%;
  display: flex;
}
#prev div:hover,
#next div:hover {
  position: relative;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1), 0 2px 3px rgba(0, 0, 0, 0.2);
}
#prev div:hover:before,
#next div:hover:before {
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
  z-index: 250;
}
#prev div p,
#next div p {
  margin: auto;
}
#text{
  /* font-family: 'Open Sans Condensed', sans-serif; */
  /* font-family: 'Nunito', sans-serif; */
  /* font-family: 'Pacifico', cursive; */
  /* font-family: 'Comfortaa', cursive; */
  font-family: "Alegreya", serif;
  text-align: justify;
  text-indent: 3em;
  padding: 1em;
  background: #222c;
  margin: 0;
  word-wrap: pre;
  color: #ccc;
}
#text::first-letter {
  font-size: 1.3em;
  padding-right: 0.1em;
  font-family: "Pacifico", cursive;
  color: #ccc7;
}
@media (max-width: 992px) {
  #postWrap{
    width: 100%;
  }
}
</style>
<style>
.VueCarousel-slide-adjustableHeight {
  display: block !important;
}
.VueCarousel-inner {
  align-items: flex-start !important;
}
</style>