<template>
  <main id="offersPage">
    <div class="wide-container">
      <div class="title-section">
        <div class="title-wrap">
          <h2 class="title">Акции</h2>
          <span class="line"></span>
        </div>
      </div>
      <div id="offerWrap">
        <item v-for="i in displaydata" :key="i.id" :item="i"></item>
      </div>
      <div id="pageSelector">
        <div v-for="i in pages" :class="{current: currentPage === i, 'page-num': true}" :key="i">
          <span @click="getPage(i)">{{ i }}</span>
        </div>
      </div>

    </div>
  </main>
</template>

<script>
import Item from "@/components/Item.vue";
import axiosNoLoad from "axios";
import axios from "@/js/AxiosInstance.js";

export default {
  props: ["scrollPosition"],
  components: {
    Item
  },
  data() {
    let displaydata = this.offers ? this.offers.data : [];
    let page = this.offers ? this.offers.current_page : 1;
    let maxPage = this.offers ? this.offers.last_page : 1;
    let pages = this.getRange(page);
    let currentPage = page;

    return {
      displaydata,
      page,
      maxPage,
      pages,
      currentPage,
      offers: []
    };
  },
  async mounted() {
    this.offers = (await axiosNoLoad.post("http://127.0.0.1:8000/all-offers", {}, {
            headers: {
              'Content-Type': 'application/json',
            }
          })).data;
  },
  watch: {
    offers() {
      this.displaydata = this.offers.data;
      this.page = this.offers.current_page;
      this.currentPage = this.offers.current_page;
      this.maxPage = this.offers.last_page;
      this.pages = this.getRange(this.page);
    }
  },
  methods: {
    async getPage(i) {
      this.offers = (await axios.post("all-offers", { page: i })).data;
    },
    getRange(n) {
      let start = n;
      if (n < 5) {
        start = 4;
      }
      let array = [];
      if (n >= this.maxPage - 3) {
        for (let i = this.maxPage - 5; i <= this.maxPage; i++) {
          array.push(i);
        }
      } else {
        for (let i = start - 3; i <= start + 1; i++) {
          array.push(i);
        }
      }
      if (this.maxPage < 6) {
        array = [];
        let i;
        let j = 3;
        while(j>=0 && start - j > 0){
          i = start - j;
          j--;
        }
        while (i <= this.maxPage) {
          array.push(i);
          i++;
        }
      }

      return array;
    }
  }
};
</script>
<style scoped>
  .wide-container {
    max-width: 960px;
    width: 100%;
    margin-right: auto;
    margin-left: auto;
  }
main {
  background-color: #ff000059;
}
#offersPage {
  background-image: url("../assets/patternBlack.png");
  background-size: 300px;
}
#offersPage.padded-top .wide-container {
  padding-top: 15em;
}
#offersPage .wide-container {
  background: #7d6b6ba6;
  padding: 3em 0em;
}
#offerWrap {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 1em;
}
.title-section {
  width: 100%;
  display: flex;
  overflow: hidden;
  position: relative;
}
.title-wrap {
  background: black;
  direction: inline-block;
  padding: 0.25em 8em 0.25em 6em;
  clip-path: polygon(0 0, 100% 0, 85% 100%, 0 100%);
  position: relative;
  left: -1em;
  display: flex;
}
.title {
  color: #ccc;
}
.line {
  background: red;
  height: 100%;
  width: 4em;
  position: absolute;
  right: 0;
  top: 0;
  display: block;
  clip-path: polygon(70% 0, 100% 0, 100% 100%, 0 100%);
}
#pageSelector {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  padding: 1em;
}
#pageSelector .current.page-num {
  background: #444;
}
#pageSelector .page-num {
  background: #aaa;
  cursor: pointer;
  margin: 1em 0.7em;
  transition: all 0.2s linear;
  border-radius: 3px;
}
#pageSelector .page-num span {
  display: block;
  padding: 0.5em 0.8em;
}
#pageSelector .page-num:hover {
  background: red;
}
@media (max-width: 992px) {
  #offerWrap {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
  }
}
@media (max-width: 768px) {
  #offerWrap {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
  }
}
@media (max-width: 576px) {
  #offerWrap {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
  #offersPage .wide-container {
    padding: 3em 0em;
  }
}
</style>

