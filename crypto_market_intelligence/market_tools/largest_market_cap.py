from pathlib import Path
from databricks_client import run_sql
from logger import logger


def get_largest_market_cap(limit: int = 10) -> dict | None:
    """
    Execute the Largest Market Capitalization SQL query.

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
    logger.info("Running Largest Market Cap query...")

    try:
        query_path = Path(__file__).resolve().parent.parent / "queries" / "largest_market_cap.sql"

        with open(query_path, "r") as file:
            sql = file.read()

        result = run_sql(sql)

        logger.info("Largest Market Cap query completed successfully.")
        return result

    except Exception as e:
        logger.error(f"Largest Market Cap query failed: {e}")
        return None