### ⚙️ Installation Guide

##### Welcome to the installation guide for the Crypto Market Intelligence MCP project.

##### This guide has been written specifically for beginners while still following industry-standard practices. Whether you are a student, aspiring AI Engineer, recruiter, or software developer, the goal is to help you successfully install, configure, and run the complete application from start to finish.

##### Unlike many installation guides that assume prior experience, every step in this document explains not only *what* to do, but also *why* it is necessary. Understanding the reasoning behind each step will help you become a better software engineer rather than simply copying commands.

---

### 🎯 Installation Objectives

##### By the end of this guide you will have successfully:

- Installed every required software package.
- Downloaded the project from GitHub.
- Created an isolated Python environment.
- Installed every required Python package.
- Configured Databricks SQL Warehouse.
- Generated a Personal Access Token.
- Configured environment variables.
- Connected Claude Desktop to the MCP Server.
- Started the FastMCP server.
- Executed live SQL queries against Databricks.
- Passed all automated unit tests.
- Successfully asked Claude Desktop questions using live cryptocurrency market data.

---

### 🖥️ System Requirements

##### Before beginning the installation process, ensure your computer meets the minimum requirements.

| Component | Minimum |
|-----------|----------|
| Operating System | macOS, Windows 11 or Ubuntu |
| Python | 3.11 or newer |
| RAM | 8 GB |
| Recommended RAM | 16 GB |
| Internet | Stable broadband connection |
| Git | Latest version |
| Visual Studio Code | Latest version |

##### Although the project may run on older systems, these specifications provide the best experience when working with Databricks, Claude Desktop, and Python simultaneously.

---

### 📦 Required Software

##### Before cloning the project, install the following software.

| Software | Purpose |
|-----------|---------|
| Python | Primary programming language |
| Git | Version control |
| Visual Studio Code | Code editor |
| Claude Desktop | AI interface |
| Databricks Account | SQL Warehouse |
| Google Chrome | Access Databricks Workspace |

##### These tools form the foundation of the development environment.

---

### 🐍 Installing Python

##### Python is the primary programming language used throughout this project. It acts as the central orchestrator responsible for communicating with Databricks, reading SQL files, managing configuration, and exposing MCP tools.

##### Download Python from:

https://www.python.org

##### After installation, verify Python has been installed correctly.

Open a terminal and run:

```bash
python --version
```

Expected output:

```text
Python 3.11.x
```

##### If Python is not recognised, ensure it has been added to your system PATH.

---

### 🔧 Installing Git

##### Git is a distributed version control system used to track changes made to source code.

##### It enables collaboration, version history, branching, and publishing projects to GitHub.

Download Git:

https://git-scm.com

Verify installation:

```bash
git --version
```

Example:

```text
git version 2.xx.xx
```

---

### 💻 Installing Visual Studio Code

##### Visual Studio Code is the development environment used throughout this project.

##### VS Code provides syntax highlighting, debugging tools, Git integration, terminal access, and excellent Python support.

Recommended extensions:

- Python
- Pylance
- GitHub Copilot (Optional)
- Markdown Preview
- SQLite Viewer (Optional)

---

### 🤖 Installing Claude Desktop

##### Claude Desktop is the AI interface that communicates with the MCP Server.

##### Rather than storing cryptocurrency information internally, Claude dynamically retrieves information from Databricks whenever a user asks a question.

##### Install Claude Desktop from the official Anthropic website and ensure it launches successfully before continuing with the configuration steps.

---

### ☁️ Creating a Databricks Workspace

##### Databricks provides the cloud data warehouse used throughout this project.

##### If you do not already have a Databricks account, create one and set up a workspace. Once the workspace is ready, create a SQL Warehouse that will execute the project's SQL queries.

##### Throughout this guide, Databricks acts as the trusted source of cryptocurrency market data.

---

### 💡 Why These Tools?

##### Each application installed during this guide has a specific responsibility:

- Python executes the application.
- Git manages source code.
- Visual Studio Code provides the development environment.
- Claude Desktop provides the conversational AI interface.
- Databricks stores and processes enterprise data.

##### Together, these tools create a complete AI Engineering development environment capable of building intelligent applications that interact with live business data.
