<template>
  <footer>
    <div id="footerContent">
      <div id="mainFooterContent" class="wide-container">
        <div id="footerMenu">
          <ul>
            <li>Режим работы:11:00 - 22:00</li>
            <li>+7 (989) 163-88-33</li>
            <li>г. Сочи, ул. Каспийская, 37б</li>
          </ul>
        </div>
        <div id="socialLinks">
          <div id="social-buttons">
            <ul class="social">
              <a href="https://www.instagram.com/dutyfree_sochi/">
              <li>
                  <i class="fa fa-instagram" aria-hidden="true"></i>
              </li>
              </a>
            </ul>
          </div>
        </div>
      </div>

      <div id="rights" class="container">
        <p>Duty Free © Все права защищены 2020</p>
      </div>
    </div>
    <div>
    <div id="footerInfoMessage">
      <p>Ресурс <a href="http://dutyfreesochi.ru/">dutyfreesochi.ru</a> не занимается дистанционной реализацией алкогольной продукции в Сочи.<br>
        Товары, представленные в сети DUTY FREE можно приобрести с 11:00 до 22:00 только в специализированном магазине.<br>
        Доставка алкогольной продукции не предусмотрена!</p>
    </div>
    <div id="footerMessage">
      <p>ЧРЕЗМЕРНОЕ УПОТРЕБЛЕНИЕ АЛКОГОЛЯ ВРЕДИТ ВАШЕМУ ЗДОРОВЬЮ</p>
    </div>
    </div>
  </footer>
</template>

<script>
export default {
  props: {
    links: Array,
    categories: Array
  },
  name: "MainHeader"
};
</script>

<style scoped>
a {
  color: #ccc;
}
li {
  margin: 10px 0;
  cursor: pointer;
  transition: ease 0.3s;
}
#footerContent {
  /* clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%); */
  background-color: #222;
  color: #ccc;
}
#mainFooterContent {
  display: flex;
  justify-content: space-between;
  padding: 2.5em 0 2.2em 0;
}

#footerCategories {
  flex: 5;
}
#footerCategories,
#footerMenu {
  text-align: right;
}
#footerMenu {
  flex: 4;
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
#social-buttons li a{
  color: rgba(167, 146, 129, 0.6);
}
#social-buttons li {
  /* font-size: 100px; */
  font-size: 60px;
  list-style-type: none;
  /* width: 100px; */
  width: 60px;
  /* height: 100px; */
  height: 60px;
  line-height: 50px;
  padding: 1%;
  /* border: 1px solid rgba(167, 146, 129, 0.4); */
  cursor: pointer;
  margin: auto 10px;
  transition: ease 0.3s;
}
#social-buttons li:hover {
  color: #a79281;
  /* border: 1px solid #a79281; */
}
.social:hover > li,
ul:hover li {
  opacity: 0.5;
}
.social:hover > li:hover,
ul:hover li:hover {
  opacity: 1;
}

#rights {
  display: flex;
}
#rights p {
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
#footerInfoMessage {
  background-color: black;
}

#footerInfoMessage p {
  text-align: center;
  color: #aaa;
  margin: auto;
}


#footerMessage p {
  font-size: 1.6em;
  text-align: center;
  color: #aaa;
  text-transform: uppercase;
  margin: auto;
}
@media (max-width: 800px) {
  #footerContent {
    padding-right: 15px;
    padding-left: 15px;
  }
  #footerMessage p {
    font-size: 1.1em;
  }
  #footerCategories ul {
    margin: 0 0 30px 0;
    padding: 5px 20px;
    display: block;
    text-align: center;
  }
  #footerCategories ul li {
    margin: 5px 10px;
    display: inline-block;
  }
  /*#footerMenu ul {*/
  /*  margin: 0;*/
  /*  padding: 5px;*/
  /*  display: flex;*/
  /*  justify-content: space-between;*/
  /*  flex-wrap: wrap;*/
  /*}*/
  #footerMenu {
    text-align: center;
  }
  #mainFooterContent {
    display: block;
  }
  #footerCategories {
    border-right: none;
  }

  #social-buttons {
    display: flex;
    justify-content: center;
    text-align: center;
  }
  #rights {
    padding: 0;
  }
}
</style>