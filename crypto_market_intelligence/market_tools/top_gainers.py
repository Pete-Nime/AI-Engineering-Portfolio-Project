from pathlib import Path
from databricks_client import run_sql
from logger import logger


def get_top_gainers(limit: int = 10) -> dict | None:
    """
    Execute the Top Gainers SQL query.

    Parameters
    ----------
    limit : int
        Number of records to return.

    Returns
    -------
    dict | None
        Databricks SQL response dictionary if successful.
        Returns None if the query fails.
    """
    logger.info("Running Top Gainers query...")

    try:
        query_path = Path(__file__).resolve().parent.parent / "queries" / "top_gainers.sql"

        with open(query_path, "r") as file:
            sql = file.read()

        result = run_sql(sql)

        logger.info("Top Gainers query completed successfully.")
        return result

    except Exception as e:
        logger.error(f"Top Gainers query failed: {e}")
        return None