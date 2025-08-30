🌐 Urdu ↔ English Translator Agent

A simple AI-powered translator agent built with Chainlit, Google Gemini API, and Python (async).
It automatically detects whether the input is in English or Urdu, and translates accordingly.

✨ Features

🔄 Auto-detects language (Urdu or English)

🌍 Bidirectional translation

⚡ Powered by Gemini 2.0 Flash

🎨 Interactive chat UI with Chainlit

🔐 Secure API key handling using .env

🛠️ Tech Stack

Chainlit
 – Chat UI framework

Google Gemini API
 – AI translation model

aiohttp
 – Async HTTP client

python-dotenv
 – Secure env handling

🚀 Getting Started
1️⃣ Clone the repo
git clone https://github.com/ersa-rani/q4-_projects/translator-agent.git
cd translator-agent

2️⃣ Create a virtual environment (with uv or venv)

Using uv:

uv init
uv add chainlit aiohttp python-dotenv


Or using pip:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3️⃣ Add API key

Create a .env file in the root:

GEMINI_API_KEY=your_gemini_api_key_here

4️⃣ Run the app
chainlit run translator_agent.py -w

💡 Usage

When you start the app, you’ll see a welcome message.

Examples:

Input:

Hello, how are you?


Output:

ہیلو، آپ کیسے ہیں؟


Input:

آپ کہاں رہتے ہیں؟


Output:

Where do you live?

📂 Project Structure
translator-agent/
│-- translator_agent.py   # Main agent logic
│-- .env                  # API key storage (not committed)
│-- requirements.txt      # Dependencies
│-- README.md             # Documentation

🔮 Future Improvements

Add OpenAI fallback if Gemini fails

Add voice-to-text translation

Deploy on Streamlit Cloud / Vercel for public access

📸 Demo Screenshot
<img width="1053" height="631" alt="image" src="https://github.com/user-attachments/assets/cae38f0d-4c9e-40d9-ad5c-6aa382b4eed3" />

