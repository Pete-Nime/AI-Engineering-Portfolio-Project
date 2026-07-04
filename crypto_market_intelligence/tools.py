from databricks_client import run_sql

def get_market_summary():
    query = """
    SELECT *
    FROM crypto.gold.crypto_market_summary
    """
    return run_sql(query)