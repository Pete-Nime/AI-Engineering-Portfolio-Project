### 🛠️ Technology Stack

##### Every technology used in this project was selected for a specific purpose. Instead of choosing tools simply because they are popular, each component was carefully chosen to solve a particular problem within the overall architecture. One of the most important skills of an AI Engineer is understanding **why** a technology is used, **where** it fits into the system, and **when** another tool might be a better choice.

##### This chapter explains each technology used throughout the project, its purpose, its role in the overall architecture, and why it was selected over possible alternatives.

---

### 🐍 Python

##### Python is the primary programming language used throughout this project. It acts as the "brain" that connects Claude Desktop, the MCP Server, Databricks SQL Warehouse, configuration files, logging, and SQL execution.

##### Instead of embedding SQL directly inside Claude, Python provides an intermediate layer responsible for reading SQL files, validating configuration settings, communicating with Databricks, handling errors, and returning structured responses back to Claude.

##### Python was chosen because it has become the industry standard language for Artificial Intelligence, Machine Learning, Data Engineering, Data Science, and Automation.

##### One of Python's greatest strengths is its enormous ecosystem. Rather than building every component from scratch, developers can use thousands of well-tested libraries maintained by the global open-source community.

##### Throughout this project Python performs several responsibilities:

- Loading environment variables
- Starting the MCP server
- Reading SQL files
- Calling the Databricks REST API
- Returning query results
- Logging system events
- Handling unexpected errors
- Running automated unit tests

##### Without Python, every component of the project would have to communicate directly with each other, making the application significantly more difficult to maintain.

---

### 🤖 Claude Desktop

##### Claude Desktop serves as the intelligent user interface for this project.

##### Unlike traditional dashboards where users click buttons and filters, Claude allows users to communicate naturally using everyday English.

##### Instead of writing SQL, users simply ask questions such as:

> Show me today's top gainers.

##### Claude understands the request and automatically determines which MCP tool should execute.

##### Claude itself does **not** know cryptocurrency prices.

##### Instead, Claude knows **how to ask** your MCP Server for information.

##### This distinction is extremely important.

##### Large Language Models are excellent at understanding language, but enterprise applications require access to live business data stored outside the model.

##### MCP provides that missing connection.

---

### 🔌 Model Context Protocol (MCP)

##### The Model Context Protocol (MCP) is the core technology behind this project.

##### MCP is an open protocol that allows Large Language Models to securely interact with external systems such as databases, APIs, documents, cloud services, and business applications.

##### Instead of storing all information inside the AI model, MCP allows the model to retrieve information only when it is needed.

##### Think of MCP as a translator.

```
User
     ↓
Claude
     ↓
MCP
     ↓
Python Tool
     ↓
Database
```

##### This architecture provides several advantages:

- Live information
- Reduced hallucinations
- Modular design
- Enterprise scalability
- Better security
- Easier maintenance

##### Modern AI Engineering is moving rapidly toward MCP-style architectures because businesses require AI systems that interact with existing enterprise software rather than isolated chatbots.

---

### ⚡ FastMCP

##### FastMCP is the framework used to build the MCP server.

##### Its purpose is similar to what Flask or FastAPI provide for web applications.

##### Instead of building every communication protocol manually, FastMCP automatically manages communication between Claude Desktop and Python.

##### FastMCP allows developers to define reusable tools using decorators.

Example:

```python
@mcp.tool()
def top_gainers():
    ...
```

##### This decorator automatically exposes the Python function to Claude Desktop.

##### Whenever Claude decides this function should answer a question, FastMCP handles the communication automatically.

##### This dramatically reduces development time while making the code easier to maintain.

---

### 🏢 Databricks SQL Warehouse

##### Databricks SQL Warehouse is where all cryptocurrency data is stored and queried.

##### Instead of using local CSV files or SQLite databases, enterprise organizations often centralize analytical data inside cloud data warehouses.

##### Databricks SQL Warehouse provides:

- High-performance SQL execution
- Cloud scalability
- Secure authentication
- Large dataset support
- Multi-user access
- Integration with modern analytics platforms

##### Using Databricks makes this project much closer to a real production environment than using a local database.

---

### 🥉 Bronze, Silver and Gold Architecture

##### This project follows the Medallion Architecture, a widely adopted design pattern in modern Data Engineering.

##### Data flows through three layers:

Bronze Layer

- Raw data ingestion
- Minimal transformation
- Original source preserved

Silver Layer

- Cleaned data
- Validated records
- Standardized formats
- Business-ready datasets

Gold Layer

- Business metrics
- Aggregated tables
- Reporting datasets
- AI-ready analytical views

##### Our MCP tools query only the Gold layer.

##### This separation ensures the AI always works with trusted, business-quality information.

---

### 🗄️ SQL

##### SQL (Structured Query Language) is responsible for retrieving information from Databricks.

##### Instead of embedding SQL directly inside Python, every query is stored as an independent SQL file.

For example:

```
queries/
    market_summary.sql
    top_gainers.sql
    top_losers.sql
    highest_volume.sql
    largest_market_cap.sql
```

##### Separating SQL from Python provides several benefits:

- Easier maintenance
- Cleaner Python code
- Better collaboration
- Independent testing
- Simpler debugging

##### Database developers can modify SQL without changing Python code.

---

### 🌐 REST API

##### Python communicates with Databricks using a REST API.

##### REST (Representational State Transfer) is one of the most common communication standards used on the internet.

##### Rather than connecting directly to the database, Python sends secure HTTPS requests containing SQL statements.

##### Databricks executes the SQL and returns structured JSON responses.

##### Nearly every modern cloud platform—including OpenAI, Azure, AWS, Stripe, GitHub, and Google Cloud—uses REST APIs.

##### Learning REST APIs is therefore an essential skill for AI Engineers.

---

### 🔑 Environment Variables

##### Sensitive information should never be hard-coded into source code.

##### Instead, credentials are stored inside a `.env` file.

Examples include:

- Databricks Host
- SQL Warehouse HTTP Path
- Personal Access Token

##### Python loads these values securely using `python-dotenv`.

##### This approach improves security and allows the same application to run across different environments without modifying source code.

---

### 📋 Logging

##### Logging records what the application is doing while it is running.

##### Unlike `print()` statements, structured logging provides timestamps, severity levels, and consistent formatting.

##### This project uses centralized logging to record:

- Query execution
- Configuration validation
- Successful requests
- Failed requests
- Unexpected errors

##### Proper logging makes debugging significantly easier in production environments.

---

### ✅ Pytest

##### Automated testing ensures the application continues working as new features are added.

##### Rather than manually checking every MCP tool, Pytest executes all unit tests automatically.

##### Our test suite validates:

- SQL execution
- Returned data
- Expected response structure
- Tool reliability

##### Running one command:

```bash
python -m pytest unit_tests/
```

##### verifies the entire project within seconds.

---

### 🧩 Modular Architecture

##### One of the strongest design decisions in this project is modular architecture.

##### Each file has a single responsibility.

Examples include:

| File | Responsibility |
|------|----------------|
| server.py | MCP Server |
| config.py | Configuration |
| logger.py | Logging |
| databricks_client.py | Databricks communication |
| market_tools/ | Business logic |
| queries/ | SQL queries |
| unit_tests/ | Automated testing |

##### Small focused files are easier to understand, easier to test, and easier to maintain than one large file containing every piece of logic.

---

### 💡 Key Takeaways

##### Every technology used in this project solves a specific problem.

- Python orchestrates the application.
- Claude Desktop provides the AI interface.
- MCP connects AI with external systems.
- FastMCP exposes Python tools.
- Databricks stores enterprise data.
- SQL retrieves business information.
- REST APIs enable communication.
- Environment variables protect credentials.
- Logging improves maintainability.
- Pytest ensures reliability.
- Modular architecture keeps the project scalable.

##### Understanding **why** each technology exists is just as important as knowing **how** to use it. Recruiters, hiring managers, 
and clients are often more interested in your design decisions than the code itself. Being able to explain these choices confidently demonstrates a 
deeper understanding of AI Engineering and software architecture.
