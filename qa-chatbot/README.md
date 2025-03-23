<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Chainlit AI Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        code {
            background-color: #ddd;
            padding: 2px 5px;
            border-radius: 4px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <h1>Chainlit AI Chatbot</h1>
    <p>This project is a simple AI chatbot built using <strong>Chainlit</strong> and <strong>Google Gemini API</strong>. It allows users to chat with a language model and receive AI-generated responses.</p>

    <h2>Features</h2>
    <ul>
        <li>Uses <code>Chainlit</code> for interactive chat UI</li>
        <li>Integrates <code>Google Gemini API</code> for AI-generated responses</li>
        <li>Simple and easy to set up</li>
    </ul>

    <h2>Installation</h2>
    <p>To get started, install the required dependencies:</p>
    <pre><code>pip install chainlit google-generativeai python-dotenv</code></pre>

    <h2>Project Setup</h2>
    <p>Create a <code>.env</code> file in your project root and add your Google Gemini API key:</p>
    <pre><code>GOOGLE_GEMINI_API_KEY=your_api_key_here</code></pre>

    <h2>Running the Chatbot</h2>
    <p>Run the chatbot with the following command:</p>
    <pre><code>chainlit run your_script.py</code></pre>

    <h2>Code Overview</h2>
    <pre><code>
import os
from dotenv import load_dotenv
import chainlit as cl
import google.generativeai as genai

load_dotenv()

gemini_api_key = os.getenv('GOOGLE_GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name='gemini-2.0-flash')

@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello, how can I help you today?").send()

@cl.on_message
async def handle_message(message : cl.Message):
    prompt = message.content
    response = model.generate_content(prompt)
    response_x = response.text if hasattr(response, 'text') else ""
    await cl.Message(content=response_x).send()
    </code></pre>

    <h2>License</h2>
    <p>This project is open-source and available for use under the MIT license.</p>

</body>
</html>
