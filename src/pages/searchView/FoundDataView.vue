<template>
  <main>
    <div id="wrap">
      <div v-for="i in data" :key="i.id">
        <item :item="i"></item>
      </div>
    </div>
  </main>
</template>

<script>
import Item from "@/components/Item.vue";

export default {
  props: {
    data: Array
  },
  components: {
    Item,
  }
}
</script>
<style scoped>
main{
  flex: 3;
  margin: 0 2em 0 0;
  background-color: #ccccccee;
}
.outer-wrap{
  margin: .5em .5em;
}
#wrap{
  padding: 1em;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-gap: 0em;
}
</style>