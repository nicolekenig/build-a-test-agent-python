"""
Demo 2: Test Idea Generation - Shows how AI can generate test scenarios
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class TestIdeaGenerator:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(
            max_output_tokens=300
        )

    def generate_test_ideas(self, api_description):
        """Generate test ideas for an API"""
        prompt = f"""
        API Description: {api_description}

        Generate ideas for tests that should be performed on this API.
        For each test, provide just the test name in this format:
        1. Test name here
        2. Test name here
        etc. 
        
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an expert API tester.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )
        return response.text


def main():
    print("=== Test Idea Generation Demo ===")

    generator = TestIdeaGenerator(GEMINI_API_KEY)

    # Simple API description
    api_description = "GET /users/{id} - Returns user information including name, email, and registration date"

    print(f"API: {api_description}")
    print("\nGenerating test ideas...")

    ideas = generator.generate_test_ideas(api_description)
    print(f"\nTest Ideas:\n{ideas}")


if __name__ == "__main__":
    main()
