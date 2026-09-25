import os
from dotenv import load_dotenv

load_dotenv()

FYERS_APP_ID = os.getenv("FYERS_APP_ID")
FYERS_SECRET_ID = os.getenv("FYERS_SECRET_ID")
FYERS_ACCESS_TOKEN = os.getenv("FYERS_ACCESS_TOKEN")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
TRADING_MODE = os.getenv("TRADING_MODE", "paper")
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")