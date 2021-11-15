# Improvement Ideas - Enhancements from base version

## PauseBotMod looks at multiple markets - DONE

- pausebotmod can look at multiple currency markets, and will only pause if all markets are experiencing strong sell signals
- This is done because the bitcoin price does not necessarily (or not necessarily alone) dictate how the other cryptos will move
- Standard is now set at BTC, ETH, BNB - being the 3 largest coins by market cap
- The bot will average out the SELL indicators for the 3 coins and compute an average market sentiment

## Stagnating Coin - DONE

- After coins have been bought, they could stagnate, preventing us from buying real moonshots
- The bot could keep them together if they stay between the original SL and TP
- we add 'tp_sl_hit' = 0 to the coins_bought dict
- We code an optional mode where we check if a coin has NEVER breached the TP (don't need to check the SL because if not it would be sold already)
- If a certain time passes and you don't reach the TP, we give up on the coin. Time is configurable.

## Drop Everything and MoonShot - DONE

- We need to receive signals from extreme moonshots, other than our normal checks
- if a coin is going up EXTREMELY and we have hit MAX_COINS, we drop a coin and jump on the moonshot
- Which coin to drop is configurable, either Best, Worst, else it picks a random one.

## Adjust THRESHOLD logic to purchase coins - DONE

- We want to purchase coins if price change is above threshold, but need to make sure that the bull run is not over and the price is on an upwards trajectory
- To do this we confirm that the latest price is close to the peak
- We would like to avoid looking for a 5% increase in price, but the coin has actually gained 8% and already dropped 3%

## Volatility Cooloff Extension - DONE

- Extended the volatiliy cooloff to be twice the time interval in minutes

## Consolidate Profit - DONE

- Track the number of times the TP has been hit
- If the number breaches a configurable threshold, tighten the SL to make sure we always end up with a gain

## Update Ticker Mod - DONE

- Module scans binance for all trading pairs ending in PAIR_WITH and not in EXCLUDE coin list
- For every coin not in existing ticker list, tries to retrieve analysis to ensure coin works
- Adds coin to ticker list
- Suggested not to run this more than once per day

## Technical Analysis - DONE

- Configure a trading strategy based on technical indicators
- Each time we find an eligible coin, we run the technical analysis to confirm that we should buy it
- Strategy is configurable in technical_analysis.py
- Strategy:
  - EMA
  - RSI
  - ADX
  - MACD

## Issues Log

- Seems that if we buy too many coins we may be missing out on opportunities. we have the moonshot logic, but should we compute a "relative coin strenth" to see if we should substitute?
- ideally you identify a coin, there is no space, you evaluate all your other investments, is it better? if yes, drop the bad coin and get the good one. always invest in good ones.
- we could also implement the technical analysis to sell? nah wtvr not yet at least.


