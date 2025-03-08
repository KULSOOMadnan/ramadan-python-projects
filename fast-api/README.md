# 🚀 FastAPI Side Hustle & Money Quotes API

Welcome to the **FastAPI Side Hustle & Money Quotes API**! This API provides random side hustle ideas and money-making quotes to inspire you. 🔥

## 📌 Technologies Used
- **FastAPI** ⚡
- **Uvicorn** 🚀
- **Python (random module)** 🎲

## 🔧 How It Works
This API has two endpoints:

### 1️⃣ `/side-hustle`
🔹 Returns a random **side hustle idea** from a predefined list.

#### Example Request:
```bash
GET /side-hustle?api_key=12345678
```
#### Example Response:
```json
{
  "side_hustles": "Freelance Writing - Start Offering your Writing Skills online!"
}
```
💡 **Note:** You must provide the correct API key (`12345678`) to access this endpoint.

---

### 2️⃣ `/money_quotes`
🔹 Returns a random **money-making quote** from a predefined list.

#### Example Request:
```bash
GET /money_quotes?api_key=7890
```
#### Example Response:
```json
{
  "money_quotes": "The only way to do great work is to love what you do. - Steve Jobs"
}
```
💡 **Note:** You must provide the correct API key (`7890`) to access this endpoint.

---

## ▶️ Running the API
Start the server using **Uvicorn**:
```bash
uvicorn filename:app --reload
```
📌 Replace `filename` with the actual Python file name containing the FastAPI app.

Once running, access the API documentation via Swagger UI:
- 📜 **Swagger UI:** `http://127.0.0.1:8000/docs`
- 📜 **Redoc UI:** `http://127.0.0.1:8000/redoc`

Happy Coding! 🚀💰
