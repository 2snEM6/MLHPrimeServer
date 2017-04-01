from flask import Flask
from flask import request
import requests as re

app = Flask(__name__)

BASE_URL = "http://marketdata.websol.barchart.com/"
KEY = "b1a585d027c8d89fa27ccd3628609739"
GET_QUOTE = "getQuote.json"
SYMBOLS = "symbols"


@app.route("/")
def hello():
    return 'Hello, world!'


@app.route("/get_quote")
def get_quote():
    symbol = request.args.get('symbol')
    r = re.get(BASE_URL + GET_QUOTE, params={'key': KEY, 'symbols': symbol})
    return r.text


if __name__ == '__main__':
    app.run(port=4000)
