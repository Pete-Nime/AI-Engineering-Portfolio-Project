"""
Unit Test
Market Summary Tool
"""

from market_tools.market_summary import get_market_summary


def test_market_summary():

    result = get_market_summary()

    assert result is not None
    assert "result" in result
    assert "data_array" in result["result"]
    assert len(result["result"]["data_array"]) > 0

    row = result["result"]["data_array"][0]

    assert len(row) >= 5

    print("✅ Market Summary Test Passed")
    result = get_market_summary()
    print(result)