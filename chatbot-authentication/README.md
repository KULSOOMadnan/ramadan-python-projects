<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Chainlit + Gemini AI Chatbot</title>
</head>

<body>
    <h1>🤖 Chainlit + Gemini AI Chatbot</h1>

    <p>This project is an interactive chatbot using <strong>Chainlit</strong> and <strong>Google Gemini AI</strong>. It provides a seamless chat experience with OAuth support (e.g., GitHub authentication).</p>

    <h2>🚀 Features</h2>
    <ul>
        <li>Integrates Google Gemini AI for intelligent responses.</li>
        <li>Supports GitHub OAuth authentication.</li>
        <li>Maintains chat history across sessions.</li>
        <li>Handles real-time user messages and responses.</li>
    </ul>

    <h2>📦 Required Packages</h2>
    <pre><code>pip install chainlit google-generativeai python-dotenv</code></pre>

    <h2>📂 Project Structure</h2>
    <pre>
    ├── .env                # Store your Google API key
    ├── main.py             # Main chatbot script
    ├── requirements.txt    # Dependencies
    └── README.md           # Project documentation
    </pre>

    <h2>🔧 Setup Instructions</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/your-username/your-repo.git</code></pre>

        <li>Navigate to the project directory:</li>
        <pre><code>cd your-repo</code></pre>

        <li>Create a virtual environment (optional but recommended):</li>
        <pre><code>python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate</code></pre>

        <li>Install dependencies:</li>
        <pre><code>pip install -r requirements.txt</code></pre>

        <li>Set up your <code>.env</code> file with your Google Gemini API key:</li>
        <pre><code>GOOGLE_GEMINI_API_KEY=your_api_key_here</code></pre>

        <li>Run the chatbot:</li>
        <pre><code>chainlit run main.py</code></pre>
    </ol>

    <h2>📚 Usage</h2>
    <p>Once the chatbot is running, interact with it in your browser by navigating to the provided local URL. Authenticate with GitHub if required.</p>

    <h2>🤝 Contributing</h2>
    <p>Feel free to fork the project, open issues, and submit pull requests!</p>

    <h2>📜 License</h2>
    <p>MIT License</p>

</body>

</html>
