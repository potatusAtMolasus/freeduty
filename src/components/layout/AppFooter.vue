<template>
  <footer>
    <div id="footerContent">
      <div id="mainFooterContent" class="wide-container">
        <div id="footerCategories">
          <ul>
            <li v-for="i in categories" :key="i.url">
              <router-link :to="i.url">{{i.label}}</router-link>
            </li>
          </ul>
        </div>
        <div id="footerMenu">
          <ul>
            <li v-for="i in links" :key="i.url">
              <router-link :to="i.url">{{i.label}}</router-link>
            </li>
          </ul>
        </div>
        <div id="socialLinks">
          <!-- <h3>Мы в соц сетях</h3> -->

          <div id="social-buttons">
            <ul class="social">
              <!-- <li>
                <a href="#">
                  <i class="fa fa-facebook" aria-hidden="true"></i>
                </a>
              </li>
              <li>
                <a href="#">
                  <i class="fa fa-twitter" aria-hidden="true"></i>
                </a>
              </li> -->
              <li>
                <a href="#">
                  <i class="fa fa-instagram" aria-hidden="true"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div id="franchaise" class="container">
        <a class="franchaise-wrap" href="#">
          <p>Франшиза</p>
        </a>
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
#social-buttons li a{
  color: rgba(167, 146, 129, 0.6);
}
#social-buttons li {
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
#footerMessage p {
  font-size: 1.6em;
  text-align: center;
  color: #aaa;
  text-transform: uppercase;
  margin: auto;
}
#franchaise {
  width: 100%;
  display: flex;
  margin-bottom: 2em;
}
.franchaise-wrap {
  margin: auto;
  background: red;
  padding: 1em 3em;
}
.franchaise-wrap a {
  text-transform: uppercase;
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
  #footerMenu ul {
    margin: 0;
    padding: 5px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  #footerMenu ul li {
    flex: 1 0 31%;
  }
  #mainFooterContent {
    display: block;
  }
  #footerCategories {
    border-right: none;
  }
  #footerMenu {
    display: none;
  }
  #social-buttons {
    display: flex;
    justify-content: center;
    text-align: center;
  }
  #franchaise.container {
    padding: 0;
  }
  #rights {
    padding: 0;
  }
}
</style>