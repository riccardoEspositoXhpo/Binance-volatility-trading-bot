# Available indicators here: https://python-tradingview-ta.readthedocs.io/en/latest/usage.html#retrieving-the-analysis

from tradingview_ta import TA_Handler, Interval, Exchange
# use for environment variables
import os
# use if needed to pass args to external modules
import sys
# used for directory handling
import glob
import time
import threading

# indicators to use in Technical Analysis
INDICATORS = ['EMA5', 'EMA10', 'EMA20', 'EMA30', 'RSI', 'ADX', 'ADX+DI', 'ADX-DI', 'MACD.macd', 'MACD.signal', 'HullMA9']
INTERVAL = Interval.INTERVAL_5_MINUTES # timeframe for analysis
TIME_TO_WAIT = 5 # time to wait in minutes before the last analysis

EXCHANGE = 'BINANCE'
SCREENER = 'CRYPTO'
PAIR_WITH = 'USDT'
TICKERS = 'tickers.txt'
TIME_TO_WAIT = 2 # Minutes to wait between analysis
FULL_LOG = False # List analysis result to console

def analyze(pairs):
    signal_coins = {}
    analysis = {}
    handler = {}
    
    if os.path.exists('signals/custsignalmod.exs'):
        os.remove('signals/custsignalmod.exs')

    for pair in pairs:
        handler[pair] = TA_Handler(
            symbol=pair,
            exchange=EXCHANGE,
            screener=SCREENER,
            interval=INTERVAL,
            timeout= 10)
       
    for pair in pairs:
        try:
            analysis = handler[pair].get_analysis()
        except Exception as e:
            print("Signalsample:")
            print("Exception:")
            print(e)
            print (f'Coin: {pair}')
            print (f'handler: {handler[pair]}')


        if FULL_LOG:
            print(f'Custsignalmod:{pair} Oscillators:{oscCheck}/{len(OSC_INDICATORS)} Moving averages:{maCheck}/{len(MA_INDICATORS)}')
        
        if True:
                signal_coins[pair] = pair
                print(f'Custsignalmod: Signal detected on {pair} at {oscCheck}/{len(OSC_INDICATORS)} oscillators and {maCheck}/{len(MA_INDICATORS)} moving averages.')
                with open('signals/custsignalmod.exs','a+') as f:
                    f.write(pair + '\n')
    
    return signal_coins

def do_work():
    signal_coins = {}
    pairs = {}

    pairs=[line.strip() for line in open(TICKERS)]
    for line in open(TICKERS):
        pairs=[line.strip() + PAIR_WITH for line in open(TICKERS)] 
    
    while True:
        if not threading.main_thread().is_alive(): exit()
        print(f'Custsignalmod: Analyzing {len(pairs)} coins')
        signal_coins = analyze(pairs)
        print(f'Custsignalmod: {len(signal_coins)} coins above moving averages. Waiting {TIME_TO_WAIT} minutes for next analysis.')
        time.sleep((TIME_TO_WAIT*60))


# testing
if __name__ == '__main__':
    do_work()

# start script
# run analysis on some timeframe
# flag potential buys statically in some file (like test_coins_bought.json tipo)
# re-run analysis a second time
# drop a signal on a coin that was present both times

