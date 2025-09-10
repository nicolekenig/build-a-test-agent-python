"""
Exercise 5: Test Execution Engine
Your task: Execute generated test code and capture results
"""

import json
import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class TestExecutionEngine:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=150)

    def execute_test(self, test_code, timeout=30):
        """
        TODO: Execute test code safely and capture results

        Args:
            test_code: Python code to execute
            timeout: Maximum execution time

        Returns:
            Dict with execution results
        """
        # TODO: Execute the test code
        # TODO: Format results properly
        # TODO: Handle execution errors

        return {
            "success": False,
            "error": "TODO: Implement test execution"
        }

def main():
    print("=== Exercise 6: Test Execution Engine ===")

    engine = TestExecutionEngine(GEMINI_API_KEY)

    # Sample test code to execute
    test_code = '''
import requests
import json

def test_api_endpoint():
    """Test the JSONPlaceholder API"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    results = {
        "status_code": response.status_code,
        "success": response.status_code == 200,
        "response_time": response.elapsed.total_seconds(),
        "has_title": "title" in response.json(),
        "has_body": "body" in response.json()
    }

    return results

# Execute the test
test_result = test_api_endpoint()
print(f"Test completed: {test_result}")
'''

    print("Executing test code...")

    # TODO: Execute the test
    results = engine.execute_test(test_code)

    print(f"\nExecution Results:")
    print(json.dumps(results, indent=2))



if __name__ == "__main__":
    main()
