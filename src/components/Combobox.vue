<template>
  <div class="combo-wrap">
    <div @click="toggle=!toggle" class="combo-top">
      <div>
        <span>{{ label }}</span>
        <span class="toggle">
          <i :class="{rotate: toggle}" class="fa fa-chevron-down"></i>
        </span>
      </div>
    </div>
    <div :class="{'combo-options': true, 'no-height': !toggle}">
      <div v-for="option in options" :key="option.value" class="combo-option" @click="pick(option)">
        <span
          :for="option.value + 'option'"
          :class="{label: true, picked: option === pickedOption}"
        >
          <span class="label-text">{{ option.label }}</span>
        </span>
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
    }
  },
  data() {
    return {
      checkedOptions: this.checked,
      toggle: false,
      pickedOption: ""
    };
  },
  computed: {
    value() {
      return this.pickedOption.value;
    },
    label() {
      return this.pickedOption.label;
    }
  },
  methods: {
    pick(option) {
      this.toggle = false;
      this.pickedOption = option;
      this.$emit("input", option.value);
    }
  }
};
</script>

<style scoped>
.toggle {
  padding-left: 0.6em;
}
.toggle i {
  transition: transform linear 0.2s;
  transform: rotate(0deg);
}
.toggle i.rotate {
  transform: rotate(180deg);
}
.combo-options {
  overflow: hidden;
  max-height: 200px;
  transition: max-height 0.2s linear;
}
.combo-options.no-height {
  max-height: 0;
}
.combo-top {
  display: flex;
  justify-content: flex-end;
  width: 100%;
  padding: 1em;
  background: #efefef;
  box-sizing: border-box;
  color: #aaa;
  cursor: pointer;
}
.combo-options {
  width: 100%;
}
.combo-option {
  width: 100%;
  height: 100%;
  background: #d1cbe3;
  /* background: #999; */
  border: 1px solid #aaa;
  color: #333;
  text-align: left;
  box-sizing: border-box;
  transition: 0.2s;
}

.combo-option:hover {
  background: #ebe8f7;
}
.combo-option .label {
  width: 100%;
  height: 100%;
  display: flex;
  padding: 0.5em 0.5em 0.5em 5em;
  box-sizing: border-box;
  cursor: pointer;
  display: flex;
  justify-content: right;
}
.combo-option .label.picked {
  background: #afaeb3;
}

.combo-option .label .label-text {
  display: inline-flex;
  height: 1em;
  padding: 0.2em;
  margin: auto 0;
}
.checker {
  position: absolute;
  top: 0.2em;
  left: 0.2em;
}
</style>
