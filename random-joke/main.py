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
            return "failed to get  joke .Please try again later."
    except:
        return "Why don't scientists trust atoms? Because they make up everything!"


def main():
    st.title("Random Joke Generator")
    st.write("Feeling down? Here are some jokes to brighten your day!")

    if st.button("Get a random joke"):
        setup, punchline = random_joke()
        st.write(f"**Joke:** {setup}")
        st.write(f"**Punchline:** {punchline}")

    # Add horizontal line
    st.divider()

    st.markdown("""
            <div style='text-align: center;'>
                <h2 style="">Want to hear another joke?</h2>
                <p>Click the button again to get another random joke</p>
            </div>
            <p> Made with   </p>
         , unsafe_allow_html=True)
                """)


main()
