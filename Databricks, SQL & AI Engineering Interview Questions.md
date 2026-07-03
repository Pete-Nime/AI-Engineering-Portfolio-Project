---

### ☁️ Databricks, SQL & AI Engineering Interview Questions

##### This section focuses on the cloud platform, SQL, and AI Engineering concepts demonstrated throughout the Crypto Market Intelligence MCP project. These questions assess your understanding of modern data platforms, cloud architecture, database design, and how Artificial Intelligence integrates with enterprise systems.

##### Rather than simply knowing SQL syntax, interviewers want to know whether you understand how enterprise systems store, process, secure, and serve business data.

---

### ❓Question 31

## Why did you choose Databricks?

##### 🎯 What the interviewer is testing

Can you justify your technology choices?

##### 💬 Professional Answer

> I selected Databricks because it is an enterprise cloud platform designed for Data Engineering, Data Analytics, Machine Learning, and AI workloads. Unlike a traditional database, Databricks provides scalable compute through SQL Warehouses, integrates well with modern cloud environments, supports the Medallion Architecture, and is widely used by enterprise organisations.

##### 👶 Explain Like I'm Five

##### Instead of keeping all my toys in one small box, I chose a huge organised warehouse where everything has its own place.

##### 🚀 Bonus Points

Mention:

- Delta Lake
- SQL Warehouse
- Spark
- Medallion Architecture

---

### ❓Question 32

## What is a SQL Warehouse?

##### 🎯 What the interviewer is testing

Cloud analytics knowledge.

##### 💬 Professional Answer

> A SQL Warehouse is a managed compute resource that executes SQL queries efficiently. It separates compute from storage, allowing organisations to scale query performance independently from the data itself.

##### 👶 Explain Like I'm Five

##### Think of a restaurant kitchen.

Customers place orders.

The kitchen prepares the meals.

The SQL Warehouse is the kitchen.

---

### ❓Question 33

## Explain the Bronze, Silver and Gold Architecture.

##### 🎯 What the interviewer is testing

Modern Data Engineering concepts.

##### 💬 Professional Answer

> The Medallion Architecture organises data into three layers. Bronze stores raw data exactly as received. Silver contains cleaned and validated data. Gold stores business-ready datasets used for reporting, dashboards, and AI applications. My MCP tools query the Gold layer because it contains trusted business metrics.

##### 👶 Explain Like I'm Five

##### It's like washing vegetables before cooking.

Bronze → Fresh from the garden.

Silver → Washed.

Gold → Ready to eat.

---

### ❓Question 34

## Why did you query the Gold layer?

##### 🎯 What the interviewer is testing

Data quality awareness.

##### 💬 Professional Answer

> The Gold layer contains validated, transformed, and business-ready information. Using this layer ensures that Claude retrieves reliable metrics instead of raw transactional data that may contain inconsistencies.

##### 🚀 Bonus Points

Mention:

- Reporting
- Dashboards
- AI applications

---

### ❓Question 35

## What is Delta Lake?

##### 🎯 What the interviewer is testing

Databricks knowledge.

##### 💬 Professional Answer

> Delta Lake is an open table format used by Databricks that adds reliability and advanced features to data lakes. It supports ACID transactions, schema enforcement, versioning, and time travel, making large-scale analytical workloads more reliable.

##### 👶 Explain Like I'm Five

##### Imagine saving every version of your homework.

If you make a mistake, you can always go back to an earlier copy.

---

### ❓Question 36

## Why didn't you store SQL inside Python?

##### 🎯 What the interviewer is testing

Code organisation.

##### 💬 Professional Answer

> Separating SQL from Python improves maintainability and collaboration. SQL specialists can optimise queries independently, while Python developers focus on application logic. This separation also keeps the codebase cleaner and easier to understand.

##### 👶 Explain Like I'm Five

##### One person writes recipes.

Another person cooks.

They work together without getting in each other's way.

---

### ❓Question 37

## Explain the Databricks REST API.

##### 🎯 What the interviewer is testing

Cloud integration.

##### 💬 Professional Answer

> The Databricks REST API provides a secure interface for applications to communicate with Databricks over HTTPS. My Python application sends SQL statements through this API, waits for execution to complete, and retrieves the results as JSON.

##### 🚀 Bonus Points

Mention:

- HTTPS
- Authentication
- JSON
- SQL execution

---

### ❓Question 38

## Why did you use a Personal Access Token (PAT)?

##### 🎯 What the interviewer is testing

Security.

##### 💬 Professional Answer

> A Personal Access Token provides secure authentication without embedding usernames or passwords inside the application. Tokens are easier to rotate, revoke, and manage, making them a safer authentication mechanism.

##### 👶 Explain Like I'm Five

##### Instead of giving someone the key to your whole house,

you give them a temporary visitor pass.

---

### ❓Question 39

## How does your SQL query reach Databricks?

##### 🎯 What the interviewer is testing

End-to-end understanding.

##### 💬 Professional Answer

> Claude selects an MCP tool. The tool loads the SQL file. Python sends the SQL through the Databricks REST API using the configured SQL Warehouse. Databricks executes the query against the Gold tables and returns the results as JSON.

##### 🚀 Bonus Points

Draw the architecture on a whiteboard if asked.

---

### ❓Question 40

## What happens after Databricks returns JSON?

##### 🎯 What the interviewer is testing

Data flow.

##### 💬 Professional Answer

> Python parses the JSON response, extracts the required information, and returns it to Claude Desktop. Claude then converts the structured data into a conversational response for the user.

##### 👶 Explain Like I'm Five

##### Databricks gives Python a neatly organised package.

Python hands it to Claude.

Claude explains it in simple English.

---

### ❓Question 41

## How would you optimise slow SQL queries?

##### 🎯 What the interviewer is testing

SQL optimisation.

##### 💬 Professional Answer

> I would first examine the execution plan to identify bottlenecks. Depending on the findings, I might optimise joins, reduce unnecessary columns, apply filters earlier, use appropriate indexes where applicable, reduce expensive aggregations, or redesign the query for better efficiency. I would also monitor warehouse sizing and query concurrency.

##### 🚀 Bonus Points

Mention:

- Execution plans
- Predicate pushdown
- Partition pruning
- Caching

---

### ❓Question 42

## What is a Window Function?

##### 🎯 What the interviewer is testing

Intermediate SQL.

##### 💬 Professional Answer

> A Window Function performs calculations across a group of related rows while preserving the individual rows. Unlike GROUP BY, it does not collapse the result set.

Examples include:

- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- NTILE()
- LAG()
- LEAD()

##### 👶 Explain Like I'm Five

##### Imagine every student keeps their own report card,

but the teacher also tells them their class ranking.

---

### ❓Question 43

## Why use SQL instead of Python for analytics?

##### 🎯 What the interviewer is testing

Technology selection.

##### 💬 Professional Answer

> SQL is specifically designed for querying and aggregating structured data efficiently within the database engine. Executing filtering and aggregation close to the data reduces unnecessary data transfer and improves performance.

##### 🚀 Bonus Points

Mention:

"Move computation to the data."

---

### ❓Question 44

## Why not use SQLite?

##### 🎯 What the interviewer is testing

Enterprise thinking.

##### 💬 Professional Answer

> SQLite is excellent for local applications and small projects, but it does not provide the scalability, collaboration, cloud integration, or distributed compute capabilities required for enterprise analytics. Databricks is more suitable for production-scale AI and data engineering workloads.

---

### ❓Question 45

## How would you secure this application?

##### 🎯 What the interviewer is testing

Security awareness.

##### 💬 Professional Answer

> I would secure the application by using environment variables for secrets, least-privilege access, encrypted communication over HTTPS, secure token rotation, authentication and authorisation, audit logging, monitoring, and regular dependency updates.

##### 🚀 Bonus Points

Mention:

- RBAC
- IAM
- Secret managers
- TLS encryption

---

### ❓Question 46

## How would this project handle millions of records?

##### 🎯 What the interviewer is testing

Scalability.

##### 💬 Professional Answer

> The architecture is designed to scale because Databricks distributes query execution across compute resources. Additional optimisations such as partitioning,
> caching, asynchronous execution, and larger SQL Warehouses can further improve performance.

##### 👶 Explain Like I'm Five

##### Instead of asking one person to sort one million letters,

you ask hundreds of people to sort them together.

---

### ❓Question 47

## What AI Engineering concepts does this project demonstrate?

##### 🎯 What the interviewer is testing

Can you connect the project to AI Engineering?

##### 💬 Professional Answer

> This project demonstrates retrieval-based AI, tool calling through the Model Context Protocol, cloud data integration,
> enterprise system orchestration, prompt interpretation, structured data retrieval, modular software design, and production engineering practices.
> Rather than treating the language model as the source of truth, the system retrieves live information from trusted enterprise data sources.

##### 🚀 Bonus Points

Mention future extensions such as:

- Retrieval-Augmented Generation (RAG)
- Vector databases
- AI agents
- Multi-agent orchestration
- Semantic search

---

### 💡 Key Takeaways

##### Modern AI Engineering is about much more than prompting language models. It involves integrating AI with cloud platforms, enterprise databases, 
secure APIs, scalable architectures, and reliable software engineering practices.

##### Throughout this project, Databricks, SQL, REST APIs, and the Model Context Protocol work together to create a system capable of delivering accurate, 
real-time business insights. Understanding these interactions demonstrates a strong foundation in both AI Engineering and modern data platforms.
