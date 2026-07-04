import os
import time
import requests
from dotenv import load_dotenv
from config import validate_config
from logger import logger

load_dotenv()

HOST = os.getenv("DATABRICKS_SERVER_HOSTNAME")
TOKEN = os.getenv("DATABRICKS_TOKEN")
WAREHOUSE = os.getenv("DATABRICKS_HTTP_PATH").split("/")[-1]

URL = f"https://{HOST}/api/2.0/sql/statements"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


def run_sql(sql: str):
    validate_config()
    logger.info("Databricks configuration validated successfully.")
    payload = {
        "warehouse_id": WAREHOUSE,
        "statement": sql,
        "wait_timeout": "0s"
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(f"Submit failed: {response.text}")

    statement_id = response.json()["statement_id"]
    status_url = f"{URL}/{statement_id}"

    while True:
        status_response = requests.get(
            status_url,
            headers=HEADERS,
            timeout=30
        )

        if status_response.status_code != 200:
            raise Exception(f"Status check failed: {status_response.text}")

        result = status_response.json()
        state = result["status"]["state"]

        if state == "SUCCEEDED":
            return result

        if state in ["FAILED", "CANCELED", "CLOSED"]:
            raise Exception(f"Query failed: {result}")

        time.sleep(1)