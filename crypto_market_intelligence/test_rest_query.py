import os
import requests
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("DATABRICKS_SERVER_HOSTNAME")
TOKEN = os.getenv("DATABRICKS_TOKEN")
WAREHOUSE = os.getenv("DATABRICKS_HTTP_PATH").split("/")[-1]

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

url = f"https://{HOST}/api/2.0/sql/statements"

payload = {
    "warehouse_id": WAREHOUSE,
    "statement": "SELECT CURRENT_TIMESTAMP()",
    "wait_timeout": "30s"
}

response = requests.post(url, headers=headers, json=payload)

print("Status:", response.status_code)
print(response.text)