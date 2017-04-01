from flask import Flask
from flask import request
from flask import json
from flask import Response
import requests as re

app = Flask(__name__)

BASE_URL = "http://marketdata.websol.barchart.com/"
KEY = "b1a585d027c8d89fa27ccd3628609739"
GET_QUOTE = "getQuote.json"
SYMBOLS = "symbols"


@app.route("/")
def hello():
    return 'Hello, world!'


@app.route("/handle")
def handle():
    data = {
        'hello': 'world',
        'number': 3
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


# Request a la API de STOCK
# r = re.get(BASE_URL + GET_QUOTE, params={'key': KEY, 'symbols': symbol})


if __name__ == '__main__':
    app.run(port=4000)
