### 🏛️ Complete System Architecture

##### One of the most important aspects of software engineering is understanding how different components work together as a complete system. A well-designed architecture ensures that every part of the application has a clear responsibility, making the project easier to understand, maintain, test, and extend.

##### Rather than building one large Python script that performs every task, this project follows a modular architecture. Each file has a single responsibility, and every layer communicates with the next in a predictable and organized way.

##### This architecture closely resembles how modern AI applications are built in industry. Companies such as OpenAI, Microsoft, Databricks, Anthropic, AWS, and Google all separate responsibilities into multiple layers instead of placing everything inside a single application.

---

### 🧠 High-Level System Architecture

##### The diagram below illustrates how information flows through the complete application.

```text
                         ┌────────────────────────────┐
                         │        User                │
                         └─────────────┬──────────────┘
                                       │
                                       ▼
                         ┌────────────────────────────┐
                         │      Claude Desktop        │
                         │ (Natural Language Input)   │
                         └─────────────┬──────────────┘
                                       │
                                       ▼
                         ┌────────────────────────────┐
                         │        FastMCP Server      │
                         │        (server.py)         │
                         └─────────────┬──────────────┘
                                       │
             ┌─────────────────────────┼─────────────────────────┐
             ▼                         ▼                         ▼
   market_summary()          top_gainers()            top_losers()
             ▼                         ▼                         ▼
 highest_volume()        largest_market_cap()      Future Tools...
             │
             ▼
                  ┌────────────────────────────┐
                  │     Python Business Logic   │
                  │      (market_tools/)        │
                  └─────────────┬──────────────┘
                                │
                                ▼
                  ┌────────────────────────────┐
                  │        SQL Queries          │
                  │       (queries/)           │
                  └─────────────┬──────────────┘
                                │
                                ▼
                  ┌────────────────────────────┐
                  │    Databricks REST API      │
                  └─────────────┬──────────────┘
                                │
                                ▼
                  ┌────────────────────────────┐
                  │ Databricks SQL Warehouse    │
                  └─────────────┬──────────────┘
                                │
                                ▼
                  ┌────────────────────────────┐
                  │      Gold Layer Tables      │
                  └─────────────┬──────────────┘
                                │
                                ▼
                  ┌────────────────────────────┐
                  │      Query Results          │
                  └─────────────┬──────────────┘
                                │
                                ▼
                  ┌────────────────────────────┐
                  │ Claude Generates Response   │
                  └────────────────────────────┘
```

---

### 🚶 End-to-End Request Lifecycle

##### Understanding how a request travels through the system is essential for becoming an AI Engineer. Every user request follows the same lifecycle.

---

### Step 1 — User Asks a Question

##### The process begins when the user types a natural language question into Claude Desktop.

Example:

```text
Show me the top gaining cryptocurrencies today.
```

##### The user does not need to understand SQL, Databricks, APIs, or Python. They simply ask a question using everyday language.

---

### Step 2 — Claude Understands the Request

##### Claude analyses the user's prompt and determines which MCP tool is capable of answering the question.

For example:

| User Question | MCP Tool |
|---------------|----------|
| Show market summary | market_summary() |
| Top gainers | top_gainers() |
| Top losers | top_losers() |
| Highest volume | highest_volume() |
| Largest market cap | largest_market_cap() |

##### Claude does not execute SQL itself. Instead, it delegates the task to your MCP server.

---

### Step 3 — FastMCP Receives the Request

##### FastMCP acts as the communication layer between Claude Desktop and Python.

##### Each tool is registered using the `@mcp.tool()` decorator.

Example:

```python
@mcp.tool()
def top_gainers(limit: int = 10):
    return get_top_gainers(limit)
```

##### This tells FastMCP that the function is available for Claude to call whenever appropriate.

---

### Step 4 — Python Business Logic Executes

##### The request is forwarded to the appropriate file inside the `market_tools` directory.

Example:

```text
market_tools/
├── market_summary.py
├── top_gainers.py
├── top_losers.py
├── highest_volume.py
└── largest_market_cap.py
```

##### Each file has one responsibility. It loads the corresponding SQL query, validates configuration, logs the request, executes the query, and returns the results.

This follows the **Single Responsibility Principle**, one of the core principles of clean software design.

---

### Step 5 — SQL File is Loaded

##### Instead of embedding SQL directly inside Python, each query is stored in its own file.

Example:

```text
queries/
├── market_summary.sql
├── top_gainers.sql
├── top_losers.sql
├── highest_volume.sql
└── largest_market_cap.sql
```

##### Separating SQL from Python makes the project easier to maintain. Database specialists can modify SQL without touching Python code, while Python developers can improve the application without editing SQL.

---

### Step 6 — Databricks REST API

##### Once the SQL statement has been loaded, Python sends it to the Databricks SQL Warehouse using the Databricks REST API.

##### The API acts as a secure bridge between your application and the cloud data warehouse.

This process includes:

- Authentication using a Personal Access Token
- Sending the SQL statement
- Waiting for execution to complete
- Receiving the response as JSON

---

### Step 7 — Databricks SQL Warehouse

##### Databricks executes the SQL query against the Gold Layer tables.

These tables have already been cleaned, validated, and transformed through the Medallion Architecture, making them suitable for analytics and AI applications.

Because of this design, Claude always receives trusted, business-ready information.

---

### Step 8 — JSON Response

##### Databricks returns the query results as a structured JSON response.

Python parses the response and returns it to the MCP server.

Example (simplified):

```json
{
  "status": {
    "state": "SUCCEEDED"
  },
  "result": {
    "row_count": 10,
    "data_array": [
      ["Bitcoin", "BTC", 59713.0, 1197888395739.0]
    ]
  }
}
```

---

### Step 9 — Claude Generates the Final Response

##### Finally, Claude receives the structured data and transforms it into a natural language response that is easy for the user to understand.

For example:

> Bitcoin remains the largest cryptocurrency by market capitalization at approximately $1.20 trillion, followed by Ethereum at $191 billion.

The user never sees the SQL query or JSON response. They simply receive a clear, conversational answer.

---

### 📂 Project Folder Structure

```text
crypto_market_intelligence/
│
├── market_tools/
│   ├── market_summary.py
│   ├── top_gainers.py
│   ├── top_losers.py
│   ├── highest_volume.py
│   └── largest_market_cap.py
│
├── queries/
│   ├── market_summary.sql
│   ├── top_gainers.sql
│   ├── top_losers.sql
│   ├── highest_volume.sql
│   └── largest_market_cap.sql
│
├── unit_tests/
│   ├── test_market_summary.py
│   ├── test_top_gainers.py
│   ├── test_top_losers.py
│   ├── test_highest_volume.py
│   └── test_largest_market_cap.py
│
├── config.py
├── databricks_client.py
├── logger.py
├── server.py
├── requirements.txt
├── README.md
└── .env
```

---

### 🏗️ Why This Architecture?

##### This architecture follows several software engineering best practices:

- **Separation of Concerns** — each component has a single responsibility.
- **Modularity** — features are isolated into reusable modules.
- **Maintainability** — changes in one area have minimal impact on others.
- **Scalability** — new tools can be added without redesigning the system.
- **Testability** — each component can be tested independently.

These principles make the project easier to maintain as it grows.

---

### 🧒 Explain It Like I'm Five

##### Imagine a restaurant:

- The **customer** is the user.
- The **waiter** is Claude Desktop.
- The **restaurant manager** is the MCP server.
- The **chef** is the Python business logic.
- The **recipe book** is the SQL file.
- The **kitchen pantry** is the Databricks SQL Warehouse.
- The **finished meal** is the answer Claude gives back.

The customer doesn't need to know how the meal is prepared. They simply ask for food, and the restaurant works together behind the scenes to deliver it. 
This project follows the same idea: every component has a job, and together they produce the final result.

---

### 💡 Key Takeaways

##### Modern AI systems are much more than language models. They are composed of multiple layers that work together to deliver reliable, real-time answers.

##### By separating the application into Claude Desktop, FastMCP, Python tools, SQL queries, REST APIs, and Databricks SQL Warehouse, 
this project demonstrates a scalable and maintainable architecture suitable for real-world AI Engineering.

##### Understanding how data flows through these layers is one of the most valuable skills you can develop as an AI Engineer. 
It enables you to build systems that are not only intelligent, but also secure, maintainable, and capable of integrating with enterprise data platforms.
