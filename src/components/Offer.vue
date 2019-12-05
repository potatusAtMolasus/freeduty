<template>
  <div class="offer-wrap outer">
    <router-link :to="url">
      <div class="offer-wrap">
        <div class="discount">
          <img src="../assets/discount.png" />
        </div>
        <div class="offer-img-wrap">
          <img :src="getImgUrl(image)" />
        </div>
        <div class="title-wrap">
          <p class="title">{{ title }}</p>
        </div>
        <div class="price-wrap">
          <div class="old-price">{{ oldPrice }}</div>
          <div class="new-price">{{ newPrice }}</div>
        </div>
      </div>
    </router-link>
  </div>
</template>
<script>
export default {
  props: {
    offerData: Object,
  },
  data(){
    return {
      id: this.offerData.id,
      title: this.offerData.title,
      image: this.offerData.image,
      newPrice: this.offerData.newPrice,
      oldPrice: this.offerData.oldPrice,
      url: this.offerData.url,
    }
  },
  methods:{
    getImgUrl(pic) {
      return require('../assets/'+pic)
    }
  }
}
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
.offer-wrap {
  width: 200px;
  padding: 10px;
  margin: 0px;
  box-shadow: 2px 3px 10px 5px #ccc;
  position: relative;
  transition: all .2s;
  cursor: pointer;
}
.offer-wrap:hover {
  box-shadow: 2px 3px 10px 10px #ccc;
}
.outer.offer-wrap{
  margin: 3em 2em;
}
.discount{
  position: absolute;
  width: 8em;
  height: 8em;
  right: -1em;
  top: 0em;
  transform: rotate(0deg);
  transition: transform .2s;
}
.offer-wrap:hover .discount{
  transform: rotate(400deg);
}
.discount img{
  filter: none; 
}
.offer-wrap:hover .discount img{
    filter: drop-shadow(5px 5px 5px #222); 
}
.offer-img-wrap{
  height: 200px;
  margin: auto;
  display: flex;
}
.offer-wrap img {
  height: 100%;
  margin: auto;
}
.price-wrap{
  display: flex;
  justify-content: center;
}
.price-wrap>div{
  margin: 0 .2em;
  vertical-align: text-bottom;
}
.old-price{
  font-size: .9em;
  position: relative;
  line-height: 1.6em;
}
.old-price:after{
  content: '';
  display: block;
  height: 2px;
  width: calc(100% + .5em);
  background: #222;
  top: .7em;
  left: -.25em;
  position: absolute;
}
.new-price{
  display: flex;
  font-size: 1.4em;
  color: red;
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

@media(max-width: 1000px){
  p.title {
    height: 4.5em;
    font-size: .9em;
  }
  .offer-img-wrap{
    height: 100px;
  }
  .outer.offer-wrap{
    margin: 1.5em 1em;
  }
  .offer-wrap {
    width: 140px;
    padding: 9px;
    margin: 0px;
  }
  .discount{
    width: 5em;
    height: 5em;
    right: 0em;
    top: 0em;
  }
}

@media(max-width: 500px){
  p.title {
    height: 7em;
    font-size: 1.2em;
  }
  .offer-img-wrap{
    height: 100px;
  }
  .outer.offer-wrap{
    margin: 1.5em 1em;
  }
  .offer-wrap {
    width: 130px;
    padding: 9px;
    margin: 0px;
  }
  .discount{
    width: 5em;
    height: 5em;
    right: 0em;
    top: 0em;
  }
}
</style>