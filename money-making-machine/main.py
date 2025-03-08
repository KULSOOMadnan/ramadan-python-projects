# Import required libraries
import streamlit as st
import random
import requests
import time 

# Set the title of the web app
st.title('💰 Money Making Machine 💰')


# Function to generate a random amount of money between 1 and 1000
def generate_money():
    return random.randint(1, 1000)


# Create a section for generating instant cash
st.subheader('Instant Cash Generator 💵')
if st.button('Generate Cash'):
    st.write('Counting Your Money...')
    time.sleep(2)  # Add delay for effect
    amount = generate_money()
    st.success(f"You Made ${amount}!")


# Function to fetch side hustle ideas from API
def fetch_side_hustle():
    try:
        # Make API request with authentication
        response = requests.get("http://127.0.0.1:8000/side-hustle?api_key=12345678")
        if response.status_code == 200:
            hustles = response.json()
            return hustles['side_hustles']
        else:
            # Return default value if API call fails
            return 'Freelancing'
    except:
        st.error("Failed to fetch side hustle ideas")
       

# Create a section for side hustle ideas
st.subheader('Side Hustle Ideas 💡')
if st.button('Generate Side Hustle'):
    ideas = fetch_side_hustle()
    if ideas:
        st.markdown("### Here's Your Side Hustle Idea:")
        st.success(ideas)
    else:
        st.error("No side hustle ideas available")


# Function to fetch motivational money quotes from API    
def fetch_money_quotes():
    try:
        # Make API request with authentication
        response = requests.get("http://127.0.0.1:8000/money_quotes?api_key=7890")
        if response.status_code == 200:
            quotes = response.json()
            return quotes['money_quotes']
        else:
            # Return default quote if API call fails
            return 'Money is the root of all evil'
    except:
        st.error("Failed to fetch money quotes")
    
        
# Create a section for motivational money quotes
st.subheader('Motivational Money Quotes 💰')
if st.button('Generate Quote'):
    quote = fetch_money_quotes()
    if quote:
        st.markdown("### Here's Your Quote:")
        st.success(quote)
        
    else:
        st.error('No quotes available')
