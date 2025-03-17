import streamlit as st
import requests

def random_joke():
    """Return a random joke from the API
    Returns:
        tuple: Contains the joke setup and punchline
    """
    try:
        response = requests.get(
            'https://official-joke-api.appspot.com/random_joke')
        if response.status_code == 200:
            joke = response.json()
            return joke['setup'], joke['punchline']
        else:
            return "Failed to get a joke. Please try again later.", ""
    except:
        return "Why don't scientists trust atoms?", "Because they make up everything!"

def main():
    # Custom CSS for Gradient Background and Styling
    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(to right, #ff9a9e, #fad0c4);
                font-family: Arial, sans-serif;
            }
            .main-title {
                text-align: center;
                font-size: 36px;
                color: white;
                font-weight: bold;
            }
            .joke-box {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
                margin-top: 20px;
            }
            .button-container {
                text-align: center;
            }
            .custom-button {
                background-color: #ff6f61;
                color: white;
                font-size: 20px;
                padding: 10px 20px;
                border-radius: 8px;
                border: none;
                cursor: pointer;
            }
            .custom-button:hover {
                background-color: #e65c50;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='main-title'> Random Joke Generator 🤣</h1>", unsafe_allow_html=True)
    st.markdown("### Feeling down? Here are some jokes to brighten your day!☀️")
    st.markdown(" ### Click the button below to get a random joke!")

    if st.button("😂 Get a Random Joke", key="joke_button"):
        setup, punchline = random_joke()
        st.markdown(f"""
            <div class='joke-box'>
                <h3>{setup} 🤔</h3>
                <p><strong>{punchline} 😆</strong></p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
            <div style='text-align: center;'>
                <h2>🔥 Want to hear another joke? 🔥</h2>
                <p>Click the button again to get another random joke!</p>
            </div>
            <p style='text-align: center;'> Made with ❤️ by a joke lover! </p>
            """, 
         unsafe_allow_html=True)

main()
