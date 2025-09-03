import chainlit as cl
import re
from tools import get_crypto_price

# Simple intent detection
def detect_intent(message: str) -> str | None:
    message = message.lower()
    if "btc" in message or "bitcoin" in message:
        return "BTC"
    if "eth" in message or "ethereum" in message:
        return "ETH"
    if "doge" in message or "dogecoin" in message:
        return "DOGE"
    return None

@cl.on_message
async def main(message: cl.Message):
    user_query = message.content
    symbol = detect_intent(user_query)

    if symbol:
        reply = await get_crypto_price(symbol)
    else:
        reply = "🤖 I can fetch prices for BTC, ETH, or DOGE. Try asking: 'What’s the price of BTC?'"

    await cl.Message(content=reply).send()
