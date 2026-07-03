### 🤖 Claude Desktop & Model Context Protocol (MCP) Configuration

##### One of the most exciting aspects of this project is that it allows Claude Desktop to communicate directly with your own Python application. Instead of only answering questions using its built-in knowledge, Claude can retrieve live information from enterprise systems such as Databricks through the Model Context Protocol (MCP).

##### This chapter explains how Claude Desktop discovers your MCP server, how the configuration file works, how Python is launched automatically, and how data flows between every component of the system.

---

### 🧠 What is Claude Desktop?

##### Claude Desktop is an Artificial Intelligence assistant developed by Anthropic.

##### Unlike traditional chatbots that only rely on the information contained within the language model, Claude Desktop supports the Model Context Protocol (MCP), allowing it to interact with external tools, databases, APIs, documents, and enterprise applications.

##### Think of Claude Desktop as the intelligent "front desk" of the application. It understands natural language, decides which tool is required, sends requests to the MCP server, and finally converts the returned data into a human-readable response.

##### Without Claude Desktop, users would need to manually execute Python scripts or write SQL queries themselves.

---

### 🔌 What is the Model Context Protocol (MCP)?

##### The Model Context Protocol (MCP) is an open standard that defines how Large Language Models communicate with external systems.

##### Rather than teaching the AI every possible piece of information in advance, MCP allows the AI to request information dynamically whenever it is needed.

##### This approach keeps responses current, reduces hallucinations, and allows AI systems to work with secure business data.

##### In this project, MCP enables Claude Desktop to communicate directly with our Python application.

---

### 🚀 Why Use MCP Instead of a Traditional API?

##### Traditional applications often require developers to build REST APIs before AI systems can access business data.

##### While REST APIs remain extremely important, MCP provides an additional abstraction layer specifically designed for AI applications.

##### Instead of Claude manually constructing HTTP requests, the MCP server exposes tools that Claude can discover and invoke automatically.

##### This results in a much simpler and more natural integration between AI models and external systems.

---

### 🗂️ Understanding `claude_desktop_config.json`

##### One of the most important files in the entire project is:

```text
claude_desktop_config.json
```

##### This file tells Claude Desktop which MCP servers should be started whenever Claude launches.

##### Think of this file as Claude's address book.

##### Without it, Claude has no idea that your Python application exists.

##### Every time Claude Desktop starts, it reads this configuration file, launches each registered MCP server, and waits for tools to become available.

---

### 📍 Where is the Configuration File Located?

##### The location depends on your operating system.

##### macOS

```text
~/Library/Application Support/Claude/claude_desktop_config.json
```

##### Windows

```text
%APPDATA%\Claude\claude_desktop_config.json
```

##### Linux

```text
~/.config/Claude/claude_desktop_config.json
```

##### If the file does not already exist, it can be created manually.

---

### 🧩 Understanding the Configuration File

##### A simplified configuration looks like this:

```json
{
  "mcpServers": {
    "crypto-market-intelligence": {
      "command": "/path/to/python",
      "args": [
        "/path/to/project/server.py"
      ]
    }
  }
}
```

##### Every section has a specific purpose.

| Property | Purpose |
|----------|---------|
| mcpServers | Lists all available MCP servers |
| crypto-market-intelligence | Friendly name displayed by Claude |
| command | Python executable used to launch the server |
| args | Python script to execute |

##### When Claude starts, it runs the command exactly as specified in this file.

---

### ⚙️ What Happens When Claude Starts?

##### The startup sequence follows these steps:

```text
User Opens Claude Desktop
            │
            ▼
Claude reads claude_desktop_config.json
            │
            ▼
Python Interpreter Starts
            │
            ▼
server.py Executes
            │
            ▼
FastMCP Server Starts
            │
            ▼
Tools Are Registered
            │
            ▼
Claude Discovers Available Tools
            │
            ▼
Ready for User Requests
```

##### This entire process usually completes in only a few seconds.

---

### 🐍 Why Does Claude Launch Python?

##### Claude Desktop does not execute SQL queries or communicate directly with Databricks.

##### Instead, Claude launches your Python application because Python contains all of the business logic required to perform those tasks.

##### Your Python application becomes the "brain" behind the AI assistant.

##### This separation keeps responsibilities clear:

- Claude understands language.
- Python performs business logic.
- Databricks stores business data.

---

### 🧰 How FastMCP Registers Tools

##### Inside `server.py`, every tool is decorated using the `@mcp.tool()` decorator.

Example:

```python
@mcp.tool()
def market_summary():
    return get_market_summary()
```

##### This decorator automatically registers the function as an MCP tool.

##### Once the server starts, Claude can discover and call this function whenever appropriate.

##### No additional API routing or HTTP endpoints are required.

---

### 🧭 How Claude Chooses a Tool

##### Suppose a user asks:

> Show me today's largest cryptocurrencies.

##### Claude analyses the request and determines that the most appropriate tool is:

```python
largest_market_cap()
```

##### Claude then invokes this tool automatically.

##### The developer does not need to manually instruct Claude which Python function to call.

---

### 🔄 Complete Request Flow

##### Every request follows the same architecture.

```text
User
 │
 ▼
Claude Desktop
 │
 ▼
FastMCP
 │
 ▼
server.py
 │
 ▼
largest_market_cap()
 │
 ▼
largest_market_cap.sql
 │
 ▼
Databricks SQL Warehouse
 │
 ▼
JSON Response
 │
 ▼
Python
 │
 ▼
Claude Desktop
 │
 ▼
Natural Language Response
```

##### This layered architecture makes the application easy to understand, test, and extend.

---

### 🧪 Verifying the Configuration

##### After configuring Claude Desktop, verify that everything is working correctly.

##### Start the MCP server:

```bash
python server.py
```

##### Restart Claude Desktop.

##### Ask:

> Show me today's top gainers.

##### If Claude returns live data from Databricks, the configuration has been completed successfully.

---

### ⚠️ Common Configuration Mistakes

##### Below are some of the most common issues developers encounter when configuring Claude Desktop.

| Problem | Cause | Solution |
|---------|-------|----------|
| Server not found | Incorrect path | Verify the Python and project paths. |
| No tools available | MCP server failed to start | Check the terminal for errors. |
| Permission denied | Incorrect Python executable | Verify the virtual environment path. |
| Invalid JSON | Missing comma or bracket | Validate the JSON syntax. |
| Claude cannot connect | Server not running | Restart Claude Desktop and the MCP server. |

##### These issues are normal during development and are usually resolved by checking file paths and configuration values.

---

### 💡 Best Practices

##### Follow these recommendations when working with MCP:

- Keep the configuration file clean and well-organised.
- Use meaningful names for MCP servers.
- Store credentials in environment variables rather than inside configuration files.
- Test the server after every significant change.
- Restart Claude Desktop after modifying the configuration.
- Use logging to monitor startup and tool execution.

---

### 🏁 Key Takeaways

##### The `claude_desktop_config.json` file acts as the bridge between Claude Desktop and your Python application. It tells Claude which MCP servers exist, how to start them, and where to find the corresponding Python code.

##### Once configured, Claude automatically launches your server, discovers your registered tools, and uses them to retrieve live business data whenever users ask questions.

##### Understanding this configuration is one of the most valuable skills when building modern AI applications because it demonstrates how language models can be safely and effectively integrated with enterprise systems.
