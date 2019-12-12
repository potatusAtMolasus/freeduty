<template>
  <section id="offersSection">
    <div class="wide-container">
      <h2 id="offers-title">Наши Акции</h2>

      <div id="offersContent">
        <div
          id="offersText"
        >Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate asperiores placeat consequatur? Eos excepturi soluta placeat reiciendis rerum. Delectus eaque ea nemo eveniet fugiat qui pariatur ab illum error aspernatur deleniti cumque animi laboriosam tempora eligendi rem corporis quae, esse atque nam accusamus aliquam. Soluta accusantium recusandae velit quia dolorem!</div>
        <div id="offersWrap">
          <carousel
            :autoplay="false"
            :loop="false"
            :centerMode="true"
            :perPage="perPage"
            :paginationEnabled="true"
            :navigationEnabled="true"
            :paginationColor="'#454545'"
          >
            <slide v-for="i in offers" :key="i.id">
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
    offers: Array
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
  
  position: relative;
  z-index: 200;
}
#offersSection .wide-container{
  margin-bottom: 3em;
}
#offersContent {
  display: flex;
  justify-content: space-between;
}
#offersWrap {
  margin: 3em;
  flex: 3;
  overflow: hidden;
}
.VueCarousel-wrapper {
  padding: 30px 15px;
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
  /* background: linear-gradient(180deg, white 5%, green 150%); */
  /* border-radius: 30px; */
  border: 1px solid #222;
  font-size: 18px;
  position: relative;
  transition: color .3s;
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
    margin: 3em 0;
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
    margin: 3em 0;
    padding: 0 .3em;
  }
  #watchOffersWrap{
    display: flex;
    justify-content: center;
  }
  #offersBtn{
    border: 2px solid #222;
  }
}

</style>
