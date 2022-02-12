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

PAIR_WITH = 'USDT'
TICKERS = 'tickers.txt'
TIME_TO_WAIT = 1 # minutes to wait between analyses

analyzed_coin = {}
failed_coins = []
failed_then_success_coins = []


def technical_analysis(coin):
    
    global analyzed_coin
    global failed_coins
    global failed_then_success_coins
    
    analyzed_coin = {}
    
    extract_indicators(coin)

    try:
        passed = run_technical_analysis()
    except:
        print("Cannot retrieve analysis for " + coin)
        passed = True

    if not passed and coin not in failed_coins:
        failed_coins.append(coin)
    elif passed and coin in failed_coins:
        failed_then_success_coins.append(coin)


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

        indicators = analysis.indicators

        for indicator in INDICATORS:

            analyzed_coin[indicator] = indicators[indicator]

    except Exception as e:
        pass


def run_technical_analysis():

    global analyzed_coin
    
    passed = True

    # # check 1 - ensure the EMAs are in order
    if not (analyzed_coin['EMA5'] > analyzed_coin['EMA10'] and (analyzed_coin['EMA5'] > analyzed_coin['EMA20'])):
        passed = False

    # check 2 - ensure RSI is within 30 / 70 bound
    # if not(analyzed_coin['RSI'] > 30 and analyzed_coin['RSI'] < 70):
    #     passed = False
    
    # # check 3 - ensure ADX above 20 and ADX+DI > ADX-DI
    # if not(analyzed_coin['ADX'] >= 20 and (analyzed_coin['ADX+DI'] > analyzed_coin['ADX-DI'])):
    #     passed = False
    
    # check 4 - MACD Line above MACD Signal
    # if not(analyzed_coin['MACD.macd'] > analyzed_coin['MACD.signal']):
    #     passed = False


    return passed



def analyze(pairs):

    global failed_coins
    global failed_then_success_coins

    signal_coins = {}
  
    if os.path.exists('signals/signalsample.exs'):
        os.remove('signals/signalsample.exs')
    
    for pair in pairs:
       
       technical_analysis(pair)
       
       if pair in failed_then_success_coins:   
        failed_then_success_coins.pop(pair)       
        failed_coins.pop(pair)       
        signal_coins[pair] = pair
        print(f'Signalsample: Signal detected on {pair}')
        with open('signals/signalsample.exs','a+') as f:
            f.write(pair + '\n')

    # debugging logic
    print(failed_coins)
    print(failed_then_success_coins)
    return signal_coins


def do_work():
    global failed_coins
    global failed_then_success_coins

    failed_coins = []
    failed_then_success_coins = []

   
    signal_coins = {}
    pairs = {}

    pairs=[line.strip() for line in open(TICKERS)]
    for line in open(TICKERS):
        pairs=[line.strip() + PAIR_WITH for line in open(TICKERS)] 
    

    while True:
        print(f'Signalsample: Analyzing {len(pairs)} coins')
        signal_coins = analyze(pairs)

        if len(signal_coins) == 0:
            print(f'Signalsample: No coins above threshold on both timeframes. Waiting {TIME_TO_WAIT} minutes for next analysis')
        else:
            print(f'Signalsample: {len(signal_coins)} coins above treshold on both timeframes. Waiting {TIME_TO_WAIT} minutes for next analysis')

        time.sleep((TIME_TO_WAIT*60))


# devi segnare uno che non é in fila, e poi diventa in fila. you get me?
# poi scopriamo il sell... che semplicemente vendi se diventa "failed" il technical analysis. controlli dall'altra parte
