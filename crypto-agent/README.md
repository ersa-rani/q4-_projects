💹 Crypto Price Agent

An interactive AI-powered crypto assistant built with Python, Chainlit, and uv.
It fetches real-time Bitcoin (BTC), Ethereum (ETH), and Dogecoin (DOGE) prices from the Binance API, using lightweight intent detection + tool calling — just like a modern AI agent!

✨ Features

🧠 Detects user intent (BTC, ETH, DOGE) from natural language queries

🔌 Fetches live prices via the Binance public API

💬 Works in a chat-like interface with Chainlit

⚡ Managed with uv (no manual venv activation required)

🧰 Modular design (tools.py for API calls, main.py for logic)

📂 Project Structure
crypto-agent/
│── .env
│── main.py
│── tools.py
│── chainlit.md
│── README.md

⚡ Setup
1. Clone & enter project
git clone <your-repo-url>
cd crypto-agent

2. Install dependencies with uv
uv init --python 3.11
uv add chainlit aiohttp python-dotenv

3. Create .env file
BINANCE_API=https://api.binance.com/api/v3/ticker/price

▶️ Run the Agent
uv run chainlit run main.py -w


Open the Chainlit web interface in your browser, and chat with your crypto agent! 🎉

🗨️ Example Questions

“What’s the price of BTC right now?”

“Tell me the Ethereum price.”

“How much is DOGE?”

“Update me on Bitcoin.”

🔮 Next Steps

Add support for more coins (SOL, BNB, etc.)

Make responses more conversational with an LLM

Show historical charts with crypto trends

<img width="1089" height="633" alt="image" src="https://github.com/user-attachments/assets/559618e1-a7f6-4909-b733-32389b283f0a" />
