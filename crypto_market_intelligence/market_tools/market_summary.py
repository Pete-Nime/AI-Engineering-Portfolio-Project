from pathlib import Path
from databricks_client import run_sql
from logger import logger


def get_market_summary() -> dict | None:
    """
    Execute the Market Summary SQL query.

    Returns
    -------
    dict | None
        Databricks SQL response dictionary if successful.
        Returns None if the query fails.
    """
    logger.info("Running Market Summary query...")

    try:
        query_path = Path(__file__).resolve().parent.parent / "queries" / "market_summary.sql"

        with open(query_path, "r") as file:
            sql = file.read()

        result = run_sql(sql)

        logger.info("Market Summary query completed successfully.")
        return result

    except Exception as e:
        logger.error(f"Market Summary query failed: {e}")
        return None