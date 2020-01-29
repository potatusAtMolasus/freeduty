<template>
    <div id="contacts-page">
        <div id="contacts-containers">
            <h1 id="contacts-title">Контакты</h1>
            <h3>Телефон: <a href="tel:+79891638833">+7 989 163-88-33</a></h3>
            <h3>Адрес: ул. Каспийская 37 б, Адлер</h3>
            <iframe
                    id="iframe"
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2897.996714018324!2d39.96155895092463!3d43.41889537546576!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40f59542541b0d5b%3A0x3670c24a10b533ed!2z0YPQuy4g0JrQsNGB0L_QuNC50YHQutCw0Y8sIDM30LEsINCh0L7Rh9C4LCDQmtGA0LDRgdC90L7QtNCw0YDRgdC60LjQuSDQutGA0LDQuSwgMzU0Mzgz!5e0!3m2!1sru!2sru!4v1579003238768!5m2!1sru!2sru"
                    height="450"
                    frameborder="0"
                    style="border:0;"
                    allowfullscreen
            ></iframe>
        </div>
    </div>
</template>

<script>
    export default {};
</script>


<style>
    #contacts-page {
        background-image: url('../assets/patternBlack.png');
    }

    #contacts-containers {
        background: rgba(180, 180, 180, 0.9);
        max-width: 800px;
        margin-right: auto;
        margin-left: auto;
        margin-bottom: 20px;
        padding: 30px;
    }

    #contacts-title {
        margin-top: 0px;
    }

    #iframe {
        width: 100%;
        z-index: 200;
        min-height: 40vh;
    }

    h3 {
        margin: 5px;
    }

</style>