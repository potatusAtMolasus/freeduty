<template>
  <main>
    <div id="postWrap" :class="{'top': scrollPosition}">
      <div id="postContent">
        <carousel
          :key="currentPost.id"
          :autoplay="false"
          :loop="false"
          :adjustableHeight="true"
          :perPage="1"
          :paginationEnabled="false"
          :navigationEnabled="true"
          :paginationColor="'#454545'"
        >
          <slide v-for="i in currentPost.images" :key="i">
            <div class="imageWrap">
              <img
                :src="getImgUrl(i)"
                alt="Не удалось загрузить картинку, посетите страницу в instagram"
              />
            </div>
          </slide>
        </carousel>
        <p id="text">{{ currentPost.text }}</p>
      </div>
      <div id="navigation">
        <router-link id="prev" v-if="prevPost.id" :to="'/post/' + prevPost.id">
          <div :style="{ 'background-image': 'url('+getImgUrl(prevPost.images[0])+')' }">
            <p>{{ prevPost.title }}</p>
          </div>
        </router-link>

        <router-link id="next" v-if="nextPost.id" :to="'/post/' + nextPost.id">
          <div :style="{ 'background-image': `url(${getImgUrl(nextPost.images[0])})` }">
            <p>{{ nextPost.title }}</p>
          </div>
        </router-link>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  props: {
    posts: Array,
    scrollPosition: Number,
  },
  data() {
    return {
      nextPost: {},
      prevPost: {},
      currentPost: {}
    };
  },
  mounted() {
    this.getPosts();
    setTimeout(()=>this.$children[0].computeCarouselHeight(), 1000)
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
    getPosts() {
      this.nextPost =
        this.posts.find(
          post => post.id === Number(this.$route.params.id) + 1
        ) || {};
      this.prevPost =
        this.posts.find(
          post => post.id === Number(this.$route.params.id) - 1
        ) || {};
      this.currentPost =
        this.posts.find(post => post.id === Number(this.$route.params.id)) || {};
    },
    getImgUrl(pic) {
      try {
        return require("../assets/" + pic);
      } catch (e) {
        return "";
      }
    }
  }
};
</script>

<style scoped>
main {
  width: 100%;
  background: #aaa;
  display: flex;
}
#postWrap.top {
  margin: 20% auto;
}
#postWrap {
  margin: 5% auto;
  background: #fff;
  width: 800px;
}
.imageWrap img {
  width: 100%;
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
</style>
<style>
.VueCarousel-slide-adjustableHeight {
  display: block !important;
}
.VueCarousel-inner {
  align-items: flex-start !important;
}
</style>