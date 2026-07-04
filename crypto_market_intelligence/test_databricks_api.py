from dotenv import load_dotenv
import os
import requests

load_dotenv()

HOST = os.getenv("DATABRICKS_SERVER_HOSTNAME")
TOKEN = os.getenv("DATABRICKS_TOKEN")
HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

print("=" * 50)
print("Databricks API Test")
print("=" * 50)

print("HOST:", HOST)
print("HTTP PATH:", HTTP_PATH)
print("TOKEN LOADED:", bool(TOKEN))

# Test 1: user identity
url = f"https://{HOST}/api/2.0/preview/scim/v2/Me"

try:
    response = requests.get(url, headers=headers, timeout=15)
    print("\nUser Identity Test")
    print("Status:", response.status_code)
    print(response.text[:500])
except Exception as e:
    print("Identity test error:", e)

# Test 2: SQL warehouses
url = f"https://{HOST}/api/2.0/sql/warehouses"

try:
    response = requests.get(url, headers=headers, timeout=15)
    print("\nSQL Warehouse Test")
    print("Status:", response.status_code)
    print(response.text[:1000])
except Exception as e:
    print("Warehouse test error:", e)