---

### 🧠 Python & Software Engineering Interview Questions

##### This section focuses on Python fundamentals and software engineering principles demonstrated throughout this project. While the application uses AI, Databricks, and MCP, the foundation of the system is still good software engineering.

##### Interviewers often use these questions to evaluate how you write maintainable, scalable, and readable code rather than simply checking whether your program runs successfully.

---

### ❓Question 13

## Explain the purpose of `server.py`.

##### 🎯 What the interviewer is testing

Can you explain the entry point of your application?

##### 💬 Professional Answer

> `server.py` is the entry point of the MCP application. Its responsibility is to initialise the FastMCP server and register every available tool using the `@mcp.tool()` decorator. It intentionally contains very little business logic because that responsibility belongs to the modules inside `market_tools`. This keeps the server lightweight and easy to maintain.

##### 👶 Explain Like I'm Five

##### Imagine a receptionist.

The receptionist doesn't do everyone's job.

The receptionist simply sends people to the correct office.

That's exactly what `server.py` does.

##### 🚀 Bonus Points

Mention the **Single Responsibility Principle**.

---

### ❓Question 14

## Why did you separate your project into multiple files?

##### 🎯 What the interviewer is testing

Project organisation.

##### 💬 Professional Answer

> Every file has one responsibility. Separating the project into modules improves readability, testing, maintenance, and scalability. If one module changes, the rest of the application is less likely to be affected.

##### 👶 Explain Like I'm Five

##### Instead of putting every tool into one giant toolbox,

I organised them into separate drawers.

Finding the right tool becomes much easier.

---

### ❓Question 15

## What are Python modules?

##### 🎯 What the interviewer is testing

Python fundamentals.

##### 💬 Professional Answer

> A module is simply a Python file containing reusable code. Modules allow developers to organise functionality into smaller components that can be imported wherever they are needed.

Example:

```python
from logger import logger
```

##### 👶 Explain Like I'm Five

##### Think of a module as a chapter in a book.

Every chapter teaches one topic.

---

### ❓Question 16

## What is a Python package?

##### 🎯 What the interviewer is testing

Project organisation.

##### 💬 Professional Answer

> A package is a collection of related Python modules organised inside a directory. Packages help organise larger projects into logical groups.

Example:

```text
market_tools/

market_summary.py

top_gainers.py

top_losers.py
```

##### 👶 Explain Like I'm Five

##### If modules are books,

packages are bookshelves.

---

### ❓Question 17

## Explain decorators.

##### 🎯 What the interviewer is testing

Intermediate Python knowledge.

##### 💬 Professional Answer

> A decorator modifies or extends the behaviour of a function without changing its implementation. In this project, FastMCP uses the `@mcp.tool()` decorator to register functions as MCP tools that Claude Desktop can discover automatically.

##### 👶 Explain Like I'm Five

##### Imagine putting a name tag on someone.

The person doesn't change.

Other people simply know their role.

---

### ❓Question 18

## Why did you use type hints?

##### 🎯 What the interviewer is testing

Code quality.

##### 💬 Professional Answer

> Type hints improve readability, IDE support, and static analysis by documenting the expected input and output types of functions. They make the code easier for both humans and tools to understand.

Example:

```python
def get_market_summary() -> dict | None:
```

##### 👶 Explain Like I'm Five

##### It's like writing labels on storage boxes.

Everyone knows what's inside.

---

### ❓Question 19

## Why did you write docstrings?

##### 🎯 What the interviewer is testing

Documentation.

##### 💬 Professional Answer

> Docstrings provide built-in documentation explaining the purpose, parameters, and return values of functions. They improve maintainability and allow documentation tools to generate reference material automatically.

##### 👶 Explain Like I'm Five

##### Every machine should come with an instruction manual.

Docstrings are instruction manuals for functions.

---

### ❓Question 20

## Explain `try` and `except`.

##### 🎯 What the interviewer is testing

Error handling.

##### 💬 Professional Answer

> `try` and `except` allow applications to recover gracefully from unexpected errors. Instead of crashing, the application logs the problem and continues operating where possible.

Example:

```python
try:
    result = run_sql(sql)
except Exception as error:
    logger.error(error)
```

##### 👶 Explain Like I'm Five

##### If you trip while walking,

you stand back up.

You don't stop walking forever.

---

### ❓Question 21

## Why use `requests`?

##### 🎯 What the interviewer is testing

API knowledge.

##### 💬 Professional Answer

> The `requests` library simplifies HTTP communication with external services. In this project it is responsible for sending SQL statements to the Databricks REST API and receiving JSON responses.

##### 🚀 Bonus Points

Mention GET, POST, headers, authentication, and JSON.

---

### ❓Question 22

## What is JSON?

##### 🎯 What the interviewer is testing

API fundamentals.

##### 💬 Professional Answer

> JSON (JavaScript Object Notation) is a lightweight data format used for exchanging structured information between applications. Databricks returns SQL results as JSON, which Python then parses before returning them to Claude Desktop.

##### 👶 Explain Like I'm Five

##### JSON is like a neatly organised shopping list.

Everything has a name and a value.

---

### ❓Question 23

## What is a REST API?

##### 🎯 What the interviewer is testing

Backend fundamentals.

##### 💬 Professional Answer

> A REST API is a standard method for applications to communicate over HTTP. In this project Python sends SQL requests to Databricks through its REST API and receives structured JSON responses.

##### 🚀 Bonus Points

Mention:

- GET
- POST
- PUT
- DELETE
- HTTP Status Codes

---

### ❓Question 24

## Why did you use a virtual environment?

##### 🎯 What the interviewer is testing

Python development practices.

##### 💬 Professional Answer

> Virtual environments isolate project dependencies, preventing conflicts between different Python projects and ensuring consistent package versions.

##### 👶 Explain Like I'm Five

##### Every project gets its own backpack.

Nothing gets mixed together.

---

### ❓Question 25

## Why use `requirements.txt`?

##### 🎯 What the interviewer is testing

Dependency management.

##### 💬 Professional Answer

> `requirements.txt` records every Python dependency required by the project, allowing other developers to recreate the same environment using a single installation command.

##### 👶 Explain Like I'm Five

##### It's like giving someone the exact shopping list they need.

---

### ❓Question 26

## Explain the Single Responsibility Principle.

##### 🎯 What the interviewer is testing

SOLID principles.

##### 💬 Professional Answer

> The Single Responsibility Principle states that every class, function, or module should have one reason to change. In this project each module performs a single responsibility, improving readability and maintainability.

##### 🚀 Bonus Points

Mention that `logger.py`, `config.py`, and `databricks_client.py` each perform one specific role.

---

### ❓Question 27

## What is DRY?

##### 🎯 What the interviewer is testing

Clean code principles.

##### 💬 Professional Answer

> DRY stands for "Don't Repeat Yourself." It encourages developers to avoid duplicating logic by creating reusable functions and modules.

##### 👶 Explain Like I'm Five

##### If you have to explain the same thing ten times,

write it down once instead.

---

### ❓Question 28

## What is KISS?

##### 🎯 What the interviewer is testing

Design philosophy.

##### 💬 Professional Answer

> KISS stands for "Keep It Simple, Stupid." Software should solve problems using the simplest design that meets the requirements rather than introducing unnecessary complexity.

---

### ❓Question 29

## What is YAGNI?

##### 🎯 What the interviewer is testing

Engineering judgement.

##### 💬 Professional Answer

> YAGNI means "You Aren't Gonna Need It." Developers should avoid building features before they are actually required. This keeps software simpler and reduces maintenance costs.

---

### ❓Question 30

## How would you scale this project?

##### 🎯 What the interviewer is testing

System design thinking.

##### 💬 Professional Answer

> I would introduce caching, asynchronous query execution, authentication, Docker containers, CI/CD pipelines, monitoring, cloud deployment, and additional MCP tools. For larger workloads I would also consider horizontal scaling and load balancing.

##### 👶 Explain Like I'm Five

##### If more people visit the shop,

hire more staff instead of making one person work harder.

---

### 💡 Key Takeaways

##### Strong Python engineers focus on more than syntax. They organise projects well, document their code, handle errors gracefully, write tests, and follow established software engineering principles.

##### Throughout this project we demonstrated these practices by separating responsibilities into modules, documenting functions with docstrings, validating configuration, logging important events, writing automated tests, and following clean architecture principles.

##### These habits make software easier to maintain, easier to scale, and easier for other developers to understand, which is why they are highly valued in professional engineering teams.
