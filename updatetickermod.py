from tradingview_ta import TA_Handler, Interval, Exchange

from binance.client import Client

from helpers.handle_creds import (
    load_correct_creds, test_api_key
)

from helpers.parameters import (
    parse_args, load_config
)

# use for environment variables
import os
# use if needed to pass args to external modules
import sys
# used for directory handling
import glob

import time


DEFAULT_CONFIG_FILE = 'config.yml'  
DEFAULT_CREDS_FILE = 'creds.yml'

config_file = DEFAULT_CONFIG_FILE
creds_file = DEFAULT_CREDS_FILE
parsed_config = load_config(config_file)
parsed_creds = load_config(creds_file)

# load config variables
PAIR_WITH = parsed_config['trading_options']['PAIR_WITH']
CUSTOM_LIST = parsed_config['trading_options']['CUSTOM_LIST']
TICKERS = parsed_config['trading_options']['TICKERS_LIST']
EXCLUDE = parsed_config['trading_options']['EXCLUDE']

# handler variables
MY_EXCHANGE = 'BINANCE'
MY_SCREENER = 'CRYPTO'
INTERVAL = Interval.INTERVAL_5_MINUTES

# Load creds for correct environment
access_key, secret_key = load_correct_creds(parsed_creds)

client = Client(access_key, secret_key)




TIME_TO_WAIT = 1 # Days to wait between analysis
FULL_LOG = False # List anylysis result to console

def analyze(current_tickers):

    raw_tickers = client.get_all_tickers()
    
    tickers = []

    for raw_ticker in raw_tickers:

        if raw_ticker['symbol'].endswith(PAIR_WITH) and all(fiat not in raw_ticker['symbol'] for fiat in EXCLUDE):
            tickers.append(raw_ticker['symbol'])
    

    for ticker in tickers:
        if ticker not in current_tickers:
            
            handler = TA_Handler(
                symbol=ticker,
                exchange=MY_EXCHANGE,
                screener=MY_SCREENER,
                interval=INTERVAL,
                timeout= 10
            )

            try: 
                test_analysis = handler.get_analysis()

                symbol = ticker.replace(PAIR_WITH, '')
                with open(TICKERS, 'a+') as f:
                    f.write('\n' + symbol)
                                
                print(f'Updateticker: Ticker {ticker} not in ticker list. Adding to list.')
            
            except Exception as e:
                    if FULL_LOG: print(f"Updateticker: Ticker {ticker} exists and not in list but not retrievable via TA_handler")
        
    # plural day handling
    s = ''
    if TIME_TO_WAIT > 1: s = 's'

    print(f"Ticker list updated. Waiting {TIME_TO_WAIT} day{s} for next check.")

           
    return

def do_work():
    current_tickers = {}


    # get list of tickers saved to file
    current_tickers=[line.strip() for line in open(TICKERS)]
    for line in open(TICKERS):
        current_tickers=[line.strip() + PAIR_WITH for line in open(TICKERS)] 
    
    
    while True:
        print(f'Updateticker: checking for new coin pairs')

        analyze(current_tickers)


        time.sleep((TIME_TO_WAIT*60*60*24))

