---

### 📥 Cloning the Repository

##### Once all prerequisite software has been installed, the next step is to download the project source code from GitHub.

##### Cloning a repository creates a complete copy of the project on your local computer. This includes every Python file, SQL query, configuration file, documentation file, and project history stored in Git.

##### Open a terminal and navigate to the directory where you would like to store the project.

Example:

```bash
cd ~/Documents/GitHub
```

##### Clone the repository.

```bash
git clone https://github.com/<your-github-username>/crypto_market_intelligence.git
```

##### Replace `<your-github-username>` with your own GitHub username.

##### Once downloaded, navigate into the project folder.

```bash
cd crypto_market_intelligence
```

##### Verify the repository was downloaded successfully.

```bash
ls
```

Expected output:

```text
README.md
requirements.txt
server.py
config.py
logger.py
market_tools/
queries/
unit_tests/
docs/
```

##### Seeing these files confirms that the repository has been cloned successfully.

---

### 📁 Understanding the Project Structure

##### Before running the project, it is important to understand how it has been organised.

##### A well-structured project is easier to maintain, easier to understand, and significantly easier to expand in the future.

```text
crypto_market_intelligence/

│
├── docs/
│
├── market_tools/
│
├── queries/
│
├── unit_tests/
│
├── server.py
├── config.py
├── logger.py
├── databricks_client.py
├── requirements.txt
├── README.md
└── .env
```

##### Each folder has a dedicated responsibility.

| Folder | Responsibility |
|---------|----------------|
| docs | Project documentation |
| market_tools | Business logic |
| queries | SQL files |
| unit_tests | Automated testing |
| server.py | FastMCP Server |
| config.py | Environment configuration |
| logger.py | Central logging |
| databricks_client.py | Databricks communication |

##### Organising software in this way follows the Single Responsibility Principle, making future development significantly easier.

---

### 🐍 Creating a Python Virtual Environment

##### One of the most important best practices in Python development is using a virtual environment.

##### A virtual environment creates an isolated Python installation specifically for this project.

##### Without a virtual environment, Python packages installed for one project could accidentally affect another project.

##### Think of a virtual environment as giving every project its own toolbox.

##### Create a virtual environment by running:

```bash
python -m venv .venv
```

##### Explanation:

| Command | Purpose |
|----------|----------|
| python | Starts Python |
| -m | Runs a Python module |
| venv | Creates a virtual environment |
| .venv | Name of the environment folder |

##### After running this command, a new folder named `.venv` will appear inside the project.

---

### ▶️ Activating the Virtual Environment

##### Before installing any packages, the virtual environment must be activated.

##### macOS / Linux

```bash
source .venv/bin/activate
```

##### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

##### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

##### Once activated, your terminal should display something similar to:

```text
(.venv)
```

##### This indicates that every Python package installed from this point onward will remain isolated within this project.

---

### 📦 Installing Project Dependencies

##### This project relies on several third-party Python libraries.

##### Rather than installing each package individually, Python uses a file named `requirements.txt`.

##### This file lists every dependency required for the project.

Install all dependencies by running:

```bash
pip install -r requirements.txt
```

##### Depending on your internet connection, installation may take several minutes.

##### Once complete, verify the installation.

```bash
pip list
```

##### You should see packages similar to:

```text
fastmcp
python-dotenv
requests
pytest
```

##### The exact versions may differ slightly depending on when the project is installed.

---

### 📄 Understanding requirements.txt

##### One of the first files recruiters often inspect is `requirements.txt`.

##### This file allows anyone to recreate the exact Python environment used during development.

Example:

```text
fastmcp
python-dotenv
requests
pytest
```

##### Each package provides specific functionality.

| Package | Purpose |
|----------|----------|
| fastmcp | MCP Server framework |
| python-dotenv | Loads environment variables |
| requests | REST API communication |
| pytest | Automated testing |

##### By storing dependencies inside a single file, new developers can set up the project using a single command rather than manually installing every package.

---

### 🔐 Creating the Environment File

##### Sensitive information should never be stored directly inside Python source code.

##### Instead, credentials are stored inside a hidden file named `.env`.

##### Create a file named:

```text
.env
```

##### Inside the file, add:

```text
DATABRICKS_SERVER_HOSTNAME=your-workspace-hostname
DATABRICKS_HTTP_PATH=your-sql-http-path
DATABRICKS_TOKEN=your-personal-access-token
```

##### Replace each placeholder with your own Databricks values.

##### Never upload your real `.env` file to GitHub.

##### Instead, include `.env` inside your `.gitignore` file.

This protects your credentials from accidental exposure.

---

### 🛡️ Why Environment Variables Matter

##### Hard-coding secrets inside Python files is considered a serious security risk.

Instead of writing:

```python
TOKEN = "abc123..."
```

##### We store secrets separately.

```text
.env
```

##### Then load them securely.

```python
load_dotenv()
```

##### This allows the same codebase to be deployed across development, testing, and production environments without modifying the source code.

##### Environment variables are considered an industry-standard approach for managing sensitive configuration values.

---

### ✅ Installation Progress Checklist

At this stage you should have successfully completed the following tasks:

- ✅ Installed Python
- ✅ Installed Git
- ✅ Installed Visual Studio Code
- ✅ Installed Claude Desktop
- ✅ Created a Databricks Workspace
- ✅ Cloned the repository
- ✅ Created a virtual environment
- ✅ Activated the virtual environment
- ✅ Installed all Python dependencies
- ✅ Created the `.env` file
- ✅ Configured environment variables

##### Congratulations! Your development environment is now ready. In the next section, we will connect the project to Databricks, generate a Personal Access Token (PAT), configure the SQL Warehouse, and verify that the application can successfully communicate with your cloud data platform.
