"""
Unit Test
Largest Market Cap Tool
"""

from market_tools.largest_market_cap import get_largest_market_cap


def test_largest_market_cap():
    result = get_largest_market_cap()

    assert result is not None
    assert "result" in result
    assert "data_array" in result["result"]
    assert len(result["result"]["data_array"]) > 0

    row = result["result"]["data_array"][0]

    # Expected columns:
    # coin_name, symbol, current_price, market_cap
    assert len(row) >= 4

    print("✅ Largest Market Cap Test Passed")