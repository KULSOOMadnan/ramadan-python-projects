# Mood Tracker 📊

This is a simple **Mood Tracker** built using **Streamlit**, **Pandas**, and **CSV file handling**. It allows users to log their daily mood and visualize mood trends over time using a bar chart.

## Features ✨
- Select your mood from a dropdown menu ✅
- Save mood data with the current date 📅
- View mood trends over time with a **bar chart** 📊
- Stores data in a **CSV file** for persistence 💾

## Technologies Used 🛠️
- **Streamlit**: For building the web interface
- **Pandas**: For data manipulation and analysis
- **Datetime**: For handling date-related operations
- **CSV Module**: For reading and writing mood data
- **OS Module**: For file handling operations

## How It Works ⚙️

### 1. Import Required Libraries
```python
import streamlit as st
import pandas as pd
import datetime
import csv
import os
```
These libraries are used for building the web app, managing data, and storing mood logs.

### 2. Define Mood Data File
```python
MOOD_FILE = 'mood_log.csv'
```
A CSV file is used to store logged mood data.

### 3. Load Existing Mood Data
```python
def Load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=['Date', 'Mood'])
    return pd.read_csv(MOOD_FILE, names=['Date', 'Mood'], header=0)
```
- Checks if the `mood_log.csv` file exists.
- If not, returns an empty DataFrame.
- Otherwise, loads the existing data from the CSV file.

### 4. Save New Mood Entry
```python
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])
```
- Opens the CSV file in **append mode**.
- Saves the selected mood along with the **current date**.

### 5. Build Streamlit Web App UI
```python
st.title("Mood Tracker")
today = datetime.date.today()
st.subheader("How are you feeling today?")
```
- Displays the **title** of the app.
- Gets the **current date**.
- Asks the user to select their mood.

### 6. Mood Selection Dropdown
```python
mood = st.selectbox('Select Your Mood', ['Happy', 'Sad', 'Angry', 'Stressed', 'Anxious', 'Neutral', 'Excited', 'Tired', ""])
```
- Provides a **dropdown menu** with various mood options.

### 7. Log Mood Button
```python
if st.button('Log Mood'):
    save_mood_data(today, mood)
    st.success(f"Mood logged for {mood}")
```
- When clicked, saves the selected mood in the CSV file.
- Displays a success message confirming the logged mood.

### 8. Display Mood Trends
```python
mood_data = Load_mood_data()
if not mood_data.empty:
    st.subheader('Mood Trends over Time')
    mood_data['Date'] = pd.to_datetime(mood_data['Date'])
    
    mood_counts = mood_data.groupby('Mood').count()['Date']
    st.bar_chart(mood_counts)
else:
    st.info("No mood data yet. Log your mood to see trends.")
```
- Loads **previously logged moods**.
- Converts dates into **datetime objects** for accurate plotting.
- Groups moods and **counts occurrences**.
- Displays a **bar chart** visualizing mood trends.
- If no data exists, an **info message** is shown.

## Output Example 🖥️
1. **Log Mood Section**
   - Dropdown for selecting mood.
   - "Log Mood" button to save the selection.
   - Success message confirming the logged mood.

2. **Mood Trends Section**
   - Bar chart showing mood occurrences over time.
   - Message prompting users to log moods if no data is available.

## Conclusion 🎯
This **Mood Tracker** provides an easy way to log daily moods and track emotional patterns over time using simple **CSV-based storage** and a **Streamlit-powered UI**.

🚀 Try it out and take control of your emotions! 😊
