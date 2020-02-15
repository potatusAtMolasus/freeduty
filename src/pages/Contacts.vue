<template>
  <div id="contactsPage" :class="{'padded-top': scrollPosition !== 0}">
    <div class="container">
      <div class="title-section">
        <div class="title-wrap">
          <h2 class="title">Контакты</h2>
          <span class="line"></span>
        </div>
      </div>
      <div class="content">
        <h3>
          Телефон:
          <a href="tel:+79891638833">+7 989 163-88-33</a>
        </h3>
        <h3>Адрес: ул. Каспийская 37 б, Адлер</h3>
        <iframe
          id="iframe"
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2897.996714018324!2d39.96155895092463!3d43.41889537546576!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40f59542541b0d5b%3A0x3670c24a10b533ed!2z0YPQuy4g0JrQsNGB0L_QuNC50YHQutCw0Y8sIDM30LEsINCh0L7Rh9C4LCDQmtGA0LDRgdC90L7QtNCw0YDRgdC60LjQuSDQutGA0LDQuSwgMzU0Mzgz!5e0!3m2!1sru!2sru!4v1579003238768!5m2!1sru!2sru"
          height="450"
          frameborder="0"
          style="border:0;"
          allowfullscreen
        ></iframe>
      </div>
    </div>
  </div>
</template>

<script>
export default {  
  props:{
    scrollPosition: Number
  },
};
</script>

<style scoped>
#contactsPage {
  background-image: url("../assets/patternBlack.png");
}
#contactsPage .container {
  background: rgba(180, 180, 180, 0.9);
  padding: 3em 0;
}
#contactsPage.padded-top .container{
  padding-top: 15em;
}
#iframe {
  width: 100%;
  z-index: 200;
  min-height: 40vh;
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
  padding: 0.25em 18em 0.25em 6em;
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
  width: 6em;
  position: absolute;
  right: 0;
  top: 0;
  display: block;
  clip-path: polygon(70% 0, 100% 0, 100% 100%, 0 100%);
}
.content{
  padding: 0 3em;
}
@media(max-width: 776px){
  .content{
    padding: .1em;
  }
  .title-wrap{
    padding: 0.25em 11.5em 0.25em 2em;
  }
  .line{
    width: 4.3em;
    clip-path: polygon(70% 0, 100% 0, 100% 100%, 0 100%);
  }
  #contactsPage.padded-top .container {
    padding-top: 3em;
  }
}
</style>