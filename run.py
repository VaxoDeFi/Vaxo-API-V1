#!/usr/bin/python

import flask
import os
from flask import request, jsonify
from pycoingecko import CoinGeckoAPI

app = flask.Flask(__name__)
app.config["DEBUG"] = True

coins = [
    {'id': 0,
     'name': 'Bitcoin',
     'symbol': 'BTC',
     'img': 'https//test.test/btc',
     'year_published': '2007'}
]

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/coins/all', methods=['GET'])
def api_all():
    return jsonify(coins)

app.run()

# Return sparklines prices on 7 days for current list
@app.route('/api/v1/resources/market/', methods=['GET'])
def market_top():
    coins = []
    return jsonify(coins)

app.run()
