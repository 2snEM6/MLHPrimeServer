from flask import Flask, json
from flask import request
from flask import json
from flask import make_response
import request as req

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

    response_data = {"displayText": 'this is text displayed'}
    speech = ""
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        body = json.dumps(request.json)
        action = body['result']['action']

        if action == 'SEARCH':
            params = body['result']['parameters']
            qs = []
            for key in params:
                if 'Param' in key:
                    qs.append(params[key])
            symbols = ''
            symbol_first = True
            for key in params:

                if 'Symbol' in key:
                    if symbol_first:
                        symbol_first = False
                        symbols = symbols + params[key]
                    else:
                        symbols = symbols + ',' + params[key]

            resp = req.get(BASE_URL + GET_QUOTE, params={'key': KEY, 'symbols': symbols})

            for param in params:
                speech = speech + " the " + param + " is " + resp[param]

    response_data["speech"] = speech
    js = json.dumps(response_data)
    r = make_response(js)
    r.headers['Content-Type'] = 'application/json'
    return r


# Request a la API de STOCK
# r = re.get(BASE_URL + GET_QUOTE, params={'key': KEY, 'symbols': symbol})


if __name__ == '__main__':
    app.run(port=4000)
