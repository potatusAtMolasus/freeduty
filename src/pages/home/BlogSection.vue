<template>
  <section id="blogSection">
    <div class="x" :style="{'grid-template-areas': layout}">

      <div class="post-wrap" v-for="post in posts" :key="post.id" :style="{'grid-area': post.area}">
        {{post.area}}
        <div class="inner-post-wrap">
          <h2 class="title">{{ post.title }}</h2>
        </div>
      </div>



      <!-- <div class="post-wrap first-post">
        <div class="inner-post-wrap">
          <h2 class="title">Lorem1</h2>
        </div>
      </div>
      
      
      <div class="post-wrap second-post">
        <div class="inner-post-wrap">
          <h2 class="title">Lorem2</h2>
        </div>
      </div>
      <div class="post-wrap thrid-post">
        <div class="inner-post-wrap">
          <h2 class="title">Lorem3</h2>
        </div>
      </div>
      <div class="post-wrap fourth-post">
        <div class="inner-post-wrap">
          <h2 class="title">Lorem4</h2>
        </div>
      </div>
      <div class="post-wrap fifth-post">
        <div class="inner-post-wrap">
          <h2 class="title">Lorem5</h2>
        </div>
      </div> -->


    </div>
  </section>
</template>

<script>
export default {
  name: "BlogSection",
  props:{
    postsData: Array,
  },
  data() {
    return {
      posts: [],
      layout: '',
    };
  },
  watch: {
    postsData(){
      console.log('this.postsData = ',this.postsData);
      
      if (this.postsData.length < 5) return
      this.posts = this.postsData.map(post=>{return {area: post.id+'post', ...post}});
      
      let posts = this.posts;
      console.log('posts = ', posts);
      this.layout = `
          "${posts[0].area} ${posts[0].area} ${posts[1].area} ${posts[3].area}"
          "${posts[0].area} ${posts[0].area} ${posts[1].area} ${posts[4].area}"
          "${posts[0].area} ${posts[0].area} ${posts[2].area} ${posts[2].area}"`;
    }
  }
};
</script>
<style>
.post-wrap {
  background: #ccc;
  position: relative;
  padding: 0.7em;
}
.inner-post-wrap {
  background: #ccc;
  border: 2px solid #222;
  width: 100%;
  height: 100%;
  display: flex;
  transition: all 0.4s ease-in-out;
  transform: scale(1);
}
.post-wrap:hover .inner-post-wrap {
  transform: scale(0);
}
.inner-post-wrap .title {
  margin: auto;
}
.x {
  width: 1000px;
  height: 500px;
  padding: 30px;
  display: grid;
  /* grid-template-areas:
    "first first second fourth"
    "first first second fifth"
    "first first thrid thrid"; */
  grid-gap: 0.7em;
}

/* .first-post {
  grid-area: first;
}
.second-post {
  grid-area: second;
}
.thrid-post {
  grid-area: thrid;
}
.fourth-post {
  grid-area: fourth;
}
.fifth-post {
  grid-area: fifth;
} */
</style>
