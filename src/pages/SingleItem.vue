<template>
  <div class="wide-container-wrapper">
  <div class="wide-container">
  <div :class="{ 'item-wrap': true, 'not-top': scrollPosition&&!isMobile }">
    <div class="content">
      <div class="title">
        {{ title }}
      </div>
      <div class="country-populaity">
        <div v-if="brand" class="brand">
          <p>Брэнд: {{ brand }}</p>
        </div>

        <div v-if="country" class="country">
          <p>Страна производитель: {{ country }}</p>
        </div>


      </div>

      <div class="price-block">
        <div class="price-wrap" v-if="!sale">
          <div class="price">{{ price }} &#8381;</div>
        </div>
        <template v-else>
          <div class="price-wrap">
            <div class="new-price">{{ salePrice }} &#8381;</div>
            <div class="old-price">{{ price }}</div>
          </div>
          <div class="sale-desc">
            <p><i class="fa fa-exclamation"></i>{{ sale }}</p>            
          </div>
        </template>
      </div>

      <div v-if="category" class="category">
        <p>Категория: {{ category }}</p>
      </div>
      <div v-if="volume" class="volume">
        <p>Объем: {{ volume }}</p>
      </div>
      <div v-if="strength" class="strength">
        <p>Крепость: {{ strength }}</p>
      </div>
      <div v-if="description" class="description">
        <p>{{ description }}</p>
      </div>


    </div>
    <div class="image-wrap">
      <div class="image">
        <img :src="getImgUrl(photo)" alt="Фото отсутствует">
      </div>
    </div>

  </div>
  </div>
  </div>
</template>

<script>
import axios from "@/js/AxiosInstance.js";

export default {
  props:{
    scrollPosition: Number,
    isMobile: Boolean,
  },
  data(){
    return {
      title: '', 
      photo: '',
      description: '',
      country: '',
      price: '',
      salePrice: '',
      sale: '',
      category: '',
      volume: '',
      strength: '',
      brand: '',
      popularity: '',
    }
  },
  async mounted(){
    const data = (await axios.post("get-item", {id: this.$route.params.id})).data;
    
    this.title = data.title, 
    this.photo = data.photo, 
    this.description = data.description, 
    this.country = data.country,
    this.price = data.price,
    this.salePrice = data.offer_price,
    this.sale = data.offer_name,
    this.category = data.category,
    this.volume = data.volume,
    this.strength = data.concentration,
    this.brand = data.brand,
    this.popularity = data.popularity
  },
  computed:{
    saleDescription(){
      return this.sale ? 'Акция действует при покупке 2 единиц товара' : '';
    }
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
  },
}
</script>

<style scoped>
.wide-container {
  max-width: 960px;
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  background: white;
}

.wide-container-wrapper {
  background: #e9e9e9 url('../assets/patternWhite.png') repeat center -638px;
  background-size: 300px;
}

.item-wrap{
  display: flex;
  margin: 0 5%;
}
.item-wrap.not-top{
  padding-top: 10em;
}

.image-wrap{
  flex: 1;
  margin: 5em;
  width: 100%;
}
.image{
  width: 80%;
}
.image img{
  width: 100%;
}

.content{
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 5em;
}
.content .title{
  font-size: 1.5em;
}
.content .country-populaity{
  display: flex;
  justify-content: left;
}
.content .country-populaity .brand, .content .country-populaity .country{
  color: #777;
  font-size: .83em;
}
.brand, .rating, .country{
  padding: .3em .5em;
  margin: auto 0;
}
.rating{
  position: relative;
  padding-right: 1.3em; 
  padding-left: 0;
}
.rating i{
  color: gold;
  font-size: 1.8em;
}
.rating span{
  position: absolute;
  padding: .3em;
  font-size: .83em;
  color: #777;
}

.price-block{
  display: flex;
  flex-direction: column;
  padding-top: 3em;
  justify-content: left;
}
.price-wrap{
  display: flex;
  color: #333;
}
.price-wrap>div{
  margin: 0 .2em;
  vertical-align: text-bottom;
}
.old-price{
  font-size: 1.4em;
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
  font-size: 1.8em;
}
.sale-desc{
  color: red;
}
.sale-desc i{
  padding-right: .3em; 
}
.category, .volume, .strength, .description{
  font-size: .97em;
  color: #777;
}
@media(max-width: 500px){
  .item-wrap{
    flex-direction: column-reverse;
  }
  .content{
    padding: 1em;
  }
  .image-wrap{
    margin: 0;
  }
  .image{
    margin: auto;
  }
}
</style>