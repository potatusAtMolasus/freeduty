<template>
  <div class="filter-wrap">
    <div @click="toggle=!toggle" class="filter-top">
      <span class="toggle" >
        <i :class="{rotate: toggle}" class="fa fa-chevron-down"></i>
      </span>
      <span>{{ title }}</span>
    </div>
    <div :class="{'filter-options': true, 'no-height': !toggle}" >
      <div v-for="option in options" :key="option" class="filter-option">
        <input
          type="checkbox"
          :value="option.value"
          :id="option.value + 'option'"
          v-model="checkedOptions"
        />
        <label :for="option.value + 'option'" class="label">
          <span class="check-wrap">
            <i class="fa fa-check checker" v-if="checkedOptions.includes(option.value)"></i>
            <i class="fa fa-check holder"></i>
          </span>
          <span class="label-text">{{ option.label }}</span>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    options: {
      type: Array,
      default() {
        return [];
      }
    },
    checked: {
      type: Array,
      default() {
        return [];
      }
    },
    title: {
      type: String,
      default: "Фильтр"
    }
  },
  data() {
    return {
      checkedOptions: this.checked,
      toggle: false
    };
  },
  watch:{
    checkedOptions(){
      this.$emit('input', this.checkedOptions)()
    },
  },
};
</script>

<style scoped>
aside{
  width: 200px;
}
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
.filter-options{
  overflow: hidden;
  max-height: 200px;
  transition: max-height .4s linear;
}
.filter-options.no-height{
  max-height: 0;
}
.filter-top{
  width: 100%;
  padding: 1em 5em 1em 1.1em;
  background: #333;
  box-sizing: border-box;
  color: #aaa;
  cursor: pointer;
}
.filter-options{
  width: 100%;
}
.filter-option{
  width: 100%;
  height: 100%;
  background: #ccc;
  border: 1px solid #aaa;
  color: #333;
  text-align: left;
  box-sizing: border-box;
}

.filter-option input{
  display: none;
}
.filter-option .label{
  width: 100%;
  height: 100%;
  display: flex;
  padding: .7em 5em .7em .7em;
  box-sizing: border-box;
  cursor: pointer;
}
.filter-option .label .label-text{
  display: inline-flex;
  height: 1em;
  padding: .2em;
  margin: auto 0;
}
.filter-option .label .check-wrap{
  border-radius: 3px;
  border: 2px solid #333;
  width: 1em;
  height: 1em;
  padding: .2em;
  display: inline-block;
  position: relative;
}
.filter-option .label .check-wrap .holder{
  position: absolute;
  top: .2em;
  left: .2em;
  opacity: 0;
  transition: opacity .2s;
}
.checker{
  position: absolute;
  top: .2em;
  left: .2em;
}
.filter-option:hover .label .check-wrap .holder{
  opacity: .6;
}
</style>
