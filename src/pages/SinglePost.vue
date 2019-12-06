<template>
  <main>
    <div id="postWrap">
      <div id="postContent">
        
        <div>Пост: {{ currentPost.title }}</div>
        <div id="date">{{ currentPost.date }}</div>
        <div id="imageWrap">
          <img :src="getImgUrl(currentPost.image)" alt="Не удалось загрузить картинку, посетите страницу в instagram">
        </div>
        <p id="text">{{ currentPost.text }}</p>

      </div>
      <div id="navigation">
        <router-link id="prev" v-if="prevPost.id" :to="'/post/' + prevPost.id">
          <div :style="{ 'background-image': 'url('+getImgUrl(prevPost.image)+')' }">
            <p>
              {{ prevPost.title }}
            </p>
          </div>
        </router-link>

        <router-link id="next" v-if="nextPost.id" :to="'/post/' + nextPost.id">
          <div :style="{ 'background-image': `url(${getImgUrl(nextPost.image)})` }">
            <p>
              {{ nextPost.title }}
            </p>
          </div>
        </router-link>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  props:{
    posts: Array,
  },
  data(){
    return {
      nextPost: {},
      prevPost: {},
      currentPost: {},
    }
  },
  mounted(){
    this.getPosts();
  },
  watch:{
    posts(){
      this.getPosts();
    },
    $route(){
      this.getPosts();
    },
  },
  methods:{
    getPosts(){
      this.nextPost = this.posts.find(post=>post.id===Number(this.$route.params.id)+1) || {};
      this.prevPost = this.posts.find(post=>post.id===Number(this.$route.params.id)-1) || {};
      this.currentPost = this.posts.find(post=>post.id==Number(this.$route.params.id)) || {};  
    },
    getImgUrl(pic) {
      try{
        return require('../assets/'+pic);
      } catch(e) {
        return '';
      }
    }
  }
};
</script>

<style scoped>
main{
  padding: 5em;
  background: #aaa;
}
#postWrap{
  background: #fff;
}
#imageWrap{
  width: 100%;
}
#imageWrap img{
  width: 100%;
}
#navigation{
  display: flex;
  width: 100%;
  height: 5.5em;
}
#prev, #next{
  width: 50%;
  height: 100%;
}
#prev div, #next div{
  height: 100%;
  display: flex;
}
#prev div:hover, #next div:hover{
  position: relative;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1), 0 2px 3px rgba(0, 0, 0, 0.2);
}
#prev div:hover:before, #next div:hover:before{
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
#prev div p, #next div p{
  margin: auto;
}
  

</style>