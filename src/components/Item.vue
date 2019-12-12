<template>
  <div class="outer-wrap">
    <router-link :to="'/item/' + id">



      <div class="item-wrap">
        
        <div class="rating">
          <i class="fa fa-star"></i>
          <span>{{ popularity }}</span>
        </div>


        <div v-if="sale" class="discount">
          <img src="../assets/discount.png" />
        </div>


        <div class="item-img-wrap">
          <img :src="getImgUrl(image)" />
        </div>
      
      
        <div class="title-wrap">
          <p class="title">{{ title }}</p>
        </div>
      
      
        <div class="price-wrap" v-if="!sale">
          <div class="price">{{ price }} &#8381;</div>
        </div>
        <div v-else class="price-wrap">
          <div class="old-price">{{ price }}</div>
          <div class="new-price">{{ salePrice }} &#8381;</div>
        </div>      
      
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  props: {
    item: Object
  },
  data() {
    return {
      id: this.item.id,
      title: this.item.title,
      image: this.item.image,
      // description: this.item.description,
      country: this.item.country,
      price: this.item.price,
      salePrice: this.item.salePrice,
      sale: this.item.sale,
      // category: this.item.category,
      // volume: this.item.volume,
      // strength: this.item.strength,
      // brand: this.item.brand,
      popularity: this.item.popularity,
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
.item-wrap {
  background: #E9E9E9;
  padding: 10px;
  margin: 0px;
  /* box-shadow: 2px 3px 10px 5px #444; */
  position: relative;
  transition: all .2s;
  cursor: pointer;
}
.item-wrap:hover {
  box-shadow: 2px 3px 15px 3px #666;
}
.outer-wrap{
  margin: 3em 2em;
  background: white;
}
.item-img-wrap{
  height: 200px;
  margin: auto;
  display: flex;
}
.item-wrap img {
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
  height: 4.8em;
}

.rating{
  position: relative;
}
.rating i{
  color: gold;
  font-size: 2em;
}
.rating span{
  position: absolute;
  bottom: .3em; 
  padding-left: .3em;
  font-size: 1.2em;
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


.discount{
  position: absolute;
  width: 8em;
  height: 8em;
  right: -1em;
  top: 0em;
  transform: rotate(0deg);
  transition: transform .2s;
}
.item-wrap:hover .discount{
  transform: rotate(400deg);
}
.discount img{
  filter: none; 
}
.item-wrap:hover .discount img{
  filter: drop-shadow(5px 5px 5px #222); 
}

@media(max-width: 500px){
  p.title {
    height: 6.6em;
    font-size: 1.1em;
  }
  .price-wrap{
    font-size: 1.5em;
  }
  .item-img-wrap{
    height: 100px;
  }
  .outer-wrap{
    margin: 1.5em 1.5em;
    width: 180px;
    box-sizing: border-box;
  }
  .item-wrap {
    padding: 5px;
    margin: 0px;
  }
  .outer-wrap{
    margin: 1.5em .5em;
  }
  .item-wrap {
    padding: 1em;
    margin: 0px;
  }
}
</style>