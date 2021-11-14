from tradingview_ta import TA_Handler, Interval, Exchange
import os
import time
import threading

INTERVAL = Interval.INTERVAL_1_MINUTE #Timeframe for analysis

EXCHANGE = 'BINANCE'
SCREENER = 'CRYPTO'
SYMBOLS = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
THRESHOLD = 13 # 7 of 15 MA's indicating sell
TIME_TO_WAIT = 5 # Minutes to wait between analysis
FULL_LOG = False # List analysis result to console

def analyze():

    paused = True

    ma_sell = 0
    average_ma_sell = 0

    for symbol in SYMBOLS:  
        analysis = {}
        handler = {}
        
        handler = TA_Handler(
                symbol=symbol,
                exchange=EXCHANGE,
                screener=SCREENER,
                interval=INTERVAL,
                timeout= 10)
    
        try:
            analysis = handler.get_analysis()
        except Exception as e:
            print("pausebotmod:")
            print("Exception:")
            print(e)
        
        ma_sell += analysis.moving_averages['SELL']
        

    average_ma_sell = ma_sell / len(SYMBOLS)
    
    if average_ma_sell >= THRESHOLD:
        paused = True
        print(f'pausebotmod: Market not looking too good, bot paused from buying. Waiting {TIME_TO_WAIT} minutes for next market checkup.')

    if average_ma_sell < THRESHOLD:
        paused = False    
        print(f'pausebotmod: Market looks ok, bot is running. Waiting {TIME_TO_WAIT} minutes for next market checkup.')


    return paused
    
#if __name__ == '__main__':
def do_work():
      
    while True:
        if not threading.main_thread().is_alive(): exit()
        # print(f'pausebotmod: Fetching market state')
        paused = analyze()
        if paused:
            with open('signals/paused.exc','a+') as f:
                f.write('yes')
        else:                
            if os.path.isfile("signals/paused.exc"):
                os.remove('signals/paused.exc')
                        
        # print(f'pausebotmod: Waiting {TIME_TO_WAIT} minutes for next market checkup')    
        time.sleep((TIME_TO_WAIT*60))
