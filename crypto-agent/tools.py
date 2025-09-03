import aiohttp

async def get_crypto_price(symbol: str) -> str:
    """Fetch real-time crypto price from Binance"""
    # Use the correct Binance API endpoint for ticker price
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return f"The current price of {symbol.upper()} is ${data['price']}"
                else:
                    return f"⚠️ Failed to fetch price. Status: {resp.status}. Try again later."
    except Exception as e:
        return f"⚠️ Error fetching price: {str(e)}"
