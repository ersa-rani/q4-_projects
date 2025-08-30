import os
import chainlit as cl
from dotenv import load_dotenv
import aiohttp

# Load API keys
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Validate API key
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is required")

# Gemini API configuration
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# --------------------------
# Welcome Message
# --------------------------
@cl.on_chat_start
async def start():
    """Send a welcome message when the chat starts."""
    welcome_message = """
🤖 **Welcome to the Urdu-English Translator Agent!**

I'm here to help you translate text between **English** and **Urdu**. Here's how I work:

• **English text** → I'll translate it to **Urdu**
• **Urdu text** → I'll translate it to **English**

Simply type your text and I'll automatically detect the language and translate it for you!

**Examples:**
- Type "Hello, how are you?" → I'll translate to Urdu
- Type "آپ کیسے ہیں؟" → I'll translate to English

Ready to start translating? Just type your message below! 🚀
    """
    
    await cl.Message(content=welcome_message).send()

# --------------------------
# Translator Agent Logic
# --------------------------
async def translate_text(text: str, target_lang: str = "ur") -> str:
    """
    Translate text between English and Urdu using Gemini API.
    target_lang = "ur" -> Urdu
    target_lang = "en" -> English
    """
    try:
        prompt = f"Translate the following text to { 'Urdu' if target_lang=='ur' else 'English'}:\n\n{text}"
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }
        
        url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    return result["candidates"][0]["content"]["parts"][0]["text"].strip()
                else:
                    error_text = await response.text()
                    return f"API Error: {response.status} - {error_text}"
                    
    except Exception as e:
        return f"Translation error: {str(e)}"

def is_urdu_text(text: str) -> bool:
    """
    Check if text contains Urdu characters.
    Uses a broader range to catch more Urdu characters.
    """
    urdu_ranges = [
        (0x0600, 0x06FF),  # Arabic
        (0x0750, 0x077F),  # Arabic Supplement
        (0x08A0, 0x08FF),  # Arabic Extended-A
        (0xFB50, 0xFDFF),  # Arabic Presentation Forms-A
        (0xFE70, 0xFEFF),  # Arabic Presentation Forms-B
    ]
    
    for start, end in urdu_ranges:
        if any(start <= ord(ch) <= end for ch in text):
            return True
    return False

# --------------------------
# Chainlit UI
# --------------------------
@cl.on_message
async def main(message: cl.Message):
    try:
        user_input = message.content.strip()
        
        if not user_input:
            await cl.Message(content="Please enter some text to translate.").send()
            return

        # Detect language using improved function
        if is_urdu_text(user_input):  
            # Urdu detected → translate to English
            result = await translate_text(user_input, target_lang="en")
        else:
            # English detected → translate to Urdu
            result = await translate_text(user_input, target_lang="ur")

        await cl.Message(content=result).send()
        
    except Exception as e:
        await cl.Message(content=f"An error occurred: {str(e)}").send()
