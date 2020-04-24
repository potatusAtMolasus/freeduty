<template>
  <div class="modal-wrap">
    <transition name="popup">
      <div v-if="showWarning" class="modal-window">
        <div id="modal-content-wrap">
          <div id="modal-title-wrap">
            <div id="circle">
              <!-- <h2>OK</h2> -->
              <h2>18+</h2>
            </div>
          </div>
          <div id="modal-msg-wrap">
            <div class="htmlContent">
              <p>Содержащаяся на сайте справочная информация об ассортименте алкогольной продукции не является
                предложением о приобретении и доводится до сведения посетителей в соответствии с требованиями
                Закона РФ от 07.02.1992 N 2300-1 'О защите прав потребителей' и Федерального закона от
                28.12.2009 N 381-ФЗ 'Об основах государственного регулирования торговой деятельности в
                Российской Федерации', с учетом ограничений, установленных Федеральным законом от 13.03.2006 N
                38-ФЗ 'О рекламе' (в редакции Федерального закона от 20.07.2012 N 119-ФЗ).</p>
              <h6 class="red_text">Исполнилось ли Вам полных 18 лет?</h6>
            </div>
          </div>
          <div id="modal-btns-wrap">
            <button class="confirm-btn" @click="ageConfirmed">
              <span>
               Да
              </span>
            </button>
            <button class="decline-btn" @click="ageDeclined">
              <span>
               Нет
              </span>
            </button>
            <!-- <button class="confirm-btn" @click="ageConfirmed">Мне исполнилось 18</button> -->
          </div>
        </div>
      </div>
    </transition>
    <transition name="fade">
      <div v-if="showWarning" class="modal-back"></div>
    </transition>
  </div>
</template>

<script>
import axios from "@/js/AxiosInstance.js";

export default {
  async created() {
    this.showWarning = !(await axios.post("is-age-confirmed", {headers: {
        'Content-Type': 'application/json',
      }})).data;
  },
  data() {
    return {
      showWarning: false
    };
  },
  methods: {
    async ageConfirmed(){
      await axios.post("confirm-age");
      this.showWarning = false;
    },
    ageDeclined(){
      window.location.replace("https://www.rosminzdrav.ru/documents/7870-prikaz-minzdravsotsrazvitiya-rossii-49-ot-19-yanvarya-2007-g");
    }
  }
};
</script>

<style scoped>
.red_text {
  color: #ff0000; cursor: auto;
  visibility: visible;
  box-sizing: border-box;
  padding: 0;
  font-family: roboto,Arial,sans-serif;
  font-weight: 400;
  font-style: normal;
  text-rendering: optimizeLegibility;
  line-height: 1.4;
  text-align: center!important;
  margin: 0 0 5px;
  clear: both;
  font-size: 1.125rem;
}

.modal-wrap {
  position: fixed;
  top: 0;
  width: 100vw;
  z-index: 99999999;
}

.modal-window {
  position: relative;
  top: 5vh;
  width: 35%;
  padding: 15px;
  margin: auto;
  border: 4px solid red;
  border-radius: 10px;
  background: #eee;
  color: black;
  box-shadow: #555 4px 4px 10px;
  z-index: 200;
}
/* .modal-window {
  position: relative;
  top: 20vh;
  width: 35%;
  padding: 15px;
  margin: auto;
  border: 4px solid white;
  background: #222;
  color: #ccc;
  box-shadow: #555 4px 4px 10px;
  z-index: 200;
} */
#modal-title-wrap{
  display: flex;
  justify-content: center;
}
#modal-title-wrap #circle{
  display: flex;
  width: 100px;
  height: 100px;
  margin: 10px 0 20px 0;
  padding: 20px;
  text-align: center;
  border: 3px solid;
  /* border: 3px solid red; */
  /* color: red; */
  border-radius: 50%;
}
#modal-title-wrap #circle h2 {
  font-weight: bold;
  margin: auto;
  text-align: center;
}
#modal-msg-wrap p {
  text-indent: 10px;
  text-align: justify;
}
#modal-btns-wrap{
  display: flex;
  justify-content: center;
  height: 25px;
  margin-bottom: 20px;
}
.confirm-btn{
  padding: 18px 40px;
  margin: 0 0 10px 0;
  /* background: linear-gradient(180deg, white 5%, green 150%); */
  /* border-radius: 30px; */
  border: 1px solid red;
  font-size: 18px;
  position: relative;
  transition: color .3s;
}
.confirm-btn:after{
  content: '';
  display: block;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0px;
  transition: height .3s;
  background: red;
  z-index: 100;
}
.confirm-btn span{
  position: relative;
  z-index: 200;
  bottom: 10px;
}
.confirm-btn:hover:after{
  height: 100%;
}
.confirm-btn:hover{
  color: white;
}

.decline-btn{
  padding: 18px 40px;
  margin: 0 0 10px 100px;
  /* background: linear-gradient(180deg, white 5%, green 150%); */
  /* border-radius: 30px; */
  border: 1px solid red;
  font-size: 18px;
  position: relative;
  transition: color .3s;
}
.decline-btn:after{
  content: '';
  display: block;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0px;
  transition: height .3s;
  background: red;
  z-index: 100;
}
.decline-btn span{
  position: relative;
  z-index: 200;
  bottom: 10px;
}
.decline-btn:hover:after{
  height: 100%;
}
.decline-btn:hover{
  color: white;
}
/* .confirm-btn:hover{
  background: linear-gradient(180deg, white 0%, green 130%);
}
.confirm-btn:active{
  background: linear-gradient(180deg, white -5%, green 110%);
} */


.popup-enter,
.popup-leave-to {
  top: -100vh;
}
.popup-enter-active,
.popup-leave-active {
  transition: top 0.5s;
}

.modal-back {
  position: fixed;
  top: 0;
  width: 100vw;
  height: 100vh;
  background: #555;
  opacity: 0.55;
  z-index: 100;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}


@media(max-width: 1000px){
  .modal-window {
    width: 80%;
    box-sizing: border-box;
  }
}
@media(max-width: 750px){
  .modal-window {
    width: 88%;
  }
}
@media(max-width: 500px){
  .modal-window {
    width: 96%;
  }
}
</style>