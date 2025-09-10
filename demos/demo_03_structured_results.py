"""
Demo 3: Structured results - Shows how AI can return easily parsable responses
"""


import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME
import json

class StructuredAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(
            max_output_tokens=1000
        )

    def think(self, question):
        """Ask the AI to respond with a structured JSON result"""
        prompt = """
            You are a helpful API testing assistant. 
            Get me 3 areas to tests, 2 test examples and 2 notes for the given question.
            Reply in JSON format with keys: 'areas_to_test', 'test_examples', 'notes'."
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(role="user", parts=[types.Part.from_text(text=prompt)]),
                types.Content(role="user", parts=[types.Part.from_text(text=question)])
            ],
            config=self.config
        )
        try:
            answer = response.text.strip().replace("```json", "").replace("```", "")
            result = json.loads(answer)
        except Exception:
            result = {"error": "Failed to parse response as JSON", "raw_response": response.text}
        return result

def main():
    print("=== Structured Results Demo ===")
    agent = StructuredAgent(GEMINI_API_KEY)
    question = "What should I test when I have a REST API that manages user posts?"
    print(f"Question: {question}")
    print("\nAgent thinking...")

    answer = agent.think(question)

    print("\nStructured result:")
    for key, value in answer.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()