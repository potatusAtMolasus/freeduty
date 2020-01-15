<template>
  <div class="loader-back">
    <!-- <svg width="200" height="200" viewBox="0 0 100 100"> -->
      <!-- <polyline
        class="line-cornered stroke-still"
        points="0,0 100,0 100,100"
        stroke-width="10"
        fill="none"
      /> -->
      <!-- <polyline
        class="line-cornered stroke-still"
        points="0,0 0,100 100,100 100,0 0,0"
        stroke-width="10"
        fill="none"
      /> -->
      <!-- <polyline
        class="line-cornered stroke-animation"
        points="0,0 100,0 100,100"
        stroke-width="10"
        fill="none"
      /> -->
      <!-- <polyline
        class="line-cornered stroke-animation"
        points="0,0 0,100 100,100 100,0 0,0"
        stroke-width="10"
        fill="none"
      /> -->


      <!-- <polyline
        class="line-cornered stroke-animation"
        points="15,0 -10,0 5,100 95,100 110,0 0,0"
        stroke-width="5"
        fill="none"
        stroke="#333"
      /> -->
      <!-- <path class="path"
            d="M-5,30
              A25,50 0 0,1 20,30
              A25,50 0 0,0 40,30
              A25,50 0 0,1 60,30
              A25,50 0 0,0 80,30
              A25,50 0 0,1 104,30
              L95,100
              L5,100
              L-5,30
              A25,50 0 0,1 20,30"
            style="fill: none"
            stroke="#333"
            stroke-width="5" />  -->
      <!-- <path class="path"
            d="M-5,30
              L95,100"
            style="fill: none"
            stroke="#333"
            stroke-width="5" />  -->


    <!-- </svg> -->
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
svg:hover path{
  d: path("M5,2 Q 8,5 5,8");
  /* d: path("M -5 30 A 25 50 0 0 1 20 30 A25 50 0 0 0 40 30 A 25 50 0 0 1 60 30 A 25 50 0 0 0 80 30 A 25 50 0 0 1 104 30 L 95 100 L5 100 L -5 30 A 25 50 0 0 1 20 30"); */

}
/* .path{
  d: path("M -5 30 A 25 50 0 0 1 20 30 A25 50 0 0 0 40 30 A 25 50 0 0 1 60 30 A 25 50 0 0 0 80 30 A 25 50 0 0 1 104 30 L 95 100 L5 100 L -5 30 A 25 50 0 0 1 20 30");
} */
.path.animate{
  animation: stroke-spacing 2s ease-in, stroke-color 8s linear;
  animation-iteration-count: infinite;
  animation-delay: 0;
  animation-direction: normal;
  animation-fill-mode: forwards;
  animation-play-state: running;
  transform-origin: center center;
}
.circle{
  transform: scale(1.25);
}
.circle.animate{
  animation: stroke-spacing 2s ease-in, stroke-color 8s linear;
  animation-iteration-count: infinite;
  animation-delay: 0;
  animation-direction: normal;
  animation-fill-mode: forwards;
  animation-play-state: running;
  transform-origin: center center;
}

.loader-back{
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  background: #111;
  z-index: 500;
  overflow: visible;
}

svg {
  overflow: visible;

  margin: auto;
  /* -webkit-transform: rotate(-45deg) scale(1); */
}

.stroke-still {
  stroke: #232323;
}

@keyframes stroke-spacing {
  0% {
    stroke-dasharray: 0 400;
  }
  45% {
    stroke-dashoffset: 0;
    stroke-dasharray: 400 400;
  }
  90% {
    stroke-dashoffset: -400;
    stroke-dasharray: 400 400;
  }
  100% {
    stroke-dashoffset: -400;
    stroke-dasharray: 400 400;
  }
}
@keyframes stroke-color {
  0%  { stroke: #3498DB; }
  24% { stroke: #643232; }
  25% { stroke: #327864; }
  49% { stroke: #327864; }
  50% { stroke: #32326e; }
  74% { stroke: #32326e; }
  75% { stroke: #78325a; }
  99% { stroke: #78325a; }
}
@keyframes fill-color {
  0%  { fill: #3498DB; }
  24% { fill: #643232; }
  25% { fill: #327864; }
  49% { fill: #327864; }
  50% { fill: #32326e; }
  74% { fill: #32326e; }
  75% { fill: #78325a; }
  99% { fill: #78325a; }
}
</style>