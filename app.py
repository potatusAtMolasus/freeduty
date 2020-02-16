# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

age_confirmed = False

@app.route('/ping', methods=['POST'])
def ping_pong():
    return jsonify('pong!')

@app.route('/confirm-age', methods=['POST'])
def check_age():
    # return jsonify(True)
    return jsonify(age_confirmed)

@app.route('/is-age-confirmed', methods=['POST'])
def confirm_age():
    global age_confirmed
    age_confirmed = True
    return jsonify(True)


@app.route('/get-item', methods=['POST'])
def get_item():
    return jsonify({
        'id': 1,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня",
        'photo': "image.jpg",
        'description': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime impedit dignissimos dicta veritatis atque aliquam deserunt dolorem itaque, ab omnis?",
        'country': "Россия",
        'price': "3290",
        'salePrice': "1699.00",
        'sale': True,
        'category': "Коньяк",
        'volume': "0,5л",
        'strength': "40% ",
        'brand': "Трижоль",
        'popularity': "9.9"
    })

@app.route('/find', methods=['POST'])
def find():
    return jsonify({
    "current_page":5,
    "data":[
        {
            "id":1792,
            "created_at":"2020-01-27 18:53:56",
            "updated_at":"2020-01-27 18:53:56",
            "title":"\u0421\u0438\u0434\u0440 \u041a\u0435\u0440\u0438\u0441\u0430\u043a \u0434\u0443 \u0438\u0433\u0440\u0438\u0441\u0442\u044b\u0439 2% 1\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":596,
            "offer_price":499,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":1,
            "concentration":2,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":2304,
            "created_at":"2020-01-27 18:53:58",
            "updated_at":"2020-01-27 18:53:58",
            "title":"\u0412\u043e\u0434\u043a\u0430 \u041f\u043b\u043e\u0434\u043e\u0432\u0430\u044f \u0410\u0440\u0430\u0440\u0430\u0442\u0441\u043a\u0430\u044f \u0414\u043e\u043b\u0438\u043d\u0430 \u0422\u0443\u0442\u043e\u0432\u0430\u044f 40% 0,5\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":519,
            "offer_price":465,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.5,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":513,
            "created_at":"2020-01-27 18:53:51",
            "updated_at":"2020-01-27 18:53:51",
            "title":"\u041d\u0430\u0441\u0442\u043e\u0439\u043a\u0430 \u0433\u043e\u0440\u044c\u043a\u0430\u044f \u0410\u0431\u0441\u043e\u043b\u044e\u0442 \u0426\u0438\u0442\u0440\u043e\u043d 40% 0,7\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":1229,
            "offer_price":1069,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.7,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":2305,
            "created_at":"2020-01-27 18:53:58",
            "updated_at":"2020-01-27 18:53:58",
            "title":"\u0412\u043e\u0434\u043a\u0430 \u0411\u0435\u043b\u0430\u044f \u0431\u0435\u0440\u0435\u0437\u043a\u0430 \u0437\u043e\u043b\u043e\u0442\u0430\u044f 40% 0,5\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":549,
            "offer_price":499,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.5,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":514,
            "created_at":"2020-01-27 18:53:51",
            "updated_at":"2020-01-27 18:53:51",
            "title":"\u041d\u0430\u043f\u0438\u0442\u043e\u043a \u0441\u043f\u0438\u0440\u0442\u043d\u043e\u0439 \u041b\u0430\u043f\u043b\u0430\u043d\u0434\u0438\u044f \u0427\u0435\u0440\u043d\u0438\u043a\u0430 40% 0,7\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":2499,
            "offer_price":2255,
            "offer_name":"\u041a\u0440\u0430\u0441\u043d\u0430\u044f \u0446\u0435\u043d\u0430",
            "category":"",
            "volume":0.7,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":2306,
            "created_at":"2020-01-27 18:53:58",
            "updated_at":"2020-01-27 18:53:58",
            "title":"\u0412\u043e\u0434\u043a\u0430 \u0411\u0435\u043b\u0430\u044f \u0431\u0435\u0440\u0435\u0437\u043a\u0430 \u043c\u043e\u0440\u043e\u0437\u043d\u0430\u044f \u043a\u043b\u044e\u043a\u0432\u0430 40% 0,5\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":599,
            "offer_price":399,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.5,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":2051,
            "created_at":"2020-01-27 18:53:57",
            "updated_at":"2020-01-27 18:53:57",
            "title":"\u0414\u0436\u0438\u043d \u0423\u0438\u0442\u043b\u0438 \u041d\u0435\u0439\u043b \u0410\u043b\u043e\u044d \u044d\u043d\u0434 \u041a\u044c\u044e\u043a\u0430\u043c\u0431\u0435\u0440 \u0414\u0436\u0438\u043d 43% 0,7\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":2200,
            "offer_price":1799,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.7,
            "concentration":43,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":2307,
            "created_at":"2020-01-27 18:53:58",
            "updated_at":"2020-01-27 18:53:58",
            "title":"\u0412\u043e\u0434\u043a\u0430 \u0432\u0438\u043d\u043e\u0433\u0440\u0430\u0434\u043d\u0430\u044f \u041a\u0438\u0437\u043b\u044f\u0440\u043a\u0430 \u0412\u044b\u0434\u0435\u0440\u0436\u0430\u043d\u043d\u0430\u044f 45% 0,5\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":783,
            "offer_price":689,
            "offer_name":"\u041a\u0440\u0430\u0441\u043d\u0430\u044f \u0446\u0435\u043d\u0430",
            "category":"",
            "volume":0.5,
            "concentration":45,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":4,
            "created_at":"2020-01-27 18:53:48",
            "updated_at":"2020-01-27 18:53:48",
            "title":"\u0421\u0438\u0434\u0440 \u044f\u0431\u043b\u043e\u0447\u043d\u044b\u0439 \u041b\u0438\u043b\u0438\u0441 \u0421\u0430\u0439\u0434\u0435\u0440 \u0421\u0442\u0430\u0440 \u0413\u0435\u0439\u0437\u0435\u0440 \u043f\u043e\u043b\u0443\u0441\u0443\u0445\u043e\u0439 4,5% 0,5\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":296,
            "offer_price":255,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.5,
            "concentration":4.5,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":2308,
            "created_at":"2020-01-27 18:53:58",
            "updated_at":"2020-01-27 18:53:58",
            "title":"\u0412\u043e\u0434\u043a\u0430 \u041e\u043d\u0435\u0433\u0438\u043d 40% 0,5\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":1355,
            "offer_price":1199,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.5,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":5,
            "created_at":"2020-01-27 18:53:48",
            "updated_at":"2020-01-27 18:53:48",
            "title":"\u0412\u0438\u043d\u043e 202 \u041a\u0443\u0432\u0448\u0438\u043d\u0430 \u041f\u0438\u0440\u043e\u0441\u043c\u0430\u043d\u0438 \u043a\u0440\u0430\u0441\u043d\u043e\u0435 \u043f\/\u0441\u0443\u0445\u043e\u0435 13% 0,75\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"\u0413\u0420\u0423\u0417\u0418\u042f",
            "price":659,
            "offer_price":399,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"\u043a\u0440\u0430\u0441\u043d. \u043f\/\u0441\u0443\u0445.",
            "volume":0.75,
            "concentration":13,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":2053,
            "created_at":"2020-01-27 18:53:57",
            "updated_at":"2020-01-27 18:53:57",
            "title":"\u0414\u0436\u0438\u043d \u0423\u0438\u0442\u043b\u0438 \u041d\u0435\u0439\u043b \u0411\u043b\u0430\u0434 \u041e\u0440\u0430\u043d\u0436 \u0414\u0436\u0438\u043d 43% 0,7\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":2200,
            "offer_price":1799,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.7,
            "concentration":43,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":2309,
            "created_at":"2020-01-27 18:53:58",
            "updated_at":"2020-01-27 18:53:58",
            "title":"\u0421\u043f\u0438\u0440\u0442\u043d\u043e\u0439 \u043d\u0430\u043f\u0438\u0442\u043e\u043a \u0412\u043e\u0434\u043a\u0430 \u0414\u0436.\u0414\u0436. \u0423\u0438\u0442\u043b\u0438 \u0420\u0435\u0432\u0435\u043d\u0435\u0432\u0430\u044f 40% 0,7\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":1200,
            "offer_price":955,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.7,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":6,
            "created_at":"2020-01-27 18:53:48",
            "updated_at":"2020-01-27 18:53:48",
            "title":"\u0421\u0438\u0434\u0440 \u044f\u0431\u043b\u043e\u0447\u043d\u044b\u0439 \u0415\u0436\u0435\u0432\u0438\u043a\u0430 \u041b\u0438\u043b\u0438\u0441 \u0421\u0430\u0439\u0434\u0435\u0440 \u0441\u043b\u0430\u0434\u043a\u0438\u0439 4% 0,5\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":296,
            "offer_price":255,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.5,
            "concentration":4,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":518,
            "created_at":"2020-01-27 18:53:51",
            "updated_at":"2020-01-27 18:53:51",
            "title":"\u041a\u043e\u043d\u044c\u044f\u043a \u0411\u0438\u0441\u043a\u0432\u0438\u0442 \u0425\u041e 40% 0,7\u043b \u043f\/\u0443 (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":19525,
            "offer_price":14990,
            "offer_name":"\u041a\u0440\u0430\u0441\u043d\u0430\u044f \u0446\u0435\u043d\u0430",
            "category":"",
            "volume":0.7,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":2310,
            "created_at":"2020-01-27 18:53:58",
            "updated_at":"2020-01-27 18:53:58",
            "title":"\u041d\u0430\u0441\u0442\u043e\u0439\u043a\u0430 \u0424\u0438\u043d\u043b\u044f\u043d\u0434\u0438\u044f \u0411\u043b\u044d\u043a\u043a\u0443\u0440\u0430\u043d\u0442 \u0441\u043e \u0432\u043a\u0443\u0441\u043e\u043c \u0447\u0435\u0440\u043d\u043e\u0439 \u0441\u043c\u043e\u0440\u043e\u0434\u0438\u043d\u044b 37,5% 1,0\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":1915,
            "offer_price":1395,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":1,
            "concentration":37.5,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":775,
            "created_at":"2020-01-27 18:53:52",
            "updated_at":"2020-01-27 18:53:52",
            "title":"\u0412\u0438\u043d\u043e \u0410\u043b\u044c\u043c\u0430 \u0420\u043e\u043c\u0430\u043d\u0430 \u041f\u0438\u043d\u043e \u0413\u0440\u0438\u0434\u0436\u043e \u0431\u0435\u043b\u043e\u0435 \u043f\/\u0441\u0443\u0445\u043e\u0435 12% 0,75\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":592,
            "offer_price":499,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.75,
            "concentration":12,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":1031,
            "created_at":"2020-01-27 18:53:53",
            "updated_at":"2020-01-27 18:53:53",
            "title":"\u0428\u0430\u043c\u043f\u0430\u043d\u0441\u043a\u043e\u0435 \u041b\u0443\u0438 \u0420\u043e\u0434\u0435\u0440\u0435\u0440 \u041a\u0430\u0440\u0442 \u0411\u043b\u0430\u043d\u0448 \u0431\u0435\u043b\u043e\u0435 \u043f\/\u0441\u0443\u0445\u043e\u0435 12% 0,75\u043b \u043f\/\u0443 (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"\u0424\u0420\u0410\u041d\u0426\u0418\u042f",
            "price":5552,
            "offer_price":5899,
            "offer_name":"\u041a\u0440\u0430\u0441\u043d\u0430\u044f \u0446\u0435\u043d\u0430",
            "category":"",
            "volume":0.75,
            "concentration":12,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":520,
            "created_at":"2020-01-27 18:53:51",
            "updated_at":"2020-01-27 18:53:51",
            "title":"\u041d\u0430\u0441\u0442\u043e\u0439\u043a\u0430 \u041c\u0430\u043c\u043e\u043d\u0442 \u0411\u043b\u0430\u0434 (MAMONT BLOOD) \u043f\/\u0441\u043b\u0430\u0434\u043a\u0430\u044f 40% 0,5\u043b (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"",
            "price":1538,
            "offer_price":1399,
            "offer_name":"\u041a\u0440\u0430\u0441\u043d\u0430\u044f \u0446\u0435\u043d\u0430",
            "category":"",
            "volume":0.5,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        },
        {
            "id":1032,
            "created_at":"2020-01-27 18:53:53",
            "updated_at":"2020-01-27 18:53:53",
            "title":"\u0412\u0438\u0441\u043a\u0438 \u0411\u0435\u043b\u0430\u044f \u041b\u043e\u0448\u0430\u0434\u044c 40% 0,7\u043b \u043f\/\u0443 (\u0431\\\u0445)",
            "photo":"",
            "description":"",
            "country":"\u0421\u041e\u0415\u0414\u0418\u041d\u0415\u041d\u041d\u041e\u0415 \u041a\u041e\u0420\u041e\u041b\u0415\u0412\u0421\u0422\u0412\u041e",
            "price":1174,
            "offer_price":899,
            "offer_name":"\u0426\u0435\u043d\u0430 \u043e\u0442 2\u0445",
            "category":"",
            "volume":0.7,
            "concentration":40,
            "brand":"",
            "count_of_sold":0
        }
    ],
    "first_page_url":"http:\/\/127.0.0.1:5000\/get-offers?page=1",
    "from":1,
    "last_page":29,
    "last_page_url":"http:\/\/127.0.0.1:5000\/get-offers?page=29",
    "next_page_url":"http:\/\/127.0.0.1:5000\/get-offers?page=2",
    "path":"http:\/\/127.0.0.1:5000\/get-offers",
    "per_page":20,
    "prev_page_url": 'null',
    "to":20,
    "total":565
    })

    return jsonify([{
        'id': 1,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "1699.00",
        'sale': False,
        'price': "3290",
        'popularity': "9.9", 
    }, {
        'id': 3,
        'title': "Текила Монтезума Белая 40% 0,75л",
        'image': "image.jpg",
        'salePrice': "2699.00",
        'sale': True,
        'price': "3290",
        'popularity': "5.2", 
    }, {
        'id': 4,
        'title': "You may think he loves you for your money 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "3699.00",
        'sale': False,
        'price': "1290",
        'popularity': "7.3", 
    }, {
        'id': 5,
        'title': "But I Know What he Actually loves you For 15% 0,6л п/у",
        'image': "image.jpg",
        'salePrice': "2699.00",
        'sale': False,
        'price': "3340",
        'popularity': "9.2",         
    }, {
        'id': 6,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2699.00",
        'sale': False,
        'price': "1230",
        'popularity': "9.7", 
    }, {
        'id': 7,
        'title': "Thats your brand new Leopard Skin PilBox Hat 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2659.00",
        'sale': True,
        'price': "2560",
        'popularity': "8.1", 
    }, {
        'id': 8,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2799.00",
        'sale': True,
        'price': "4110",
        'popularity': "9.1", 
    }])
    
@app.route('/get-categories', methods=['POST'])
def get_categories():
    return jsonify([{
        'url':'/search/1',
        'label': 'Категория 1',
    }, {
        'url':'/search/2',
        'label': 'Категория 2',
    }, {
        'url':'/search/3',
        'label': 'Категория 3',
    }, {
        'url':'/search/4',
        'label': 'Категория 4',
    }, {
        'url':'/search/5',
        'label': 'Категория 5',
    }, {
        'url':'/search/6',
        'label': 'Категория 6',
    }, {
        'url':'/search/7',
        'label': 'Категория 7',
    }, {
        'url':'/search/8',
        'label': 'Категория 8',
    }])

@app.route('/all-offers', methods=['POST'])
def get_offers():

        # 'id': 1,
        # 'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        # 'image': "image.jpg",
        # 'description': "",
        # 'country': "",
        # 'price': "3290",
        # 'salePrice': "2 699.00",
        # 'sale': "2 699.00",
        # 'category': "",
        # 'volume': "",
        # 'strength': "",
        # 'brand': "",
        # 'popularity': "", 
    return jsonify([{
        'id': 1,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 3,
        'title': "Текила Монтезума Белая 40% 0,75л",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 4,
        'title': "You may think he loves you for your money 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 5,
        'title': "But I Know What he Actually loves you For 15% 0,6л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",        
        'popularity': "9.1", 
    }, {
        'id': 6,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 7,
        'title': "Thats your brand new Leopard Skin PilBox Hat 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 8,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }])

@app.route('/get-popular', methods=['POST'])
def get_popular():
    return jsonify([{
        'id': 1,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': False,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 3,
        'title': "Текила Монтезума Белая 40% 0,75л",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 4,
        'title': "You may think he loves you for your money 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': False,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 5,
        'title': "But I Know What he Actually loves you For 15% 0,6л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': False,
        'price': "3290",
        'popularity': "9.1",         
    }, {
        'id': 6,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': False,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 7,
        'title': "Thats your brand new Leopard Skin PilBox Hat 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 8,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }])

@app.route('/get-posts', methods=['POST'])
def get_posts():
    return jsonify([{
        'id': 1,
        'title': "Фламинго",
        'images': ["flamingo.jpg","man.jpg", "climate.jpg",],
        'text': """white, pink, green or blue
                show off your natural hue
                flamingo, Oh oh o-uuu-o
                if you're multicolored, that's cool too"""
    }, {
        'id': 2,
        'title': "Глобусы",
        'images': ["image.jpg"],
        'text': """Гло гло гло-бу-сы
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque, saepe!"""
    }, {
        'id': 3,
        'title': "Глобальное потепление",
        'images': ["climate.jpg"],
        'text': """Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque, saepe!"""
    }, {
        'id': 4,
        'title': "Конь Боджек",
        'images': ["man.jpg", "climate.jpg", "flamingo.jpg"],
        'text': """Back in the 90s I was in a very famous tv show
                Bojack the horse, Bojack the horse don't act like you don't know
                And i'm trying to hold on to my past
                it's been so long i don't think that i am gonna last
                i guess i'll just try and make you understand
                That i'm more a horse than a man
                Or i'm more man than a horse"""
    }, {
        'id': 5,
        'title': "Канье Вест",
        'images': ["ye.png","discount.png"],
        'text': """Grrrat-gat (I can still feel the love)
                Gat-gat-gat-gat-gat
                Grrrat-gat-gat-gat (I can still feel the love)
                Grrrat-gat-gat-gat-gat-gat (feel the love)
                Grrrat
                Ba-ba-ba-ba
                Brrat-tat-da-da-da-da
                Ga-ga-ga-ga
                Brrr-ah-da-da, brrr-ah-da-da
                Brrr-ah-da-da-da, brrr-ah-da-da-da
                Brrr-ah-brrr-ah, brrr-ah-ga-grrrat
                Ru-ru-ru-ru-oh!"""
    }, {
        'id': 6,
        'title': "Работа Фронтэндера",
        'images': ["discount.png"],
        'text': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque in sequi illo laborum neque."
    }])

@app.route('/get-filters', methods=['POST'])
def get_filters():   
    return jsonify({
        'categories': [
            {'value': 'vino', 'label': 'Вино'},
            {'value': 'vodka', 'label': 'Вока'},
            {'value': 'konjak', 'label': 'Коньяк'},
            {'value': 'viski', 'label': 'Виски'}
        ],
        'brands': [
            {'value': 'fanagoria', 'label': 'Fanagoria'},
            {'value': 'sangria', 'label': 'Sangria'},
            {'value': 'bells', 'label': 'Bells'},
            {'value': 'jack', 'label': 'Jack'}
        ],
        'countries': [
            {'value': 'russia', 'label': 'Россия'},
            {'value': 'england', 'label': 'Великобритания'},
            {'value': 'usa', 'label': 'США'},
            {'value': 'ukraine', 'label': 'Украина'}
        ],
        'price': {
            'lowest': 100,
            'highiest': 5000
        }
    })

if __name__ == '__main__':
    app.run()