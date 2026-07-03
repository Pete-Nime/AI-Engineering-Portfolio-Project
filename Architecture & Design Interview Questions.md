### 🏗️ Architecture & Design Interview Questions

##### In this chapter we explore some of the most common architecture and software engineering questions that interviewers ask when discussing portfolio projects.

##### Rather than memorising answers, focus on understanding the reasoning behind each design decision. Interviewers are usually more interested in *why* you made a decision than whether you chose a particular technology.

---

### ❓Question 1

## Why did you build this project?

##### 🎯 What the interviewer is testing

##### They want to understand whether you solved a real problem or simply followed an online tutorial.

##### 💬 Professional Answer

> I wanted to explore how modern AI systems can interact with enterprise data platforms rather than relying only on the language model's built-in knowledge. The project demonstrates how Claude Desktop can retrieve live cryptocurrency market information from Databricks using the Model Context Protocol. Along the way I also wanted to apply software engineering best practices such as modular architecture, automated testing, logging, configuration validation and documentation.

##### 👶 Explain Like I'm Five

##### Instead of making Claude remember everything, I taught Claude where to look for the latest information.

##### 🚀 Bonus Points

Mention that the same architecture could be reused for healthcare, finance, retail or logistics.

##### ⚠ Common Mistake

Do not answer:

> I just wanted to learn MCP.

Always explain the business value.

---

### ❓Question 2

## Why did you choose Python?

##### 🎯 What the interviewer is testing

##### They want to know whether your technology choice was intentional.

##### 💬 Professional Answer

> Python is widely used across AI Engineering, Data Engineering and Machine Learning. It has an excellent ecosystem, integrates well with Databricks and FastMCP, and allows rapid development while remaining highly readable. It also has mature libraries for APIs, testing, logging and cloud integrations.

##### 👶 Explain Like I'm Five

##### Python is like a Swiss Army knife.

It has a tool for almost everything.

##### 🚀 Bonus Points

Mention libraries such as:

- requests
- pytest
- python-dotenv
- FastMCP

---

### ❓Question 3

## Why did you use the Model Context Protocol?

##### 🎯 What the interviewer is testing

Do you actually understand MCP?

##### 💬 Professional Answer

> MCP provides a standard way for language models to communicate with external systems. Instead of embedding business logic inside Claude, MCP allows Claude to discover reusable tools and execute them when required. This creates cleaner separation between AI reasoning and application logic.

##### 👶 Explain Like I'm Five

##### Claude is smart.

But MCP gives Claude hands.

Now Claude can actually do work.

##### 🚀 Bonus Points

Mention that MCP reduces hallucinations because the model retrieves live information instead of guessing.

---

### ❓Question 4

## Why didn't you connect Claude directly to Databricks?

##### 🎯 What the interviewer is testing

Can you explain software architecture?

##### 💬 Professional Answer

> Directly connecting Claude to Databricks would tightly couple the AI model with the database. By introducing a Python application in the middle, we centralise authentication, logging, validation, error handling and business logic. This makes the system easier to maintain and extend.

##### 👶 Explain Like I'm Five

##### Instead of letting customers cook inside the kitchen,

we use waiters.

The waiter keeps everything organised.

---

### ❓Question 5

## Why did you separate SQL from Python?

##### 🎯 What the interviewer is testing

Software organisation.

##### 💬 Professional Answer

> SQL and Python solve different problems. SQL retrieves data while Python orchestrates application behaviour. Separating them improves maintainability, readability and collaboration because database specialists can optimise SQL without changing application logic.

##### 👶 Explain Like I'm Five

##### One person cooks.

One person serves.

Don't ask one person to do both jobs.

---

### ❓Question 6

## Why did you create market_tools?

##### 🎯 What the interviewer is testing

Can you organise software?

##### 💬 Professional Answer

> Every file inside market_tools performs one business capability. Instead of placing every query inside server.py, each tool has its own module, making the application modular and scalable.

##### 🚀 Bonus Points

Mention the Single Responsibility Principle.

---

### ❓Question 7

## Why did you create logger.py?

##### 🎯 What the interviewer is testing

Production readiness.

##### 💬 Professional Answer

> Logging allows developers to understand what the application is doing while it is running. Instead of using print statements, structured logging records timestamps, severity levels and useful debugging information. This becomes extremely valuable when diagnosing problems in production.

##### 👶 Explain Like I'm Five

##### Logging is like keeping a diary.

Every important thing the application does gets written down.

---

### ❓Question 8

## Why did you use environment variables?

##### 🎯 What the interviewer is testing

Security awareness.

##### 💬 Professional Answer

> Sensitive credentials should never be stored inside source code. Environment variables separate secrets from application logic, making the project more secure and easier to deploy across multiple environments.

##### 🚀 Bonus Points

Mention:

- Development
- Testing
- Production

---

### ❓Question 9

## Why did you write unit tests?

##### 🎯 What the interviewer is testing

Software quality.

##### 💬 Professional Answer

> Unit tests ensure that each MCP tool continues to behave correctly as the project evolves. Whenever I add a new feature or refactor code, I can immediately verify that existing functionality still works by running the automated test suite.

##### 👶 Explain Like I'm Five

##### Every time I fix my bicycle,

I quickly check the brakes,

the tyres,

and the chain.

That's exactly what unit tests do.

---

### ❓Question 10

## Why Databricks instead of PostgreSQL?

##### 🎯 What the interviewer is testing

Cloud knowledge.

##### 💬 Professional Answer

> PostgreSQL is an excellent relational database and would work well for many applications. I chose Databricks because this project demonstrates enterprise AI Engineering rather than traditional web development. Databricks provides cloud scalability, SQL Warehouses, Medallion Architecture, AI integration and modern analytics capabilities that align closely with enterprise data platforms.

##### 🚀 Bonus Points

Mention:

- Delta Lake

- SQL Warehouse

- Medallion Architecture

- Spark

---

### ❓Question 11

## Why FastMCP instead of building your own server?

##### 🎯 What the interviewer is testing

Framework selection.

##### 💬 Professional Answer

> FastMCP abstracts away much of the communication layer required by MCP. Rather than implementing the protocol manually, I could focus on business logic while still following the MCP standard. This reduced development time and produced cleaner, more maintainable code.

---

### ❓Question 12

## If you had another month, what would you improve?

##### 🎯 What the interviewer is testing

Can you think beyond the current version?

##### 💬 Professional Answer

> I would add authentication, caching, asynchronous query execution, GitHub Actions for automated testing, Docker support, deployment to Azure or AWS, additional market analytics tools, richer response formatting, and monitoring dashboards. I would also explore integrating vector search and Retrieval-Augmented Generation (RAG) for combining structured SQL data with unstructured market reports.

##### 🚀 Bonus Points

Mention CI/CD, Docker, Kubernetes, or cloud deployment if relevant to the role.

---

### 💡 Key Takeaways

##### Great interview answers focus on **why**, not just **what**.

##### When discussing your project, explain:

- The business problem.
- The architecture.
- The technologies.
- The engineering decisions.
- The trade-offs.
- Future improvements.

##### Interviewers are looking for engineers who can reason about software design, communicate clearly, and make thoughtful decisions—not just write code.
