SELECT
    coin_name,
    symbol,
    current_price,
    price_change_percentage_24h,
    market_cap
FROM crypto.gold.top_gainers
ORDER BY price_change_percentage_24h DESC
LIMIT 10;