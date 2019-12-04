<template>
  <div class="outer-wrap">
    <router-link :to="url">
      <div class="popular-wrap">
        <div class="popular-img-wrap">
          <img :src="getImgUrl(image)" />
        </div>
        <div class="title-wrap">
          <p class="title">{{ title }}</p>
        </div>
        <div class="price-wrap">
          <div class="old-price">{{ price }}</div>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  props: {
    popularData: Object
  },
  data() {
    return {
      id: this.popularData.id,
      title: this.popularData.title,
      image: this.popularData.image,
      price: this.popularData.price,
      url: this.popularData.url
    };
  },
  methods:{
    getImgUrl(pic) {
      return require('../assets/'+pic)
    }
  }
};
</script>

<style scoped>
a{
  text-decoration: none;
  color: inherit;
}
.wrapper {
  width: 100%;
  margin: 20px;
  display: flex;
  flex-direction: column;
}
.popular-wrap {
  background: white;
  padding: 10px;
  margin: 0px;
  box-shadow: 2px 3px 10px 5px #444;
  position: relative;
  transition: all .2s;
  cursor: pointer;
}
.popular-wrap:hover {
  box-shadow: 2px 3px 10px 10px #444;
}
.outer-wrap{
  margin: 3em 2em;
  background: white;
}
.popular-img-wrap{
  height: 200px;
  margin: auto;
  display: flex;
}
.popular-wrap img {
  height: 100%;
  margin: auto;
}
.price-wrap{
  display: flex;
  justify-content: center;
}
.title-wrap{
  font-weight: bold;
  position: relative;
}
.title-wrap:after{
  content: '';
  display: block;
  height: 2px;
  width: 94%;
  background: #222;
  bottom: -.7em;
  left: 3%;
  position: absolute;
}
p.title {
  height: 3.8em;
}
@media(max-width: 500px){
  p.title {
    height: 6.6em;
    font-size: 1.1em;
  }
  .price-wrap{
    font-size: 1.5em;
  }
  .popular-img-wrap{
    height: 100px;
  }
  .outer-wrap{
    margin: 1.5em 1.5em;
    width: 180px;
    box-sizing: border-box;
  }
  .popular-wrap {
    padding: 5px;
    margin: 0px;
  }
  .outer-wrap{
    margin: 1.5em .5em;
  }
  .popular-wrap {
    padding: 1em;
    margin: 0px;
  }
}
</style>