# Import required libraries
import streamlit as st           # For creating web interface
import pandas as pd               # For data manipulation and analysis
import datetime                   # For handling dates
import csv                       # For reading/writing CSV files
import os          # For file operations



# Define the CSV file path where mood data will be stored
MOOD_FILE = 'mood_log.csv'            

def Load_mood_data():                  
    # Function to load mood data from CSV file
    if not os.path.exists(MOOD_FILE):   # Check if file exists
        return pd.DataFrame(columns=['Date', 'Mood'])  # Return empty DataFrame if no file
    return pd.read_csv(MOOD_FILE , names=['Date', 'Mood'], header=0)  # Read and return existing data

def save_mood_data(date , mood):        # Function to save new mood entry
    with open(MOOD_FILE, "a") as file:  # Open file in append mode
        writer = csv.writer(file)       # Create CSV writer object
        writer.writerow([date, mood])   # Write the new mood entry


st.title("Mood Tracker")                # Display app title

today = datetime.date.today()           # Get current date
st.subheader(f"How are you feeling today ?")  # Display question subheader
mood = st.selectbox('Select Your Mood',['Happy', 'Sad', 'Angry', 'Stressed', 'Anxious', 'Neutral', 'Excited' , 'Tired' , ""])  # Create mood dropdown

if st.button('Log Mood'):               # When log button is clicked
    save_mood_data(today, mood)         # Save the mood data
    st.success(f"Mood logged for {mood}")  # Show success message

mood_data = Load_mood_data()            # Load existing mood data
if not mood_data.empty:                 # If data exists
    st.subheader('Mood Trends over Time ')  # Display trends section
    mood_data['Date'] = pd.to_datetime(mood_data['Date'])  # Convert dates to datetime objects
    
    mood_counts = mood_data.groupby('Mood').count()['Date']  # Count frequency of each mood
    st.bar_chart(mood_counts)           # Display bar chart of mood frequencies

else:                                   # If no data exists
    st.info("No mood data yet. Log your mood to see trends.")  # Show info message
