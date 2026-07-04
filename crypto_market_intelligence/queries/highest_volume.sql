SELECT
    coin_name,
    symbol,
    current_price,
    total_volume,
    market_cap
FROM crypto.gold.highest_volume
ORDER BY total_volume DESC
LIMIT 10;