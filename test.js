var indicators = {

    "RSI": 60.28037412, // above 70 then price is too high and below 30 price is too low 
    "ADX": 35.78754863, // above 20 it is a "strong signal"
    "ADX+DI": 23.16948389, // strong signal to buy when ADX+DI is higher than ADX-DI
    "ADX-DI": 13.82449817, // signal to sell when -DI goes above +DI
    "MACD.macd": 2444.73734978, // bull when macd is above signal
    "MACD.signal": 2606.00138275, // see above
    "close": 45326.97, // this is the price actually
    "EMA5": 45600.06414333,  // these should all be included
    "EMA10": 45223.22433151, // typically I'd look for a moment in which EMA10 > EMA20 > EMA30 > EMA50 ?
    "EMA20": 43451.52018338, // not sure about 100 and 200, 
    "EMA30": 41908.5944052,
    "EMA50": 40352.10222373,
    "EMA100": 40356.09177879,
    "EMA200": 39466.50411569,
    "HullMA9": 45470.37107407, // if it is increasing we can buy? must be below the current price though? 
    "low": 44203.28,
    "high": 45560
}

// comments .
// we pull out both analyses over two timeframes... ?

// in one case I just check the latest to look at moving averages
// second I can look at the trends ?

/* BUY if on shortest timeframe
 
 (EMA) 5 > 10 > 20 > 30 > 50 (check if we care about 50) - price at least greater than the 10
 (RSI) between 30 and 70
 (ADX) above 20
 (ADX) +DI > -DI
 (MACD) Macd > Signal

 To check on longest timeframe:
 (MACD) Macd was less high than signal?
 (EMA) it was not all in order ? 
 (ADX) lower?


*/
