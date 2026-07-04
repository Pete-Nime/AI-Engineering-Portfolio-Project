### 🚀 Uploading a VS Code Project to GitHub (Beginner Friendly)

##### This guide explains every Git command we used to upload our Crypto Market Intelligence MCP project from VS Code to GitHub. Think of Git as your project's "save game" system and GitHub as your online backup where recruiters, teammates, and clients can view your work.

---

### 🧠 Imagine You're Building a LEGO House

##### Imagine you've spent weeks building an amazing LEGO house.

- Your **computer (VS Code)** is your bedroom where you're building it.
- **Git** is your notebook that records every change you make.
- **GitHub** is a museum where you proudly display your LEGO house for everyone to see.

Git helps move your project safely from your computer to GitHub.

---

### 📍 Step 1 — Check Where You Are

##### Before using Git, make sure you're inside the correct project folder.

```bash
pwd
```

##### What does it do?

- `pwd` means **Print Working Directory**.
- It tells you your current location.

Example:

```text
/Users/macbookpro/crypto_market_intelligence
```

##### Think of it like checking the address of your house before inviting someone over.

---

### 📍 Step 2 — Look at Your Project Files

```bash
ls
```

##### What does it do?

Lists every file and folder in your project.

Example:

```text
README.md
server.py
queries/
market_tools/
unit_tests/
```

##### Think of opening your toy box to see everything inside.

---

### 📍 Step 3 — Check Whether Git is Connected to GitHub

```bash
git remote -v
```

##### What does it do?

Shows which GitHub repository your project is connected to.

Example:

```text
origin https://github.com/Pete-Nime/AI-Engineering-Portfolio-Project.git (fetch)

origin https://github.com/Pete-Nime/AI-Engineering-Portfolio-Project.git (push)
```

##### Think of checking whether your house has a road leading to the museum.

---

### 📍 Step 4 — Connect Your Project to GitHub

##### If your project has never been connected before, connect it using:

```bash
git remote add origin https://github.com/Pete-Nime/AI-Engineering-Portfolio-Project.git
```

##### What does it do?

Creates the road between your computer and GitHub.

Without this connection Git doesn't know where to upload your project.

---

### 📍 Step 5 — Rename Your Branch

```bash
git branch -M main
```

##### What does it do?

Makes sure your main branch is called **main**.

Most GitHub repositories use **main** as the default branch.

##### Think of naming the main road to your house.

---

### 📍 Step 6 — Download Anything Already on GitHub

```bash
git pull origin main --allow-unrelated-histories
```

##### What does it do?

Downloads anything already stored on GitHub into your computer.

##### Why did we use `--allow-unrelated-histories`?

Because:

- GitHub already had files.
- Your computer already had different files.

This tells Git:

> "Please combine both projects instead of complaining."

Think of joining two LEGO houses together.

---

### 📍 Step 7 — Check What's Changed

```bash
git status
```

##### What does it do?

Shows everything Git has noticed.

Possible output:

```text
modified:

new file:

deleted:
```

or

```text
nothing to commit, working tree clean
```

##### This is like your teacher checking which homework pages you've completed.

---

### 📍 Step 8 — Tell Git to Prepare Everything

```bash
git add .
```

##### What does it do?

Stages every file for saving.

The `.` means:

> "Everything in this folder."

##### Think of putting every LEGO piece into a moving box.

---

### 📍 Step 9 — Save Your Progress

```bash
git commit -m "Complete Crypto Market Intelligence MCP project"
```

##### What does it do?

Creates a permanent snapshot of your project.

The message explains what you changed.

Examples:

```bash
git commit -m "Added Databricks integration"
```

```bash
git commit -m "Fixed unit tests"
```

```bash
git commit -m "Completed documentation"
```

##### Think of taking a photo of your LEGO house before changing it again.

---

### 📍 Step 10 — Upload Everything to GitHub

```bash
git push origin main
```

##### What does it do?

Uploads your saved project to GitHub.

After this command, everyone with access can see your latest work.

##### Think of delivering your LEGO house to the museum.

---

### 📍 Step 11 — Download Future Changes

If someone else changes the project:

```bash
git pull origin main
```

##### This downloads the newest version before you continue working.

---

### 📍 Step 12 — Check Everything is Clean

```bash
git status
```

You should see:

```text
On branch main

nothing to commit, working tree clean
```

##### This means:

✅ Everything has been saved.

✅ Everything has been uploaded.

✅ Your computer and GitHub are synchronized.

---

### 📍 Helpful Git Commands You'll Use Every Day

```bash
pwd
```

##### Shows where you currently are.

---

```bash
ls
```

##### Lists files in the current folder.

---

```bash
git status
```

##### Shows what has changed.

---

```bash
git add .
```

##### Stages all files.

---

```bash
git commit -m "Your message"
```

##### Saves your work locally.

---

```bash
git push origin main
```

##### Uploads everything to GitHub.

---

```bash
git pull origin main
```

##### Downloads the latest changes from GitHub.

---

```bash
git remote -v
```

##### Shows which GitHub repository you're connected to.

---

```bash
git log --oneline
```

##### Shows the history of all your commits.

---

```bash
git diff
```

##### Shows exactly what has changed before committing.

---

### 🎯 The Complete Git Workflow

##### Every time you work on your project, follow these steps:

```bash
git status
```

⬇️

```bash
git add .
```

⬇️

```bash
git commit -m "Describe what you changed"
```

⬇️

```bash
git push origin main
```

That's it!

---

### 🧠 Key Takeaways

##### Git is your project's memory.

##### GitHub is your project's online home.

##### VS Code is where you build your project.

##### `git add` prepares your files.

##### `git commit` saves your work.

##### `git push` uploads everything to GitHub.

##### `git pull` downloads the latest changes.

##### `git status` tells you exactly what's happening.

---

### 🏆 Final Analogy

##### Imagine writing a storybook.

- VS Code is your desk where you write.
- Git is the **Save** button.
- GitHub is your bookshelf in a public library.
- Every `commit` is a new edition of your book.
- Every `push` places the newest edition on the library shelf.
- Every `pull` brings home the latest edition if someone else has updated it.

Congratulations! 🎉

You now know the same Git workflow used every day by professional Software Engineers, Data Engineers, AI Engineers, and DevOps Engineers around the world.
