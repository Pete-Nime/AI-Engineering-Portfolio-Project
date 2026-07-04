"""
Unit Test
Top Losers Tool
"""

from market_tools.top_losers import get_top_losers


def test_top_losers():

    result = get_top_losers()

    assert result is not None
    assert "result" in result
    assert "data_array" in result["result"]
    assert len(result["result"]["data_array"]) > 0

    row = result["result"]["data_array"][0]

    assert len(row) >= 5

    print("✅ Top Losers Test Passed")