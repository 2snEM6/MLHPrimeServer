from flask import Flask
from flask import request
from flask import json
from flask import Response
from flask import make_response
import requests as re

app = Flask(__name__)

BASE_URL = "http://marketdata.websol.barchart.com/"
KEY = "b1a585d027c8d89fa27ccd3628609739"
GET_QUOTE = "getQuote.json"
SYMBOLS = "symbols"


@app.route("/")
def hello():
    return 'Hello, world!'


@app.route("/webhook", methods=['POST'])
def handle():
    data = {
        hello: 'world',
        number: 3
    }
    js = json.dumps(data)
    r = make_response(js)
    r.headers['Content-Type'] = 'application/json'
    return r


# Request a la API de STOCK
# r = re.get(BASE_URL + GET_QUOTE, params={'key': KEY, 'symbols': symbol})


if __name__ == '__main__':
    app.run(port=4000)
