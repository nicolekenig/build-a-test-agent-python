import os
from dotenv import load_dotenv

load_dotenv()

# Gemini Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = 'gemini-2.0-flash'

# Sample API endpoints for testing
SAMPLE_APIS = {
    "jsonplaceholder": "https://jsonplaceholder.typicode.com",
    "httpbin": "https://httpbin.org",
    "reqres": "https://reqres.in/api"
}

# Test configuration
TEST_TIMEOUT = 30
MAX_RETRIES = 3