# 📌 To-Do List CLI App (Python + UV) 🚀

A simple yet powerful **command-line To-Do List application** built using **Python and UV**. This tool allows users to **add, list, complete, and remove tasks** while storing them in a **JSON file for persistence**. Whether you're managing daily tasks or tracking work progress, this lightweight CLI app is your perfect productivity companion! ✅  

---

## 📦 Features  

✔️ **Add Tasks** – Quickly add tasks to your to-do list 📌  
✔️ **List Tasks** – View all your tasks with completion status 📋  
✔️ **Mark Tasks as Completed** – Keep track of what’s done ✅  
✔️ **Remove Tasks** – Delete tasks when no longer needed ❌  
✔️ **Persistent Storage** – Tasks are saved in a `JSON` file 🗂️  
✔️ **Fast & Lightweight** – Runs instantly in your terminal ⚡  

---

## 🛠️ Installation  

### 🔹 Prerequisites  
Make sure you have **Python 3.x** installed. You can check your Python version by running:  
```bash
python --version
```

# ⚙️ How It Works  

This To-Do List CLI app is designed to efficiently manage tasks using **Python and UV**. It operates through a **command-line interface (CLI)**, allowing users to interact with the application seamlessly.  

1️⃣ Tasks are stored in a JSON file (todo.json) for persistence.
2️⃣ The CLI commands interact with this file to add, list, complete, and remove tasks.
3️⃣ UV handles the command-line interface in an elegant way, making interactions simple and user-friendly.

---

## 🔹 Step-by-Step Workflow  

1️⃣ **User Inputs a Command**  
   - The user provides a command such as `add`, `list`, `complete`, or `remove`.  
   - Example:  
     ```bash
     uv todo add "Complete Python project"
     ```
   - The app receives the command and processes the request.  

2️⃣ **Tasks Are Stored in a JSON File**  
   - When a new task is added, it is saved in a `todo.json` file.  
   - Example JSON Structure:  
     ```json
     [
       {"task": "Complete Python project", "completed": false},
       {"task": "Read a book", "completed": false}
     ]
     ```
   - This ensures that tasks are **persistent** even after closing the app.  

3️⃣ **Listing Tasks**  
   - The `list` command retrieves and displays all tasks from the JSON file.  
   - Example:  
     ```bash
     uv todo list
     ```
   - **Output:**  
     ```
     📋 To-Do List:
     1. Complete Python project ❌
     2. Read a book ❌
     ```

4️⃣ **Marking a Task as Completed**  
   - When a user runs the `complete` command, the selected task is updated in the JSON file.  
   - Example:  
     ```bash
     uv todo complete 1
     ```
   - **Updated JSON:**  
     ```json
     [
       {"task": "Complete Python project", "completed": true},
       {"task": "Read a book", "completed": false}
     ]
     ```
   - **Updated List Output:**  
     ```
     📋 To-Do List:
     1. ✅ Complete Python project
     2. Read a book ❌
     ```

5️⃣ **Removing a Task**  
   - The `remove` command deletes a task from `todo.json`.  
   - Example:  
     ```bash
     uv todo remove 2
     ```
   - The app updates the JSON file and removes the specified task.  
   - **Updated List Output:**  
     ```
     📋 To-Do List:
     1. ✅ Complete Python project
     ```

---

## 🔹 Behind the Scenes  

- **Data Storage**: Tasks are stored in a JSON file (`todo.json`) instead of a database to keep it lightweight.  
- **Efficient CLI Interaction**: The **UV CLI framework** handles user commands elegantly.  
- **Fast Execution**: No unnecessary memory usage since the JSON file is only accessed when needed.  

---

## 🎯 Summary  

✅ **Persistent Storage** – All tasks are stored in a JSON file.  
✅ **User-Friendly Commands** – Simple CLI commands for managing tasks.  
✅ **Efficient Execution** – Only loads and modifies data when necessary.  
✅ **Minimal Resource Usage** – Lightweight and fast performance. 

---

This is how the **To-Do List CLI App** efficiently handles tasks while keeping everything simple and effective! 🚀  



##  🙌 Let's Connect!
If you found this useful, drop a ⭐ on GitHub, share your feedback, or connect with me!

💬 Let's build amazing things together!


