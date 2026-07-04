from fastmcp import FastMCP
from market_tools.market_summary import get_market_summary
from market_tools.top_gainers import get_top_gainers
from market_tools.top_losers import get_top_losers
from market_tools.highest_volume import get_highest_volume
from market_tools.largest_market_cap import get_largest_market_cap
from logger import logger

mcp = FastMCP("Crypto Market Intelligence MCP")


@mcp.tool()
def market_summary() -> dict | None:
    """
    Retrieve an overall summary of the cryptocurrency market.

    Returns
    -------
    dict | None
        Market statistics including market cap,
        trading volume and coin count.
    """
    logger.info("MCP Tool: market_summary called")
    return get_market_summary()


@mcp.tool()
def top_gainers(limit: int = 10) -> dict | None:
    """
    Retrieve the top gaining cryptocurrencies.

    Parameters
    ----------
    limit : int
        Number of cryptocurrencies to return.

    Returns
    -------
    dict | None
    """
    logger.info(f"MCP Tool: top_gainers called (limit={limit})")
    return get_top_gainers(limit)

@mcp.tool()
def top_losers(limit: int = 10) -> dict | None:
    """
    Retrieve the top losing cryptocurrencies.

    Parameters
    ----------
    limit : int
        Number of cryptocurrencies to return.

    Returns
    -------
    dict | None
    """
    logger.info(f"MCP Tool: top_losers called (limit={limit})")
    return get_top_losers(limit)

@mcp.tool()
def highest_volume(limit: int = 10) -> dict | None:
    """
    Retrieve cryptocurrencies with the highest trading volume.

    Parameters
    ----------
    limit : int
        Number of cryptocurrencies to return.

    Returns
    -------
    dict | None
    """
    logger.info(f"MCP Tool: highest_volume called (limit={limit})")
    return get_highest_volume(limit)

@mcp.tool()
def largest_market_cap(limit: int = 10) -> dict | None:
    """
    Retrieve cryptocurrencies with the largest market capitalization.

    Parameters
    ----------
    limit : int
        Number of cryptocurrencies to return.

    Returns
    -------
    dict | None
    """
    logger.info(f"MCP Tool: largest_market_cap called (limit={limit})")
    return get_largest_market_cap(limit)


if __name__ == "__main__":
    mcp.run()