from dotenv import load_dotenv
import os

load_dotenv()

print("=" * 50)
print("Testing .env")
print("=" * 50)

print("HOSTNAME :", os.getenv("DATABRICKS_SERVER_HOSTNAME"))
print("HTTP PATH:", os.getenv("DATABRICKS_HTTP_PATH"))

token = os.getenv("DATABRICKS_TOKEN")

if token:
    print("TOKEN     : Loaded Successfully")
    print("First 15 characters:", token[:15])
    print("Length:", len(token))
else:
    print("TOKEN NOT FOUND")