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


analyzed_coins = {}

def analyze(coin):
    
    global analyzed_coins
    
    analyzed_coins = {}
    
    extract_indicators(coin)

    passed = run_technical_analysis()

    return passed


def extract_indicators(coin):

    global analyzed_coins

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

    analyzed_coins[coin] = {}

    indicators = analysis.indicators

    for indicator in INDICATORS:

        analyzed_coins[coin][indicator] = indicators[indicator]


def run_technical_analysis():

    global analyzed_coins
    
    passed = True

    return passed

def technical_analysis(coin):

    print(f'Technical Analysis: Analyzing {coin} pair')
    passed = analyze(coin)

    if passed:
        print(f'Technical Analysis: Success - BUY')
    else:
        print(f'Technical Analysis: Failure - NO BUY')

    return passed
