"""
Unit Test
Top Gainers Tool
"""

from market_tools.top_gainers import get_top_gainers


def test_top_gainers():

    result = get_top_gainers()

    assert result is not None
    assert "result" in result
    assert "data_array" in result["result"]
    assert len(result["result"]["data_array"]) > 0

    row = result["result"]["data_array"][0]

    assert len(row) >= 5

    print("✅ Top Gainers Test Passed")