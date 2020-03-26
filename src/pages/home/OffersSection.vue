<template>
    <section id="offersSection">
        <div class="wide-container">
            <!-- <h2 id="offers-title">Наши Акции</h2> -->

            <div id="offersContent">
                <div id="offersWrap">
                    <div class="mobile_wrapper">
                        <div class="title-section">
                            <h2 class="title">Акции</h2>
                        </div>
                        <carousel id="cor"
                                  :autoplay="true"
                                  :loop="true"
                                  :scrollPerPage="false"
                                  :centerMode="true"
                                  :perPage="perPage"
                                  :paginationEnabled="false"
                                  :navigationEnabled="true"
                                  :paginationColor="'#454545'"
                                  :autoplayTimeout="2500"
                        >
                            <slide v-for="i in homeOffers" :key="i.id">
                                <item :item="i"></item>
                            </slide>
                        </carousel>
                    </div>
                    <div class="allOffers show-for-small-only">
                        <div class="watchOffersWrap">
                            <router-link class="offersBtn" to="/offers">
                      <span>
                        все акции
                      </span>
                            </router-link>
                        </div>

                        </div>
                    <div id="offersText">Ассортимент «Дьюти Фри» насчитывает около 3000 алкогольных напитков со всего
                        мира — от демократичных бестселлеров до мировых звезд, отмеченных престижными рейтингами.
                        Благодаря тому, что мы напрямую сотрудничаем с ведущими импортерами, цены для вас мы постарались
                        сделать максимально низкими.
                    </div>
                </div>
            </div>
        </div>
        <div class="disignWrapper hide-for-small-only">
        <div class="allOffers">
            <div class="triangle leftTop"></div>
            <div class="triangle leftBottom"></div>
            <div class="triangle rightTop"></div>
            <div class="triangle rightBottom"></div>
        </div>
            <div class="watchOffersWrap">
                <router-link  class="offersBtn" id="offersBtn" to="/offers">
                      <span>
                        все акции
                      </span>
                </router-link>
            </div>
        </div>
    </section>
</template>

<script>
    import Item from "@/components/Item.vue";

    export default {
        name: "OffersSection",
        props: {
            isMobile: Boolean,
            homeOffers: Array
        },
        components: {
            Item
        },
        computed: {
            perPage() {
                return this.isMobile ? 2 : 3;
            }
        }
    };
</script>
<style scoped>
    #cor {
        box-sizing: border-box;
        padding: 0;
        padding-left: 0;
        padding-right: .625rem;
        float: left;
        width: 75%;
        min-height: 1px;
        /* height: 357px; */
        margin: -5px;
        position: relative;
        /* z-index: 5; */
    }


    .allOffers {
        z-index: -1;
        background: red;
        max-width: 1060px;
        height: 84px;
        margin: 0 auto;
        position: relative;
    }

    .allOffers .triangle.leftTop {
        border-top: 41px solid red;
        border-left: 21px solid transparent;
        top: 0;
        right: 100%;
    }

    .allOffers .triangle.rightTop {
        border-top: 41px solid red;
        border-right: 21px solid transparent;
        top: 0;
        left: 100%;
    }

    .allOffers .triangle.rightBottom {
        border-bottom: 41px solid red;
        border-right: 21px solid transparent;
        bottom: 0;
        left: 100%;
    }

    .allOffers .triangle {
        width: 0;
        height: 0;
        position: absolute;
    }

    .allOffers .triangle.leftBottom {
        border-bottom: 41px solid red;
        border-left: 21px solid transparent;
        bottom: 0;
        right: 100%;
    }

    .title-section {
        width: 100%;
        display: flex;
        overflow: hidden;
        position: relative;
    }

    .show-for-small-only {
        display: none;
    }

    .title-section .title-wrap {
        background: black;
        direction: inline-block;
        padding: 0.25em 18em 0.25em 6em;
        clip-path: polygon(0 0, 100% 0, 85% 100%, 0 100%);
        position: relative;
        left: -1em;
        display: flex;
    }

    .title {
        font-size: 1.75rem;
        font-weight: normal;
        text-transform: uppercase;
        color: #000;
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
        font-family: roboto, Arial, sans-serif;
    }

    .line {
        background: red;
        height: 100%;
        width: 6em;
        position: absolute;
        right: 0;
        top: 0;
        display: block;
        clip-path: polygon(80% 0, 100% 0, 100% 100%, 0 100%);
    }

    .inner .title-wrap span {
        width: 50%;
        display: block;
        margin: auto;
        background: #333c;
        padding: 1em;
        color: #ccc;
    }

    #offersSection {
        overflow: hidden;
        background: #e9e9e9 url('../../assets/patternWhite.png') repeat center -638px;
        background-size: 300px;
        position: relative;
        z-index: 200;
    }

    /* #offersSection .wide-container{} */
    #offersContent {
        justify-content: space-between;
    }

    #offersWrap {
        padding: 0em 3em 0em 3em;;
        flex: 3;
        overflow: hidden;

    }

    .disignWrapper {
        top: -80px;
        position: relative;
    }

    #offersText {
        flex: 0.9;
        background: black;
        line-height: 1.5em;
        font-size: .9375rem;
        font-style: italic;
        color: #fff;
        position: relative;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        padding-top: .625rem;
        padding-left: .625rem;
        padding-right: .625rem;
        float: left;
        width: 25%;
        height: 357px;
        min-height: 1px;
        top: -35px;
        left: 30px;
    }

    .watchOffersWrap {
        top: -50px;
        position: relative;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
        margin-top: 0;
        margin-bottom: 0;
        max-width: 1060px;
    }

    .offersBtn {
        top: -25px;
        right: 170px;
        text-decoration: none;
        color: #ffffff;
    }

    .offersBtn {
        float: right;
        padding: 3px 4px;
        margin: 20px 0 10px 0;
        /*background: linear-gradient(180deg, #bbb 5%, #E9E9E9 150%);*/
        /* border-radius: 30px; */
        border: 1px solid #ffffff;
        font-size: 18px;
        position: relative;
        transition: color .3s;
        /* text-decoration: 2px underline dotted red; */
    }

    .offersBtn:after {
        content: '';
        display: block;
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 0px;
        transition: height .3s;
        background: #222;
        z-index: 100;
    }

    .offersBtn span {
        font-size: .9em;
        position: relative;
        z-index: 200;
    }

    .offersBtn:hover:after {
        height: 100%;
    }

    .offersBtn:hover {
        color: white;
    }

    .wide-container {
        max-width: 960px;
        width: 100%;
        margin-right: auto;
        margin-left: auto;
    }

    @media (max-width: 800px) {

        .watchOffersWrap {
            margin: 26px auto 0;
            display: inline-block;
            justify-content: center;
            top: 0;
            position: relative;
            width: unset;
            margin-left: unset;
            margin-right: unset;
            margin-bottom: unset;
            max-width: unset;
        }

        .offersBtn {
            -webkit-box-direction: normal;
            font-style: normal;
            line-height: 1.5;
            font-weight: 400;
            font-family: "Roboto", sans-serif;
            top: -25px;
            right: 170px;
            text-decoration: none;
            color: #ffffff;
            padding: 3px 4px;
            border: 1px solid #ffffff;
            font-size: 18px;
            position: static;
            transition: color .3s;
            margin: 0;
            display: inline-block;
            float: none;
        }
        .mobile_wrapper {
            padding-left: .625rem;
        }

        .allOffers {
            top:-35px;
            text-align: center;
        }

        .show-for-small-only {
            display: block;
            color: #222;
            font-style: normal;
            line-height: 1.5;
            z-index: 1;
            cursor: auto;
            font-family: roboto, Arial, sans-serif;
            font-size: 1rem;
            font-weight: 400;
            box-sizing: border-box;
            padding: 0;
            display: inherit !important;
            background: red;
            max-width: 1060px;
            height: 84px;
            margin: 0 auto;
            position: relative;
            width: 100%;
            float: left;
            margin-top: 20px;
        }

        .hide-for-small-only {
            display: none;
        }

        #cor {
            width: 100%;
            margin: 0;
        }

        .wide-container {
            padding: 0;
        }

        #offersWrap {
            padding: 0;
        }

        #offersContent {
            font-size: 0.8em;
            display: block;
        }

        #offersText {
            width: 100%;
            box-sizing: border-box;
            padding-top: 20px;
            /* padding-bottom: 0px; */
            margin-bottom: 20px;
            max-height: 200px;
            width: 100%;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            height: auto;
            padding-bottom: 20px;
            font-size: 1em;
            left: unset;
        }
    }

    @media (max-width: 500px) {

        .offersBtn {
            -webkit-box-direction: normal;
            font-style: normal;
            line-height: 1.5;
            font-weight: 400;
            font-family: "Roboto", sans-serif;
            top: -25px;
            right: 170px;
            text-decoration: none;
            color: #ffffff;
            padding: 3px 4px;
            border: 1px solid #ffffff;
            font-size: 18px;
            position: static;
            transition: color .3s;
            margin: 0;
            display: inline-block;
            float: none;
        }

        .allOffers {
            text-align: center;
            top: -35px;
        }

        .mobile_wrapper {
            padding-left: .625rem;
        }

        .show-for-small-only {
            display: block;
            color: #222;
            font-style: normal;
            line-height: 1.5;
            cursor: auto;
            font-family: roboto, Arial, sans-serif;
            font-size: 1rem;
            font-weight: 400;
            box-sizing: border-box;
            padding: 0;
            display: inherit !important;
            background: red;
            max-width: 1060px;
            height: 84px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
            width: 100%;
            float: left;
            margin-top: 20px;
        }

        .hide-for-small-only {
            display: none;
        }

        #cor {
            width: 100%;
            margin: 0;
        }

        #offersContent {
            font-size: 0.8em;
            display: block;
        }

        #offersText {
            width: 100%;
            box-sizing: border-box;
            padding-top: 20px;
            /* padding-bottom: 0px; */
            margin-bottom: 20px;
            max-height: 200px;
            width: 100%;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            height: auto;
            padding-bottom: 20px;
            font-size: 1em;
            left: unset;
        }

        #offersWrap {
            padding: 0;
        }

        .watchOffersWrap {
            margin: 26px auto 0;
            display: inline-block;
            justify-content: center;
            top: 0;
            position: relative;
            width: unset;
            margin-left: unset;
            margin-right: unset;
            margin-bottom: unset;
            max-width: unset;
        }

        #offers-title {
            background: #424141eb;
            margin: auto;
            padding: 1em;
        }

    }

    @media (max-width: 950px)  and (min-width: 800px){
        #cor {
            width: 66.66%;

        }

        #offersText {
            width: 33.33%;
        }

    }

</style>