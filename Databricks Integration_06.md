---

### ☁️ Databricks Integration

##### One of the biggest differences between beginner projects and enterprise AI applications is where the data comes from.

##### Many beginner projects read data from local CSV files or small SQLite databases stored on a personal computer. While this is perfectly acceptable for learning, enterprise applications rarely operate this way.

##### Large organisations store their information inside secure cloud platforms capable of handling millions or even billions of records. These cloud platforms provide scalability, security, reliability, collaboration, and high-performance analytics.

##### In this project, Databricks acts as the enterprise data platform responsible for storing and analysing cryptocurrency market information.

##### Rather than asking Claude to memorise cryptocurrency prices, Claude retrieves live business data directly from Databricks whenever a user asks a question.

---

### 🏢 What is Databricks?

##### Databricks is a cloud-based data platform built for modern Data Engineering, Data Analytics, Machine Learning, and Artificial Intelligence.

##### It combines several technologies into a single collaborative environment where data engineers, analysts, data scientists, and AI engineers can work together.

##### Databricks provides tools for:

- Data Engineering
- SQL Analytics
- Data Warehousing
- Data Science
- Machine Learning
- Artificial Intelligence
- Streaming Data
- Business Intelligence

##### Some of the world's largest organisations use Databricks to analyse enormous amounts of business data every day.

Examples include:

- Microsoft
- Shell
- HSBC
- Adobe
- Comcast
- Walgreens
- Rivian
- Regeneron

##### Learning Databricks therefore provides valuable experience directly applicable to enterprise environments.

---

### 🏛️ Why We Chose Databricks

##### Many different database technologies exist.

Examples include:

| Database | Common Usage |
|----------|---------------|
| SQLite | Local applications |
| MySQL | Websites |
| PostgreSQL | Enterprise applications |
| SQL Server | Business intelligence |
| Oracle | Banking |
| Snowflake | Cloud analytics |
| BigQuery | Google Cloud |
| Amazon Redshift | AWS |
| Databricks SQL Warehouse | AI + Data Engineering |

##### Databricks was selected because it combines cloud data warehousing with modern AI capabilities.

##### Since this project demonstrates AI Engineering, Databricks provides an excellent example of an enterprise-grade analytical platform.

---

### 🥇 Understanding the Medallion Architecture

##### Throughout this project we organised our data using the Medallion Architecture.

This consists of three layers:

```text
Raw Data
     │
     ▼
 Bronze
     │
     ▼
 Silver
     │
     ▼
 Gold
```

##### Each layer has a different responsibility.

---

### 🥉 Bronze Layer

##### The Bronze layer stores raw data exactly as it arrives from the original source.

Characteristics:

- Original records
- No cleaning
- No transformation
- Historical archive
- Easy recovery

Think of the Bronze layer as your raw ingredients before cooking.

---

### 🥈 Silver Layer

##### The Silver layer improves the raw data.

Typical tasks include:

- Removing duplicates
- Handling missing values
- Standardising column names
- Correcting data types
- Validating records
- Applying business rules

The Silver layer creates clean, reliable datasets ready for analysis.

---

### 🥇 Gold Layer

##### The Gold layer contains business-ready information.

Instead of storing raw transactions, it stores meaningful analytical views.

Examples:

- Top Gainers
- Top Losers
- Highest Volume
- Largest Market Cap
- Market Summary

##### Our MCP tools query **only** the Gold layer because it contains trusted business metrics that are ready for reporting and AI consumption.

---

### 🗄️ Creating a SQL Warehouse

##### Before Python can execute SQL queries, Databricks requires a SQL Warehouse.

##### A SQL Warehouse is a managed compute resource responsible for executing SQL statements efficiently.

Think of it as the "engine" that processes every SQL query sent from Python.

##### Inside Databricks:

1. Open **SQL Warehouses**
2. Click **Create SQL Warehouse**
3. Give it a meaningful name

Example:

```text
Crypto Market Warehouse
```

##### Recommended settings for learning:

- Starter Warehouse
- Auto Stop Enabled
- Serverless (if available)

##### Auto Stop reduces cloud costs by shutting down the warehouse when it is no longer in use.

---

### 🔑 Creating a Personal Access Token (PAT)

##### Python needs permission before it can communicate with Databricks.

Instead of entering your username and password every time, Databricks uses a Personal Access Token (PAT).

##### Think of a PAT as a secure digital key.

Instead of this:

```text
Username
Password
```

Python sends:

```text
Bearer eyJhbGciOi...
```

##### This token identifies your application and grants secure access to your Databricks workspace.

---

### 🛠️ Generating the Personal Access Token

##### Inside Databricks:

1. Click your profile icon.
2. Open **Settings**.
3. Select **Developer**.
4. Open **Access Tokens**.
5. Click **Generate New Token**.
6. Give the token a meaningful name.

Example:

```text
Crypto Market MCP
```

##### Copy the generated token immediately.

##### Databricks will only display it once.

##### Store the token securely inside your `.env` file.

---

### 🌐 Understanding the HTTP Path

##### Every SQL Warehouse has a unique HTTP Path.

##### The HTTP Path tells Databricks exactly which warehouse should execute your SQL queries.

Without it, Python would not know where to send requests.

Example:

```text
/sql/1.0/warehouses/xxxxxxxxxxxxxxxx
```

##### Copy this value from your SQL Warehouse settings.

---

### ⚙️ Configuring the .env File

##### Your `.env` file should now contain:

```text
DATABRICKS_SERVER_HOSTNAME=adb-xxxxxxxx.azuredatabricks.net

DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/xxxxxxxxxxxx

DATABRICKS_TOKEN=dapiXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

##### Never commit this file to GitHub.

Instead, include:

```text
.env
```

inside your `.gitignore`.

This prevents sensitive credentials from being published accidentally.

---

### 🧩 How Python Uses These Variables

##### The application loads the environment variables using:

```python
load_dotenv()
```

##### The configuration module retrieves each value.

Example:

```python
DATABRICKS_SERVER_HOSTNAME = os.getenv("DATABRICKS_SERVER_HOSTNAME")
```

##### Before running any SQL query, the project validates that every required variable exists.

This prevents confusing runtime errors later.

---

### 🔄 Communication Flow

The complete communication process now looks like this:

```text
Claude Desktop
        │
        ▼
FastMCP
        │
        ▼
Python
        │
        ▼
config.py
        │
        ▼
logger.py
        │
        ▼
Databricks REST API
        │
        ▼
SQL Warehouse
        │
        ▼
Gold Tables
        │
        ▼
JSON Response
        │
        ▼
Claude Desktop
```

##### Every question asked by the user follows this same journey through the system.

---

### ✅ Verifying the Connection

##### Before continuing, verify that Databricks is correctly configured.

Run one of your existing unit tests:

```bash
python -m pytest unit_tests/test_market_summary.py
```

##### If successful, you should see:

```text
=========================
1 passed
=========================
```

##### Alternatively, start the MCP server:

```bash
python server.py
```

##### Open Claude Desktop and ask:

> Give me a market summary.

##### If Claude returns live cryptocurrency data, the complete integration has been configured successfully.

---

### 💡 Key Takeaways

##### Databricks is much more than a database. It is a complete cloud platform designed for modern data engineering, analytics, machine learning, and AI.

##### By combining Databricks SQL Warehouse with the Model Context Protocol, this project demonstrates how AI systems can securely retrieve real-time enterprise data instead of relying on static knowledge.

##### This architecture reflects how many modern AI applications are built in production environments, making it a valuable project for anyone pursuing a career in AI Engineering, Data Engineering, or Cloud Analytics.
