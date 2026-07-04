"""
Unit Test
Highest Volume Tool
"""

from market_tools.highest_volume import get_highest_volume


def test_highest_volume():
    result = get_highest_volume()

    assert result is not None
    assert "result" in result
    assert "data_array" in result["result"]
    assert len(result["result"]["data_array"]) > 0

    row = result["result"]["data_array"][0]

    # Expected columns:
    # coin_name, symbol, current_price, total_volume, market_cap
    assert len(row) >= 5

    print("✅ Highest Volume Test Passed")