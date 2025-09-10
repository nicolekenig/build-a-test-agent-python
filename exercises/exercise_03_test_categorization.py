"""
Exercise 3: Test Categorization
Your task: Split the test cases into different categories
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME
from utils.sample_apis import SAMPLE_ENDPOINTS


class TestCategorizer:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=200)

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
        # TODO: Call the mode and returned a categorized list

        return {
            "happy_path": ["TODO: Implement happy path tests"],
            "error_handling": ["TODO: Implement error tests"],
            "edge_cases": ["TODO: Implement edge case tests"]
        }




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
