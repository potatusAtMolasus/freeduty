<template>
  <main id="aboutPage">
    <div class="wrapper">

      <div class="content">
        <div id="about-text">
          <p>Нашей целью с первых дней существования было формирование культуры потребления алкоголя в нашем крае. Ориентируясь на правильный вкус наших клиентов и профессиональные рекомендации, мы подобрали уникальный ассортимент вин и спиртных напитков.</p>
          <p>Ассортимент «Дьюти Фри» насчитывает около 3000 алкогольных напитков со всего мира — от демократичных бестселлеров до мировых звезд, отмеченных престижными рейтингами. Благодаря тому, что мы напрямую сотрудничаем с ведущими импортерами, цены для вас мы постарались сделать максимально низкими.</p>
          <p>Компания стремиться, чтобы в каждой ценовой категории были представлены вина и напитки с оптимальным соотношением цены и качества, и предоставляет высокий уровень сервиса для наших клиентов.</p>
          <p>Наши напитки обладают безупречной репутацией и пользуются заслуженным признанием потребителей. Наши клиенты своим постоянством подтверждают высокое качество продукции и отличные условия сотрудничества.</p>
          <p>У нас вы можете заказать напитки, не представленные в каталоге, мы сделаем все возможное, чтобы вы получили удовольствие и радость, наслаждаясь своим выбором и хорошим вкусом!</p>
        </div>
        <!-- <img id="about-image" src="../assets/009.jpg" /> -->
        <div class="image-section">
          <div class="image-wrap">
            <img id="about-image" src="../assets/0290.jpg" />
          </div>
        </div>
      </div>

      <div class="table-wrap">
        <table style="margin-left: auto; margin-right: auto;">
          <tbody>
            <tr v-for="row in table" :key="row.name">
              <td>
                <div>{{ row.name }}</div>
              </td>
              <td>
                <div>{{ row.value }}</div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  props: {
    scrollPosition: Number
  },
  data() {
    return {
      table: [
        {
          name: "Полное наименование",
          value: "Общество с ограниченной ответственностью «ДЬЮТИ ФРИ СОЧИ»"
        },
        { name: "Сокращенное наименование", value: "ООО «ДЬЮТИ ФРИ СОЧИ»" },
        {
          name: "Юридический адрес",
          value: "354340, г. Сочи, ул. Каспийская 37Б, 1 этаж"
        },
        {
          name: "Адрес фактический",
          value: "354340, г. Сочи, ул. Каспийская 37Б, 1 этаж"
        },
        { name: "ОГРН", value: "1192375045268" },
        { name: "ИНН", value: "2367009900" },
        { name: "КПП", value: "236701001" },
        { name: "Лицензия", value: "№23РПА0019263 от 24.09.2019 г." },
        { name: "Расчетный счет", value: "40702810326260000514" },
        { name: "БАНК", value: 'ФИЛИАЛ "РОСТОВСКИЙ" АО "АЛЬФА-БАНК"' },
        { name: "Корреспондентский счет", value: "30101810500000000207" },
        { name: "БИК", value: "046015207" },
        { name: "Генеральный директор", value: "Демирчян Аревик Сетраковна" }
      ]
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Alegreya|Comfortaa|Nunito|Open+Sans+Condensed:300|Pacifico&display=swap");
main {
  background-color: #fbf8f8;
}
#aboutPage {
  background-image: url("../assets/patternBlack.png");
  background-size: 300px;
}
.wrapper {
  width: 100%;
}
.content {
  position: relative;
}
#aboutPage.padded-top .wrapper {
  padding-top: 13em;
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
#about-text {
  position: absolute;
  z-index: 100;
  right: 2em;
  float: right;
  top: 2em;
  padding: 1.3em;
  font-size: 1.18em;
  color: white;
  background: #000e;
  width: 65%;
}
#about-text p {
  /* font-family: 'Open Sans Condensed', sans-serif; */
  /* font-family: 'Nunito', sans-serif; */
  /* font-family: 'Pacifico', cursive; */
  /* font-family: 'Comfortaa', cursive; */
  font-family: "Alegreya", serif;
  text-align: justify;
  text-indent: 3em;
}
#about-text p::first-letter {
  font-size: 1.3em;
  padding-right: 0.1em;
  font-family: "Pacifico", cursive;
  color: red;
}
.image-section {
  position: relative;
  top: 0;
  /* top: 50em; */
}
.image-wrap {
  position: relative;
  /* top: -32em; */
  z-index: 0;
}
#about-image {
  width: 100%;
  /* position: absolute; */
}
.table-wrap {
  margin: auto;
  width: 87%;
  /* padding: 3em 0 1.25rem 0; */
  padding-bottom: 1.25em
}
table {
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  background: rgba(180, 180, 180, 0.6);
  width: 100%;
  table-layout: fixed;
  overflow-wrap: break-word;
}

td,
th {
  padding: 1em;
  border: 1px solid #cccc;
  text-align: left;
  background: rgb(255, 247, 247);
  background: linear-gradient(
    180deg,
    rgba(255, 247, 247, 1) 13%,
    rgba(226, 243, 246, 1) 79%
  );
}
@media(max-width: 1500px){
  #about-text{
    width: 56%;
    box-sizing: border-box;
  }
}
@media(max-width: 1300px){
  #about-text{
    top: 4em;
  }
}
@media(max-width: 1300px){
  #about-text{
    width: 75%;
  }
}
@media(max-width: 1050px){
  #about-text{
    right: unset;
    margin: auto;
    width: 100%;
    font-size: 1em;
  }
}
@media(max-width: 776px){
  .image-section{
    display: none;
  }
  #about-text{
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    box-sizing: border-box;
  }
  #about-text{
    padding: .4em;
  }
  .title-wrap{
    padding: 0.25em 6em;
  }
  .line{
    width: 3.5em;
    clip-path: polygon(65% 0, 100% 0, 100% 100%, 0 100%);
  }
  #aboutPage.padded-top .wrapper {
    padding-top: 3em;
  }
  .table-wrap{
    width: 100%;
    padding-bottom: 0;
  }
}
</style>