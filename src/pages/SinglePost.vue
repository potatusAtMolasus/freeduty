<template>
  <main>
    <div id="postWrap">
      <div id="postContent">
        <div>Пост: {{ currentPost.title }}</div>
      </div>
      <div id="navigation">
        <router-link v-if="prevPost.id" id="" :to="'/post/' + prevPost.id">
          <div>
            {{ prevPost.title }}
          </div>
        </router-link>

        <router-link v-if="nextPost.id" :to="'/post/' + nextPost.id">
          <div>
            {{ nextPost.title }}
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
    }
  }
};
</script>

<style>
</style>