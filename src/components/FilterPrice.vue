<template>
  <div class="filter-wrap">
    <div @click="toggle=!toggle" class="filter-top">
      <span class="toggle" >
        <i :class="{rotate: toggle}" class="fa fa-chevron-down"></i>
      </span>
      <span>{{ title }}</span>
    </div>
    <div :class="{'filter-body': true, 'no-height': !toggle}" >
      <div class="inputs">
        <input type=number class="inpur-number" @change="lowerChange" v-model="lower" name="lower" id="lower">
        <span class="minus">-</span>
        <input type=number class="inpur-number" @change="higherChange" v-model="higher" name="higher" id="higher">
      </div>
      <div class="range-wrap">
        <vue-slider v-bind="options" @change="valueChange" v-model="value" />
      </div>
    </div>
  </div>
</template>

<script>
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/antd.css'

export default {
  props: {
    min: {
      type: Number,
    },
    max: {
      type: Number,
    },
    title: {
      type: String,
      default: "Фильтр"
    }
  },
  data() {    
    return {
      toggle: false,
      options: {
        min: 0,
        max: 1000000,
      },
      lower: 0,
      higher: 1000,
      value: [0, 1000],
    };
  },
  watch: {
    min(){
      this.options = {
        min: this.min,
        max: this.max,
      };
      this.lower = this.min;
      this.value = [Number(this.lower), this.value[1]];
    },
    max(){
      this.options = {
        min: this.min,
        max: this.max,
      };
      this.higher = this.max;      
      this.value = [this.value[0], Number(this.higher)];
    },
  },
  methods: {
    valueChange(){
      this.lower = this.value[0];
      this.higher = this.value[1];
      this.throwValue();
    },
    lowerChange(){
      if(this.lower < this.min) this.lower = this.min;
      if(this.lower > this.higher) this.higher = this.lower;
      this.value = [Number(this.lower), Number(this.higher)];
      this.throwValue();
    },
    higherChange(){
      if(this.higher > this.max) this.higher = this.max;
      if(this.higher === '') this.higher = this.value[1];
      else if(this.higher < this.lower) this.lower = this.higher;
      this.value = [Number(this.lower), Number(this.higher)];
      this.throwValue();
    },
    throwValue(){
      this.$emit('input', this.value);
    },
    reset(){
      this.higher = this.max;      
      this.lower = this.min;      
      this.value = [Number(this.lower), Number(this.higher)];
    },
  },
  components: {
    VueSlider
  },
}
</script>
<style scoped>
.toggle{
  padding-right: .6em;
}
.toggle i {
  transition: transform linear .2s;
  transform: rotate(0deg);
}
.toggle i.rotate {
  transform: rotate(180deg);
}
.inputs{
  display: flex;
  justify-content: space-between;
}
.filter-body{
  overflow: hidden;
  max-height: 200px;
  transition: max-height .4s linear;
  width: 100%;
  box-sizing: border-box;
  background: #ccc;
  border-right: 1px solid #aaa;
  border-left: 1px solid #aaa;
  color: #333;
}
.filter-body.no-height{
  max-height: 0;
}
.range-wrap{
  padding: 1em;
}
.filter-top{
  width: 100%;
  padding: 1em 5em 1em 1.1em;
  background: #333;
  box-sizing: border-box;
  color: #aaa;
  cursor: pointer;
}
.inputs{
  margin: 1em;
  line-height: 1.5em;
}
.minus{
  padding: .7em;
  line-height: 1.5em;

}
.inpur-number{
  padding: 1em;
  border: 2px solid #333c;
  border-radius: 5px;
  display: inline;  
}
@media (max-width: 1200px) {
  .inpur-number{
    width: 5em;
  }
}
</style>