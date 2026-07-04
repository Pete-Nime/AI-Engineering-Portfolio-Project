import requests

url = "https://dbc-3019ec54-2294.cloud.databricks.com"

print("Connecting...")

try:
    r = requests.get(url, timeout=10)

    print("Connected!")
    print("Status Code:", r.status_code)

except Exception as e:
    print(e)