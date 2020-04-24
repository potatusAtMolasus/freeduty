<template>
  <section id="popularSection">
    <div class="back"></div>
      <div id="popuplarWrap">
        <div id="popularTitleWrapWrap">
          <div id="popularTitleWrap">
            <h2>Популярное</h2>
          </div>
        </div>

        <div id="popularItemsWrap">
          <carousel
                  id="popcor"
            :autoplay="false"
            :scrollPerPage="false"
            :loop="true"
            :autoplayTimeout="2500"
            :centerMode="true"
            :perPage="perPage"
            :paginationEnabled="false"
            :navigationEnabled="true"
            :paginationColor="'#454545'"
          >
            <slide v-for="i in popularItems" :key="i.id">
              <item :item="i"></item>
            </slide>
          </carousel>
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
    width: Number,
  },
  components: {
    Item
  },
  computed:{
    perPage(){    
      let perPage;
      if (this.width > 2080) perPage = 9;
      else if (this.width > 1680) perPage = 7;
      else if (this.width > 1400) perPage = 5;
      else if (this.width > 1200) perPage = 4;
      else if (this.width > 900) perPage = 3;
      return this.isMobile ? 2 : perPage;
    }
  }
};
</script>
<style scoped>

 #popcor {
   padding-bottom: 3.2em;
 }
.back {
  color: #222;
  font-style: normal;
  line-height: 1.5;
  cursor: auto;
  font-family: roboto,Arial,sans-serif;
  font-size: 1rem;
  font-weight: 400;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  background: #000;
  width: 696px;
  height: 480px;
  padding-top: 105px;
  position: absolute;
  top: 0;
  left: 50%;
  margin-left: -348px;
}

#popularSection {
  background: #4f4f4f;
  background-size: 300px;
  position: relative;
  z-index: 300;
  clear: both;
  padding-left: 1em;
  padding-right: 1em;
}

#popularSection:before {
  left: 50%;
  margin-left: -950px;
}

#popularSection:after {
  right: 50%;
  margin-right: -950px;
}

#popularSection:before,
#popularSection:after {
  content: '';
  background: url(../../assets/patternBlack.png) repeat-y center -638px;
  width: 554px;
  height: 543px;
  position: absolute;
  top: 0;
}


#popuplarWrap {
  position: relative;
  display: flex;
  justify-content: center;
  overflow: visible;
  padding: 3em 4em 4em 4em;
}
#popularTitleWrapWrap {
  position: absolute;
  top: -3em;
  display: flex;
  z-index: 400;
}
#popularTitleWrap {
  position: relative;
  padding: 1em 15.9em;
  background: black;
  color: #ddd;
  margin: auto;
}

#popularTitleWrap h2 {
  margin-top: 0;
  width: 100%;
  text-align: center;
  font-size: 1.75rem;
  font-weight: normal;
  text-transform: uppercase;
  font-family: roboto, Arial, sans-serif;
}

#popularItemsWrap {
  z-index: 300;
  width: 100%;
  /* box-shadow: #555 2px 2px 10px 5px; */
}


@media(max-width: 800px){
    #popuplarWrap{
    display: block;
  }
  #popularText{
    width: 100%;
    box-sizing: border-box;
  }
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
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 0;
    padding-top: 1em;
    max-width: 696px;
  }
}

@media(max-width: 500px){
  #popularSection:before,
  #popularSection:after {
    position: static;
  }

  #popuplarWrap{
    display: block;
  }
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
    border: none;
    margin-bottom: 10px;
  }
}
</style>