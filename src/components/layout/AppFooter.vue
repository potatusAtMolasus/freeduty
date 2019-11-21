<template>
  <footer>
    <div id="footerContent">
      <div id="mainFooterContent" class="wide-container">
        <div id="footerCategories">
          <ul>
            <li>Категория 1</li>
            <li>Категория 3</li>
            <li>Категория 2</li>
            <li>Категория 4</li>
            
          </ul>
        </div>
        <div id="footerMenu">
          <ul>
            <li>Главная</li>
            <li>О нас</li>
            <li>Адреса</li>
            <li>Акции</li>
            <li>Блог</li>
            <li>Корпоративным клиентам</li>
          </ul>
        </div>
        <div id="socialLinks">
          <h3>Social links</h3>

          <div id="social-buttons">
            <ul class="social">
              <li>
                <i class="fa fa-facebook" aria-hidden="true"></i>
              </li>
              <li>
                <i class="fa fa-twitter" aria-hidden="true"></i>
              </li>
              <li>
                <i class="fa fa-instagram" aria-hidden="true"></i>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div id="rights" class="container">
        <p>Duty Free © Все права защищены 2019</p>
      </div>
    </div>
    <div id="footerMessage">
      <!-- <p>Чрезмерное употребление алкоголя вредит вашему здоровью</p> -->
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, amet!</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "MainHeader"
};
</script>

<style scoped>
li{
  margin: 10px 0;
  cursor: pointer;
  transition: ease 0.3s;
}
#footerContent {
  /* clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%); */
  background-color: #222;
  color: #ccc;

}
#mainFooterContent{
  display: flex;
  justify-content: space-between;
  padding: 2.5em 0 2.2em 0;
}

#footerCategories {
  flex: 5;
}
#footerCategories,
#footerMenu {
  border-right: 1px solid #686868;
}
#footerMenu {
  flex: 7;
}
#socialLinks {
  flex: 4;
  padding: 0 3em;
}

#social-buttons {
  text-align: center;
  font-size: 30px;
}

#social-buttons .social {
  display: flex;
  padding-left: 0;
}
#social-buttons li {
  color: rgba(167, 146, 129, 0.6);
  list-style-type: none;
  width: 50px;
  height: 50px;
  line-height: 50px;
  padding: 1%;
  border: 1px solid rgba(167, 146, 129, 0.4);
  cursor: pointer;
  margin: auto 10px;
  transition: ease 0.3s;
}
#social-buttons li:hover {
  color: #a79281;
  border: 1px solid #a79281;
}
.social:hover > li, ul:hover li {
  opacity: 0.5;
}
.social:hover > li:hover, ul:hover li:hover {
  opacity: 1;
}

#rights{
  display: flex;
}
#rights p{
  margin: auto;
  text-align: center;
  font-size: 1.08em;
  line-height: 2em;
}

#footerMessage {
  background-color: black;
  height: 70px;
  display: flex;
}
#footerMessage p {
  font-size: 1.6em;
  text-align: center;
  color: #aaa;
  text-transform: uppercase;
  margin: auto;
}
</style>