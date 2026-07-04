from databricks import sql
from dotenv import load_dotenv
import os
import time

load_dotenv()

HOST = os.getenv("DATABRICKS_SERVER_HOSTNAME")
HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")
TOKEN = os.getenv("DATABRICKS_TOKEN")

print("=" * 50)
print("Testing Databricks SQL Warehouse")
print("=" * 50)

print("HOST:", HOST)
print("HTTP PATH:", HTTP_PATH)
print("TOKEN LOADED:", bool(TOKEN))
print("TOKEN LENGTH:", len(TOKEN) if TOKEN else 0)

start = time.time()

try:
    print("\nConnecting...")

    connection = sql.connect(
        server_hostname=HOST,
        http_path=HTTP_PATH,
        access_token=TOKEN,
        timeout=30
    )

    print("Connected!")

    cursor = connection.cursor()

    cursor.execute("SELECT CURRENT_TIMESTAMP()")
    result = cursor.fetchall()

    print("\nSQL Test Result:")
    print(result)

    cursor.close()
    connection.close()

    print("\nFinished successfully!")

except Exception as e:
    print("\nConnection failed.")
    print("Error type:", type(e).__name__)
    print("Error message:", e)

finally:
    print("Elapsed:", round(time.time() - start, 2), "seconds")