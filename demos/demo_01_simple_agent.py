"""
Demo 1: Simple AI Agent - Shows basic LLM interaction
Run this to understand how an AI agent thinks and responds
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class SimpleAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        # Set up the model name and configuration once
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(
            max_output_tokens=200
        )

    def think(self, question):
        """Ask the AI to think about something"""
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are a helpful API testing assistant.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = question)]
                )
            ],
            config=self.config
        )
        return response.text


def main():
    print("=== Simple AI Agent Demo ===")

    # Create our simple agent
    agent = SimpleAgent(GEMINI_API_KEY)

    # Ask it to think about APIs
    question = "What should I test when I have a REST API that manages user posts?"

    print(f"Question: {question}")
    print("\nAgent thinking...")

    answer = agent.think(question)
    print(f"\nAgent says: {answer}")


if __name__ == "__main__":
    main()