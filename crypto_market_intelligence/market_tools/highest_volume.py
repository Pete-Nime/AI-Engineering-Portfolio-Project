from pathlib import Path
from databricks_client import run_sql
from logger import logger


def get_highest_volume(limit: int = 10) -> dict | None:
    """
    Execute the Highest Trading Volume SQL query.

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
    logger.info("Running Highest Volume query...")

    try:
        query_path = Path(__file__).resolve().parent.parent / "queries" / "highest_volume.sql"

        with open(query_path, "r") as file:
            sql = file.read()

        result = run_sql(sql)

        logger.info("Highest Volume query completed successfully.")
        return result

    except Exception as e:
        logger.error(f"Highest Volume query failed: {e}")
        return None