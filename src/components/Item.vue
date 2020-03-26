<template>
  <div class="outer-wrap">
    <router-link :to="'/item/' + id">



      <div class="item-wrap">
        
<!--        <div class="rating">-->
<!--          <i class="fa fa-star"></i>-->
<!--          <span>{{ popularity }}</span>-->
<!--        </div>-->


        <div v-if="sale" class="discount">
          <img src="../assets/discount.png" />
        </div>

        <div v-if="sale" class="discount sale-text-wrap">
          <h2 class="sale-text">{{sale}}</h2>
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
      image: this.item.photo,
      // description: this.item.description,
      country: this.item.country,
      price: this.item.price,
      salePrice: this.item.offer_price,
      sale: this.item.offer_name,
      // category: this.item.category,
      // volume: this.item.volume,
      // strength: this.item.strength,
      // brand: this.item.brand,
      popularity: this.item.popularity,
    };
  },
  methods:{
    getImgUrl(pic) {
      return pic || require('../assets/image.jpg');
      
      // try{
      //   return require('../assets/'+pic);
      // } catch(e) {
      //   return '';
      // }
    },
  }
};
</script>

<style scoped>

a{
  text-decoration: none;
  color: inherit;
}
.item-wrap {
    box-shadow: 0 0 4px 2px rgba(0,0,0,.1);
  background: #ffffff;
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
  margin: 0.5em 0.5em 0.5em 0.5em;
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
  height: 5.8em;
}

.rating{
  position: relative;
}
.rating i{
  color: red;
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
  font-size: 1.2em;
  color: red;
}

.discount{
  position: absolute;
  width: 5em;
  height: 5em;
  right: -0.6em;
  top: 0em;
}

.discount img{
  filter: none; 
}

.sale-text-wrap{
  display: flex;
  align-items: center;
  justify-content: center;
}
.sale-text{
  position: relative;
  right: 0;
  color: white;
  width: 50%;
  font-size: .5em;
  line-height: 2em;
  text-transform: uppercase;
  text-align: center;
}

@media(max-width: 900px){
  p.title {
    height: 7.6em;
  }
  .sale-text{
    font-size: .6em;
  }
}
@media(max-width: 500px){
  .discount{
    width: 6em;
    height: 6em;
  }
  .title-wrap{
    font-weight: normal;
    font-size: 1rem;
  }
  .price{
    font-size: 1rem;
  }
  .new-price{
    font-size: 1rem;
  }
  .old-price{
    font-size: .7rem;
  }
  p.title {
    height: 6.8em;
    font-size: .9em;
    width: 100%;
    overflow: hidden;
    word-wrap: break-word;
  }
  .price-wrap{
    font-size: 1.5em;
  }
  .item-img-wrap{
    height: 200px;
  }
  .outer-wrap{
    background: white;
    margin: 1.5em .2em;
    box-sizing: border-box;
  }
  .item-wrap {
    padding: 5px;
    margin: 0px;
  }
  .item-wrap {
    padding: 1em;
    margin: 0px;
  }
}
</style>