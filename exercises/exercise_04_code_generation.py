"""
Exercise 4: Test Code Generation
Your task: Generate Python test code
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class TestCodeGenerator:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=200)

    def generate_test_function(self, test_description, endpoint_info):
        """
        TODO: Generate executable Python test code

        Args:
            test_description: What the test should do
            endpoint_info: API endpoint details

        Returns:
            String containing executable Python code
        """
        # TODO: Create prompt for code generation
        # Include requirements:
        # - Use requests library
        # - Include assertions
        # - Handle errors
        # - Return results

        prompt = f"""
        
        """

        # TODO: Call the model and extract code from re

        return "# TODO: Implement code generation"


def main():
    print("=== Exercise 4: Test Code Generation ===")

    generator = TestCodeGenerator(GEMINI_API_KEY)

    # Test scenario
    test_description = "Test that GET /posts/1 returns a valid post with required fields"
    endpoint = {
        "method": "GET",
        "path": "/posts/1",
        "description": "Get specific post",
        "base_url": "https://jsonplaceholder.typicode.com"
    }

    print(f"Generating code for: {test_description}")

    # TODO: Generate test code
    code = generator.generate_test_function(test_description, endpoint)

    print(f"\nGenerated Code:\n{code}")

if __name__ == "__main__":
    main()
