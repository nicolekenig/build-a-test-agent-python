"""
Exercise 3: Test Categorization
Your task: Split the test cases into different categories
"""
from http.client import responses

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME
from utils.sample_apis import SAMPLE_ENDPOINTS
import json


class TestCategorizer:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=200)

    def think(self, prompt, question):
        """Ask the AI to respond with a structured JSON result"""
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


    def generate_test_categories(self, endpoint_info):
        """
        TODO: Generate different categories of tests

        Categories to consider:
        - Happy path tests
        - Error handling tests
        - Edge cases
        - Security tests
        - Performance tests

        Returns:
            Dict with test categories and ideas
        """
        # TODO: Create comprehensive prompt
        prompt = """
        Categories to consider: Happy path tests, Error handling tests, Edge cases, Security tests, Performance tests
        Reply in JSON format with keys: 'happy_path', 'error_handling', 'edge_cases', 'security', 'performance'.
        """
        question = f"Generate testing suggestions for this endpoint: {endpoint_info["method"], endpoint_info["path"], endpoint_info["description"]}. Keep response under 100 words. and close the json!"

        # TODO: Call the mode and returned a categorized list
        response = self.think(prompt,question)
        return response


def main():
    print("=== Exercise 3: Test Categorization ===")

    generator = TestCategorizer(GEMINI_API_KEY)

    # Use a more complex endpoint
    endpoint = SAMPLE_ENDPOINTS[0]["endpoints"][1]  # GET /posts/1

    print(f"Generating test categories for: {endpoint['method']} {endpoint['path']}")

    # TODO: Generate test categories
    categorized_tests = generator.generate_test_categories(endpoint)

    print("\nTest Ideas by Category:")
    for category, tests in categorized_tests.items():
        print(f"\n{category.upper()}:")
        for test in tests:
            print(f"  - {test}")


if __name__ == "__main__":
    main()
