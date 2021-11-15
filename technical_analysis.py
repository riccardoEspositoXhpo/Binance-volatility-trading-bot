# Available indicators here: https://python-tradingview-ta.readthedocs.io/en/latest/usage.html#retrieving-the-analysis

from datetime import datetime
from tradingview_ta import TA_Handler, Interval, Exchange
# use for environment variables
import os
# use if needed to pass args to external modules
import sys

# used for directory handling
import glob
import time
import json
import datetime

from helpers.handle_creds import (
    load_correct_creds, test_api_key
)

from helpers.parameters import (
    parse_args, load_config
)

# indicators to use in Technical Analysis
INDICATORS = ['EMA5', 'EMA10', 'EMA20', 'EMA30', 'RSI', 'ADX', 'ADX+DI', 'ADX-DI', 'MACD.macd', 'MACD.signal', 'HullMA9']
INTERVAL = Interval.INTERVAL_1_MINUTE 

DEFAULT_CONFIG_FILE = 'config.yml'  

config_file = DEFAULT_CONFIG_FILE
parsed_config = load_config(config_file)

# load config variables
PAIR_WITH = parsed_config['trading_options']['PAIR_WITH']

EXCHANGE = 'BINANCE'
SCREENER = 'CRYPTO'


analyzed_coin = {}

def analyze(coin, price):
    
    global analyzed_coin
    
    analyzed_coin = {}
    
    extract_indicators(coin)

    passed = run_technical_analysis(price)

    return passed


def extract_indicators(coin):

    global analyzed_coin

    try:
        handler = TA_Handler(
                symbol=coin,
                exchange=EXCHANGE,
                screener=SCREENER,
                interval=INTERVAL,
                timeout= 10)
        analysis = handler.get_analysis()

    except Exception as e:
        print("CustSignal - ")
        print("Exception:")
        print(e)
        print (f'Coin: {coin}')
        print (f'handler: {handler}')

    indicators = analysis.indicators

    for indicator in INDICATORS:

        analyzed_coin[indicator] = indicators[indicator]


def run_technical_analysis(price):

    global analyzed_coin
    
    passed = True

    # check 1 - ensure the EMAs are in order
    if not (price > analyzed_coin['EMA5'] > analyzed_coin['EMA10'] > analyzed_coin['EMA20']):
        passed = False

    # check 2 - ensure RSI is within 30 / 70 bound
    if not(analyzed_coin['RSI'] > 30 and analyzed_coin['RSI'] < 70):
        passed = False
    
    # check 3 - ensure ADX above 20 and ADX+DI > ADX-DI
    if not(analyzed_coin['ADX'] >= 20 and (analyzed_coin['ADX+DI'] > analyzed_coin['ADX-DI'])):
        passed = False
    
    # check 4 - MACD Line above MACD Signal
    if not(analyzed_coin['MACD.macd'] > analyzed_coin['MACD.signal']):
        passed = False


    return passed

def technical_analysis(coin, price):

    print(f'Technical Analysis: Analyzing {coin} pair')
    passed = analyze(coin, price)

    if passed:
        print(f'Technical Analysis: Success - BUY')
    else:
        print(f'Technical Analysis: Failure - NO BUY')

    return passed


if __name__ == '__main__':
    coin = 'UMAUSDT'
    price = 64000
    technical_analysis(coin,price)
    print(analyzed_coin)