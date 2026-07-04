from dotenv import load_dotenv
import os
import requests

load_dotenv()

token = os.getenv("DATABRICKS_TOKEN")

url = "https://dbc-3019ec54-2294.cloud.databricks.com/api/2.0/clusters/list"

headers = {
    "Authorization": f"Bearer {token}"
}

print("Testing Token...")

try:

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("✅ Token is VALID")

    else:
        print(response.text)

except Exception as e:
    print(e)