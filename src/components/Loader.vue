<template>
  <!-- <div class="loader-back" :class="{'hidden': !show}"> -->
  <div class="loader-back" :class="{'hidden': !show}">
    <div class="svg-wrap">
      <svg class="svg-line" width="400" height="600" viewBox="0 0 100 100">
        <polyline
          class="line-cornered stroke-animation"
          points="15,0 -10,0 5,90 75,90 90,0 0,0"
          stroke-width="2"
          fill="none"
          stroke="red"
        />
      </svg>
      <svg class="svg-path" width="370" height="500" viewBox="0 0 100 100">
        <path
          class="path"
          width="200"
          d="M0,35
          A25,50 0 0,1 20,35
          A25,50 0 0,0 40,35
          A25,50 0 0,1 60,35
          A25,50 0 0,0 80,35
          A25,50 0 0,1 100,35
          A25,50 0 0,0 120,35
          A25,50 0 0,1 140,35"
          style="fill: none"
          stroke="red"
          stroke-width="2"
        />
      </svg>
      <svg class="svg-cubes" width="400" height="500" viewBox="0 0 100 100">
        <rect
          class="first-rect"
          x="50"
          y="50"
          width="10"
          height="10"
          stroke="red"
          stroke-width="2"
          fill="none"
          rx="1"
        />
        <rect
          class="second-rect"
          x="70"
          y="80"
          width="12"
          height="12"
          stroke="red"
          stroke-width="2"
          fill="none"
          rx="1"
        />
        <rect
          class="third-rect"
          x="20"
          y="80"
          width="10"
          height="10"
          stroke="red"
          stroke-width="2"
          fill="none"
          rx="1"
        />
        <rect
          class="fourth-rect"
          x="10"
          y="45"
          width="6"
          height="6"
          stroke="red"
          stroke-width="1.3"
          fill="none"
          rx="1"
        />
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  props: ['show'],
};
</script>

<style scoped>

.loader-back {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: #111;
  z-index: 500;
  overflow: visible;
  display: flex;
}
.loader-back.hidden{
  z-index: -100;
  visibility: hidden;
}
.svg-wrap {
  margin: auto;
  position: relative;
  transform: rotate(0.75);
}
svg {
  position: absolute;
}
.svg-line {
  overflow: visible;
  left: 25px;
}
.svg-path {
  position: relative;
  left: 0px;
  overflow: hidden;
  /* overflow: visible; */
}
.svg-cubes {
  position: absolute;
  left: 30px;
  animation: bounce 2s linear infinite 1s ;
}

path {
  position: relative;
  animation: wiggle 2s linear infinite;
}
.first-rect{
  transform: translate(10px, -10px) rotate(9deg);
}
.second-rect{
  transform: translate(7px, -20px) rotate(20deg);
}
.third-rect{
  transform: translate(80px, 10px) rotate(56deg);
}
.fourth-rect{
  transform: translate(40px, 10px) rotate(49deg);
}
@keyframes wiggle {
  0% {
    transform: translate(1px, 0px);
  }
  100% {
    transform: translate(-39px, 0px);
  }
}
@keyframes bounce {
  0% {
    top: 0px;
  }
  50% {
    top: 20px;
  }
  100% {
    top: 0px;
  }
}
@media (max-width: 576px) {
  .svg-line{
    width: 250px;
    height: 450px;
    left: 20px;
  }
  .svg-path{
    width: 236px;
    height: 350px;
    left: 0px;
  }
  .svg-cubes{
    width: 250px;
    height: 350px;
    left: 30px;
  }
}
</style>