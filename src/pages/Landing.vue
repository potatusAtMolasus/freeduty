<template>
  <main>
    <div id="wrapper">
      <div id="landingWrapper">
        <div id="logo">
          <div id="logoWrap">
            <img src="../assets/logo.png" id="logo" />
          </div>
        </div>
        <div id="contacts">
          <p id="phone">
            <span>
              <i class="fa fa-phone"></i> +7 989 163-88-33
            </span>
          </p>
          <p id="address">
            <span>
              <i class="fa fa-map-marker"></i> ул. Каспийская 37 б, Адлер
            </span>
          </p>
        </div>
      </div>
      <iframe
				id="iframe"
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2897.996714018324!2d39.96155895092463!3d43.41889537546576!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40f59542541b0d5b%3A0x3670c24a10b533ed!2z0YPQuy4g0JrQsNGB0L_QuNC50YHQutCw0Y8sIDM30LEsINCh0L7Rh9C4LCDQmtGA0LDRgdC90L7QtNCw0YDRgdC60LjQuSDQutGA0LDQuSwgMzU0Mzgz!5e0!3m2!1sru!2sru!4v1579003238768!5m2!1sru!2sru"
        height="450"
        frameborder="0"
        style="border:0;"
        allowfullscreen
      ></iframe>
    </div>
  </main>
</template>

<script>
export default {
  mounted() {}
};
</script>

<style scoped>
main {
  background-color: black;
  width: 100%;
  min-height: 100vh;
  display: inline-flex;
  justify-content: center;
	box-sizing: border-box;
}
#landingWrapper:before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: linear-gradient(
      180deg,
      rgba(65, 65, 65, 0.15),
      rgba(0, 0, 0, 0.25)
    ),
    linear-gradient(
      30deg,
      rgba(65, 65, 65, 0.397),
      rgba(65, 65, 65, 0.1) 50%,
      rgba(65, 65, 65, 0.226) 50%,
      rgba(65, 65, 65, 0)
    );
  z-index: 100;
}
#wrapper{
	width: 100%;
}
#landingWrapper {
  display: flex;
  justify-content: center;
  flex-direction: column;
	position: relative;
}

#logo {
  width: 450px;
	margin: 3em auto auto auto;
}
#logoWrap {
  margin: 10px;
  width: 100%;
}
#logoWrap img {
  width: 100%;
}
#contacts {
  color: white;
  display: flex;
  flex-direction: column;
	width: 450px;
	margin: 4em auto 5em auto;
}
#phone,
#address {
  margin: 3px;
  font-size: 2em;
  text-shadow: red 2px 2px 8px;
}
/* #phone{} */
/* #address{} */
#iframe{
	width: 100%;
	z-index: 200;
}
@media (max-width: 500px) {
  #logo {
    width: 350px;
  }
  #address {
    font-size: 1.2em;
  }
  #phone {
    font-size: 1.2em;
  }
}
</style>