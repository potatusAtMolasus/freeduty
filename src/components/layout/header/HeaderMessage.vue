<template>
  <div id="HeaderMessage" :class="{'no-height': scrollPosition>0}">
    <p>Tommodi repellat. Voluptatum corporis consequuntur, fugiat quae libero, assumend porro ab</p>
    <p>A labore explicabo aliquam mollitia similique 8:12 safa 12:23 quasi debitis rem quod nobis. Consequuntur, quisquam.</p>
    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad facilis voluptates deserunt voluptate</p>
  </div>
</template>

<script>
export default {
  props:{
    scrollPosition: Number
  }
}
</script>

<style>
/* Стили для предупреждения */
#HeaderMessage {
  box-sizing: border-box;
  overflow: hidden;
  padding: 1.1em;
  background: black;
  transition: all 0.2s;
  height: 6em;
}
#HeaderMessage.no-height {
  height: 0;
  margin: 0;
  padding: 0;
}
#HeaderMessage p {
  line-height: 1.5em;
  font-size: 0.9em;
  text-align: center;
  margin: 0;
  color: white;
}

@media only screen and (max-device-width: 480px) {
  body {
    -ms-text-size-adjust: 100%;
    -moz-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
  }
}

@media(max-width: 700px){
  #HeaderMessage p {
    font-size: 0.8em;
  }
  #HeaderMessage {
    padding: .1em;
    height: auto;
  }
}
@media(max-width: 500px){
  #HeaderMessage p {
    font-size: 0.7em;
  }
  #HeaderMessage {
    padding: .1em;
    height: auto;
  }
}
</style>