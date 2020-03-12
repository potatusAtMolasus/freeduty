<template>
  <section id="offersSection">
    <div class="wide-container">
      <h2 id="offers-title">Наши Акции</h2>

      <div id="offersContent">
        <div id="offersText">Ассортимент «Дьюти Фри» насчитывает около 3000 алкогольных напитков со всего мира — от демократичных бестселлеров до мировых звезд, отмеченных престижными рейтингами. Благодаря тому, что мы напрямую сотрудничаем с ведущими импортерами, цены для вас мы постарались сделать максимально низкими.</div>
        <div id="offersWrap">
          <carousel
            :autoplay="true"
            :loop="true"
            :scrollPerPage="false"
            :centerMode="true"
            :perPage="perPage"
            :paginationEnabled="false"
            :navigationEnabled="true"
            :paginationColor="'#454545'"
            :autoplayTimeout="2500"
          >
            <slide v-for="i in homeOffers" :key="i.id">
              <item :item="i"></item>
            </slide>
          </carousel>
        </div>
      </div>

      <div id="watchOffersWrap">
        <router-link id="offersBtn" to="/offers">
          <span>
            Все акции
            <i class="fa fa-arrow-right"></i>
          </span>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
import Item from "@/components/Item.vue";

export default {
  name: "OffersSection",
  props: {
    isMobile: Boolean,
    homeOffers: Array
  },
  components: {
    Item
  },
  computed:{
    perPage(){
      return this.isMobile ? 2 : 3;
    }
  }
};
</script>
<style scoped>
#offersSection{
  background-image: url('../../assets/patternBlack.png');
  background-size: 300px;
  position: relative;
  z-index: 200;
}
/* #offersSection .wide-container{} */
#offersContent {
  display: flex;
  justify-content: space-between;
}
#offersWrap {
  background: rgba(180, 180, 180, 0.9);
  padding: 3em;
  flex: 3;
  overflow: hidden;
}
#offersText {
  flex: 1;
  background: black;
  height: 100%;
  width: 30%;
  color: #ddd;
  padding: 1.5em;
  line-height: 1.5em;
}

#watchOffersWrap{
  display: flex;
  justify-content: right;
}
#offersBtn{
  text-decoration: none;
  color: #222;
}
#offersBtn{
  padding: 18px 40px;
  margin: 20px 0 10px 0;
  background: linear-gradient(180deg, #bbb 5%, #E9E9E9 150%);
  /* border-radius: 30px; */
  border: 2px solid #222;
  font-size: 18px;
  position: relative;
  transition: color .3s;
  /* text-decoration: 2px underline dotted red; */
}
#offersBtn:after{
  content: '';
  display: block;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0px;
  transition: height .3s;
  background: #222;
  z-index: 100;
}
#offersBtn span{
  position: relative;
  z-index: 200;
}
#offersBtn:hover:after{
  height: 100%;
}
#offersBtn:hover{
  color: white;
}

@media(max-width: 800px){
  .wide-container{
    padding: 0;
  }
  #offersWrap {
    padding: 0 .3em;
  }
  #offersContent {
    font-size: 0.8em;
    display: block;
  }
  #offersText{
    width: 100%;
    box-sizing: border-box;
  }
}

@media(max-width: 500px){
  #offersContent {
    font-size: 0.8em;
    display: block;
  }
  #offersText{
    width: 100%;
    box-sizing: border-box;
  }
  #offersWrap {
    padding: 0 .3em;
  }
  #watchOffersWrap{
    display: flex;
    justify-content: center;
  }
  #offersBtn{
    border: 2px solid #222;
  }
  #offers-title{
    background:#424141eb;
    margin: auto;
    padding: 1em;
  }
}

</style>
