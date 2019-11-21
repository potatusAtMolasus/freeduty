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
    return jsonify(age_confirmed)

@app.route('/age-confirmed', methods=['POST'])
def confirm_age():
    # global age_confirmed
    # age_confirmed = True
    return jsonify(True)

if __name__ == '__main__':
    app.run()