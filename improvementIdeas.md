# Improvement Ideas - Enhancements from base version

## PauseBotMod looks at multiple markets

- pausebotmod can look at multiple currency markets, and will only pause if all markets are experiencing strong sell signals
- This is done because the bitcoin price does not necessarily (or not necessarily alone) dictate how the other cryptos will move
- Standard is now set at BTC, ETH, BNB - being the 3 largest coins by market cap

## Stagnating Coin - DONE

- After coins have been bought, they could stagnate, preventing us from buying real moonshots
- The bot could keep them together if they stay between the original SL and TP
- we add 'tp_sl_hit' = False to the coins_bought dict
- We code an optional mode where we check if a coin has NEVER breached the TP (don't need to check the SL because if not it would be sold already)
- If a certain time passes and you don't reach the TP, we give up on the coin. Time is configurable.


## Drop Everything and MoonShot

- We need to receive signals from extreme moonshots, other than our normal checks
- if a coin is going up EXTREMELY and we have hit MAX_COINS, we drop a coin and jump on the moonshot
- Which coin to drop is configurable, either Best, Worst, or random (not sure why we would choose random)




 
