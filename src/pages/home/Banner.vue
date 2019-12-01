<template>
  <section id="bannerSection">
    <div id="bannerContent">
      <carousel :autoplay="true" :loop="true" :autoplayTimeout="5000" :centerMode="true" :perPage="1" :paginationEnabled="false">
        <slide>
          <div class="banner-slide" style="background:#333"></div>
        </slide>
        <slide>
          <div class="banner-slide" style="background:#222"></div>
        </slide>
        <slide>
          <div class="banner-slide" style="background:#444"></div>
        </slide>
      </carousel>
    </div>
  </section>
</template>

<script>
export default {};
</script>
<style scoped>
#bannerContent{
  background: black;
}
.banner-slide{
  height: 100vh;
}
.VueCarousel-pagination{
  position: absolute;
  top: 100px;
  display: none;
}
</style>