import streamlit as st  # Importing Streamlit for web app functionality
import random  # Importing random for selecting random questions
import time  # Importing time for adding delays

# Set page title and icon
st.set_page_config(page_title="Quiz App 🎓", page_icon="📜")

# Title and introduction
st.title("📜 Fun Quiz Application 🎉")
st.write("🧠 Test your knowledge with this exciting quiz! Answer the questions and see if you get them right. Let's go! 🚀")



# List of quiz questions with options and correct answers
quiz_questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Berlin", "Madrid", "Paris"],
        'answer': "Paris"
    },
    {
        'question': "What is 2 + 2?",
        'options': ["3", "4", "5"],
        'answer': "4"
    },
    {
        'question': "What is the largest planet in our solar system?",
        'options': ["Earth", "Jupiter", "Mars"],
        'answer': "Jupiter"
    },
    {
        'question': "What is the chemical symbol for water?",
        'options': ["H2O", "O2", "CO2"],
        'answer': "H2O"
    },
    {
        'question': "What is the main ingredient in guacamole?",
        'options': ["Tomato", "Avocado", "Onion"],
        'answer': "Avocado"
    },
    {
        'question': "What year did the Titanic sink?",
        'options': ["1912", "1905", "1898"],
        'answer': "1912"
    },
    {
        'question': "What is the smallest prime number?",
        'options': ["0", "1", "2"],
        'answer': "2"
    },
    {
        'question': "What is the hardest natural substance on Earth?",
        'options': ["Gold", "Diamond", "Iron"],
        'answer': "Diamond"
    },
    {
        'question': "What is the largest mammal in the world?",
        'options': ["Elephant", "Blue Whale", "Giraffe"],
        'answer': "Blue Whale"
    },
    {
        'question': "What is the currency of Japan?",
        'options': ["Yen", "Won", "Dollar"],
        'answer': "Yen"
    },
    {
        'question': "What is the main language spoken in Brazil?",
        'options': ["Spanish", "Portuguese", "English"],
        'answer': "Portuguese"
    },
    {
        'question': "What is the tallest mountain in the world?",
        'options': ["K2", "Kangchenjunga", "Mount Everest"],
        'answer': "Mount Everest"
    },
    {
        'question': "What is the largest ocean on Earth?",
        'options': ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"],
        'answer': "Pacific Ocean"
    },
    {
        'question': "What is the boiling point of water?",
        'options': ["100°C", "90°C", "80°C"],
        'answer': "100°C"
    },
    {
        'question': "What is the primary gas found in the air we breathe?",
        'options': ["Oxygen", "Carbon Dioxide", "Nitrogen"],
        'answer': "Nitrogen"
    },
    {
        'question': "What is the name of the longest river in the world?",
        'options': ["Amazon River", "Nile River", "Yangtze River"],
        'answer': "Nile River"
    },
    {
        'question': "What is the main ingredient in bread?",
        'options': ["Flour", "Sugar", "Salt"],
        'answer': "Flour"
    },
    {
        'question': "What planet is known as the Red Planet?",
        'options': ["Mars", "Venus", "Saturn"],
        'answer': "Mars"
    },
    {
        'question': "What is the largest continent on Earth?",
        'options': ["Africa", "Asia", "Europe"],
        'answer': "Asia"
    },
    {
        'question': "What is the name of the first man to walk on the moon?",
        'options': ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin"],
        'answer': "Neil Armstrong"
    },
    {
        'question': "What is the most widely spoken language in the world?",
        'options': ["English", "Mandarin", "Spanish"],
        'answer': "Mandarin"
    }
]

# Check if there is a current question in the session state
if "current_question" not in st.session_state:
    # If not, select a random question from the quiz questions
    st.session_state.current_question = random.choice(quiz_questions)
    st.success("🎉 A new question has been selected!")  # Display success message for new question
if "current_question" not in st.session_state:
    # If not, select a random question from the quiz questions
    st.session_state.current_question = random.choice(quiz_questions)

# Get the current question from the session state
question = st.session_state.current_question

# Display the current question as a subheader
st.subheader( f"🎯 {question['question']}")

# Create a dropdown for the user to select an answer
selected_options = st.radio('Choose your Answers', question['options'], key="answers")

# Check if the submit button is clicked
if st.button(' 🚀 Submit Answers'):
    # Check if the selected answer is correct
    if selected_options == question['answer']:
        st.success("✅ Correct! Great job! 🎉") # Display success message for correct answer
    else:
        st.error('❌ Incorrect! The Correct Answer is ' + str(question['answer']))  # Display error message for incorrect answer
    
    time.sleep(3)  # Pause for 3 seconds before proceeding
    
    # Select a new random question for the next round
    st.session_state.current_question = random.choice(quiz_questions)
    
    st.rerun()  # Rerun the app to refresh the question

