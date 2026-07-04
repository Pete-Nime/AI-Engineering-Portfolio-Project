SELECT
    coin_name,
    symbol,
    current_price,
    market_cap
FROM crypto.gold.most_valuable_coins
ORDER BY market_cap DESC
LIMIT 10;