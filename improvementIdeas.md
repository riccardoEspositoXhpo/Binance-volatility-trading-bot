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


## Drop Everything and MoonShot - DONE

- We need to receive signals from extreme moonshots, other than our normal checks
- if a coin is going up EXTREMELY and we have hit MAX_COINS, we drop a coin and jump on the moonshot
- Which coin to drop is configurable, either Best, Worst, else it picks a random one.


## Always invest in stable coin - TODO

- We need to not let our funds go to waste and sit still
- If no opportunities are found, we should hold one of the best performing coins from a pre-defined list, selecteed by a human
- When the opportunity presents, we purchase the coin with the highest oscillators/technical indicators
- If another opportunity presents itself, we should probably drop the stablecoin and make room? 
- Easiest way to do this?

We leverage signalsamplemod to print out the best coin from the bunch and write to separate file.
Then if not max coins we can invest in it

However the feature to make room is harder. We should leverage moonshot code for it

If it says "max coins" then flag the coin and we are holding the stableCoin, say makeRoom = True?

if makeRoom is true sell stableCoin (just loop through list and wtvr)

then the next buy iteration remember coin and buy it? Idk. I just don't wanna miss a moonshot ever.

 
