<template>
  <main>
    <div class="search-field">
      <input
        type="text"
        class="search-input"
        @keyup.enter="find"
        v-model="query"
        placeholder="Поиск"
      />
      <button @click="find" class="find-btn">
        <span>
          <i class="fa fa-search"></i>
        </span>
      </button>
    </div>
    <div id="sortWrap">
      <div class="selector-wrap">
        <span>Сортировать по</span>
        <div>
          <combobox placeholder="Сортировать по" :options="comboOptions" v-model="sortBy"></combobox>
        </div>
      </div>
    </div>
    <div id="wrap">
      <div v-for="i in items" :key="i.id">
        <item :item="i"></item>
      </div>
    </div>

    <div id="pageSelector">
      <div v-for="i in pages" :class="{current: current === i, 'page-num': true}" :key="i">
        <span @click="getPage(i)">{{ i }}</span>
      </div>
    </div>
  </main>
</template>

<script>
import Item from "@/components/Item.vue";
import Combobox from "@/components/Combobox.vue";

export default {
  props: {
    data: Array,
    currentPage: Number,
    maxPage: Number
  },
  data() {
    return {
      current: 1,
      pages: [],
      query: "",
      items: [],
      sortBy: "",
      comboOptions: [
        { label: "По возрастанию цены", value: "priceIncr" },
        { label: "По уменьшению цены", value: "priceDecr" }
      ]
    };
  },
  mounted() {
    this.current = this.currentPage;
    this.pages = this.getRange(this.currentPage);
  },
  watch: {
    currentPage() {
      this.current = this.currentPage;
      this.pages = this.getRange(this.currentPage);
    },
    data() {
      this.items = this.data;
    },
    sortBy() {
      if (this.sortBy === "popularity") {
        this.items = this.items.sort((a, b) => b.popularity - a.popularity);
      } else if (this.sortBy === "priceIncr")
        this.items = this.items.sort((a, b) => {
          const aPrice = a.sale ? a.salePrice : a.price;
          const bPrice = b.sale ? b.salePrice : b.price;
          return aPrice - bPrice;
        });
      else if (this.sortBy === "priceDecr")
        this.items = this.items.sort((a, b) => {
          const aPrice = a.sale ? a.salePrice : a.price;
          const bPrice = b.sale ? b.salePrice : b.price;
          return bPrice - aPrice;
        });
    }
  },
  methods: {
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
    },
    find() {
      this.$emit("find", this.query);
    },
    getPage(i) {
      this.$emit("pageSelected", i);
    }
  },
  components: {
    Item,
    Combobox
  }
};
</script>
<style scoped>
main {
  flex: 3;
  margin: 0 2em 0 0;
  background-color: #ccccccee;
}

#sortWrap {
  padding: 1em;
  display: flex;
  justify-content: right;
  position: relative;
  width: auto;
  height: 2em;
}
.search-field {
  padding: 1em 0 0 1em;
}
.search-input {
  padding: 1em;
  background: #efefef;
  color: #aaa;
  border: none;
  width: 25em;
}
.find-btn {
  text-decoration: none;
  position: relative;
  top: 1px;
  color: #aaa;
  padding: 11px 20px;
  background: linear-gradient(180deg, #222 5%, #444 150%);
  border: none;
  font-size: 18px;
  position: relative;
  transition: color 0.3s;
  cursor: pointer;
}
.find-btn:after {
  content: "";
  display: block;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0px;
  transition: height 0.3s;
  background: red;
  z-index: 100;
}
.find-btn span {
  position: relative;
  z-index: 200;
}
.find-btn:hover:after {
  height: 100%;
}
.find-btn:hover {
  color: white;
}

.selector-wrap {
  display: flex;
  position: absolute;
  z-index: 200;
}
.selector-wrap span {
  padding-right: 1em;
  position: relative;
  top: 1em;
}
.selector-wrap > div {
  position: relative;
}
.outer-wrap {
  background: white;
  margin: 0.5em 0.5em;
}
.combo-wrap {
  display: inline;
}
#wrap {
  padding: 1em;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-gap: 0em;
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
@media (max-width: 1000px) {
  #wrap {
    padding: 1em;
    grid-template-columns: 1fr 1fr 1fr;
  }
}
@media (max-width: 700px) {
  #wrap {
    grid-template-columns: 1fr 1fr;
  }
  .search-input {
    width: 13em;
  }
  .selector-wrap {
    width: 10em;
  }
  .selector-wrap span {
    width: 20em;
    font-size: 0.85em;
    display: none;
  }
}
@media (max-width: 500px) {
  main {
    margin: 0;
  }
  #wrap {
    grid-template-columns: 1fr 1fr;
  }
  .selector-wrap span {
    padding-right: 0;
  }
}
</style>
