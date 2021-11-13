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

## Always invest in stable coin - TODO

- Last priority, not sure if we want this.


- We need to not let our funds go to waste and sit still
- If no opportunities are found, we should hold one of the best performing coins from a pre-defined list, selected by a human
- When the opportunity presents, we purchase the coin with the highest oscillators/technical indicators, continuously monitored
- We only buy it after a certain time period (configurable) has passed and we still have room
- We can only buy a stablecoin if that purchase would not take us to max coins

## Adjust THRESHOLD logic to purchase coins - TODO

- We want to purchase coins if price change is above threshold, but need to make sure that the bull run is not over and the price is on an upwards trajectory
- To do this we confirm that the latest price is trading in some neighborhood of the max_price

## Volatility Cooloff Extension - DONE

- Extended the volatiliy cooloff to be twice the time interval in minutes

## Consolidate Profit - DONE

- Track the number of times the TP has been hit
- If the number breaches a configurable threshold, tighten the SL to make sure we always end up with a gain

## Custom Signal Mod

- Configure custsignalmod to implement a trading strategy based on technical indicators
- Strategy will be to look for coins trading above their EMA, with EMA10 > EMA longer periods

## Issues Log
