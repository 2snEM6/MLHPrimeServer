from flask import Flask
import requests as re
app = Flask(__name__)

BASE_URL = "http://ondemand.websol.barchart.com/"
KEY  "b1a585d027c8d89fa27ccd3628609739"
GET_QUOTE = "getQuote.json"

http://ondemand.websol.barchart.com/getQuote.json?symbols=AAPL%2CGOOG&fields=fiftyTwoWkHigh%2CfiftyTwoWkHighDate%2CfiftyTwoWkLow%2CfiftyTwoWkLowDate&mode=I

@app.route("/")
def hello():
    return 'Hello, world!'

@app.route("/get_quote")
def get_quote():
    r = re.get(BASE_URL + GET_QUOTE, params=)




if __name__ == '__main__':
    app.run(port=4000)
