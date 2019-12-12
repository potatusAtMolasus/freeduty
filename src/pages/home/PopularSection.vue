<template>
  <section id="popularSection">
      <div id="popuplarWrap">
        <div id="popularTitleWrapWrap">
          <div id="popularTitleWrap">
            <h2>Популярное</h2>
          </div>
        </div>

        <div id="popularItemsWrap">
          <carousel
            :autoplay="false"
            :loop="false"
            :centerMode="true"
            :perPage="perPage"
            :paginationEnabled="true"
            :navigationEnabled="true"
            :paginationColor="'#454545'"
          >
            <slide v-for="i in popularItems" :key="i.id">
              <item :item="i"></item>
            </slide>
          </carousel>
        </div>

        <div id="popularFooterWrapWrap">
          <div id="popularFooterWrap">
            <router-link id="popularsBtn" to="/popular">
              <span>
                 Товары
                <i class="fa fa-arrow-right"></i>
              </span>
            </router-link>
          </div>
        </div>

      </div>
  </section>
</template>

<script>
import Item from "@/components/Item.vue";
export default {
  name: "PopularSection",
  props: {
    popularItems: Array,
    isMobile: Boolean,
  },
  components: {
    Item
  },
  computed:{
    perPage(){
      return this.isMobile ? 2 : 5;
    }
  }
};
</script>
<style scoped>

#popularSection {
  background: #888;
  position: relative;
  z-index: 100;
}
#popuplarWrap {
  position: relative;
  overflow: visible;
  padding: 6em 4em 6em 4em;
}
#popularTitleWrapWrap {
  position: absolute;
  top: -3em;
  left: 0;
  display: flex;
  width: 100%;
  z-index: 200;
}
#popularTitleWrap {
  position: relative;
  padding: 1em 10em;
  background: black;
  color: #ddd;
  margin: auto;
}
#popularItemsWrap {
  z-index: 300;
  /* box-shadow: #555 2px 2px 10px 5px; */
}

#popularFooterWrapWrap{
  position: absolute;
  bottom: -4em;
  left: 0;
  display: flex;
  width: 100%;
  z-index: 200;
}
#popularFooterWrap{
  position: relative;
  padding: 3.5em 8em;
  background: black;
  color: #ddd;
  margin: auto;
}

#popularsBtn{
  text-decoration: none;
  color: red;
}
#popularsBtn{
  padding: 18px 40px;
  margin: 20px 0 10px 0;
  /* background: linear-gradient(180deg, white 5%, green 150%); */
  /* border-radius: 30px; */
  border: 1px solid red;
  font-size: 18px;
  position: relative;
  transition: color .3s;
}
#popularsBtn:after{
  content: '';
  display: block;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0px;
  transition: height .3s;
  background: red;
  z-index: 100;
}
#popularsBtn span{
  position: relative;
  z-index: 200;
}
#popularsBtn:hover:after{
  height: 100%;
}
#popularsBtn:hover{
  color: white;
  box-shadow: #232323 2px 2px 15px 7px;
}

@media(max-width: 800px){
  #popularItemsWrap {
    border: none;
  }
  #popularFooterWrapWrap{
    position: relative;
    bottom: 0;
  }
  #popularFooterWrap{
    width: 100%;
    padding: 3em 4em;
    display: flex;
  }
  #popularsBtn{
    margin: auto;
  }
  .wide-container{
    padding: 0;
  }
  #popuplarWrap {
    padding: 0;
  }
  #popularTitleWrapWrap {
    position: relative;
    margin: 0;
    top: 0;
  }
  #popularTitleWrap{
    padding: 1em;
    width: 100%;
    display: flex;
    justify-content: center;
  }
}

@media(max-width: 500px){
  .wide-container{
    padding: 0;
  }
  #popularContent {
    font-size: 0.8em;
    display: block;
  }
  #popularText{
    width: 100%;
    box-sizing: border-box;
  }
  #popularItemsWrap {
    border: 2px solid #555;
  }
}
</style>