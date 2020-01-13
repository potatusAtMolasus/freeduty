<template>
  <section id="bannerSection">
    <div id="bannerContent">
      <carousel :autoplay="true" :loop="true" :autoplayTimeout="5000" :centerMode="true" :perPage="1" :paginationEnabled="false">
        <slide>
          <div class="banner-slide" style="background:#333">
            <img class="slide-photo" src="../../assets/017.jpg" />
          </div>
        </slide>
        <slide>
          <div class="banner-slide" style="background:#222">
            <img class="slide-photo" src="../../assets/017.jpg" />
          </div>
        </slide>
        <slide>
          <div class="banner-slide" style="background:#444">
            <img class="slide-photo" src="../../assets/017.jpg" />
          </div>
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

}
.slide-photo{
  width: 100%;
}
.VueCarousel-pagination{
  position: absolute;
  top: 100px;
  display: none;
}
</style>