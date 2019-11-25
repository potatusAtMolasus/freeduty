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
    return jsonify(True)
    # return jsonify(age_confirmed)

@app.route('/age-confirmed', methods=['POST'])
def confirm_age():
    global age_confirmed
    age_confirmed = True
    return jsonify(True)

@app.route('/find', methods=['POST'])
def find():
    return jsonify(True)
    
@app.route('/get-categories', methods=['POST'])
def get_categories():
    return jsonify([{
        'url':'/category/1',
        'label': 'Категория 1',
    }, {
        'url':'/category/2',
        'label': 'Категория 2',
    }, {
        'url':'/category/3',
        'label': 'Категория 3',
    }, {
        'url':'/category/4',
        'label': 'Категория 4',
    }, {
        'url':'/category/5',
        'label': 'Категория 5',
    }, {
        'url':'/category/6',
        'label': 'Категория 6',
    }, {
        'url':'/category/7',
        'label': 'Категория 7',
    }, {
        'url':'/category/8',
        'label': 'Категория 8',
    }])



if __name__ == '__main__':
    app.run()