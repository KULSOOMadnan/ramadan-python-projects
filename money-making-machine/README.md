# 💰 Money Making Machine 💰

## 🚀 Project Overview
This is a **practice project** that integrates **FastAPI with Streamlit** to create an interactive web app that:

- 💵 **Generates instant cash** (randomized cash rewards)
- 💡 **Suggests side hustle ideas** (API-driven suggestions)
- 📢 **Displays motivational money quotes** (financial wisdom)

## 🛠 Tech Stack
- **FastAPI** ⚡ (Backend API)
- **Streamlit** 🎨 (Frontend UI)
- **Python Requests** 🌍 (Fetching API data)
- **Random & Time Modules** ⏳ (For logic & effects)

## 🔥 Features
### 1️⃣ Instant Cash Generator
- Click a button to generate a **random amount of money** between 1 and 1000.
- Uses the **random module** for randomness.
- Adds a **2-second delay** using the `time.sleep()` function for a realistic effect.

### 2️⃣ Side Hustle Idea Generator
- Calls the **FastAPI backend** to fetch a **random side hustle idea**.
- Uses an API **GET request** with authentication.
- Displays the response dynamically on the **Streamlit UI**.

### 3️⃣ Motivational Money Quotes
- Calls the **FastAPI backend** to fetch a **random money quote**.
- Uses an API **GET request** with authentication.
- Displays the response dynamically on the **Streamlit UI**.

## 🚀 How It Works
### 1️⃣ FastAPI Backend
The **FastAPI** backend provides two API endpoints:
- `/side-hustle?api_key=12345678` → Returns a **random side hustle idea**.
- `/money_quotes?api_key=7890` → Returns a **random motivational quote**.

Both endpoints require an **API key** for access.

### 2️⃣ Streamlit Frontend
- Calls the FastAPI backend using **requests.get()**.
- Displays the data in an interactive **web app**.
- Uses **buttons** to fetch and display new data.

## 📌 Running the Project
1. **Start FastAPI Server:**
   ```bash
   uvicorn main:app --reload
   ```
2. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

## 🎯 Key Learnings
✅ How to **integrate FastAPI with Streamlit**.
✅ Making **GET requests** and handling API responses.
✅ Using **random & time modules** for better UX.
✅ Displaying **real-time API data** dynamically.
✅ Improving UI with **interactive components**.

## 💡 Want to Learn More?
🔗 **GitHub Repo:** [Insert Repo Link]

A huge shoutout to **Sir Ashariba** for his guidance! 🙌

🚀 If you found this useful, drop a ⭐ on the repo!
