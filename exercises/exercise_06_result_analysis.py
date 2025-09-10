"""
Exercise 6: Test Execution Result Analysis
Your task: Execute generated test code safely and send results to the model
"""

import requests
import time
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
         Execute test code safely and capture results
         """
        try:
            # Create execution environment
            exec_globals = {
                '__builtins__': __builtins__,
                'requests': requests,
                'json': json,
                'time': time,
                'print': print
            }

            # Execute the code
            exec(test_code, exec_globals)

            # Look for the test function and execute it
            if 'test_api_endpoint' in exec_globals:
                result = exec_globals['test_api_endpoint']()
                return {
                    "execution_success": True,
                    "test_results": result,
                    "execution_time": time.time(),
                    "error": None
                }
            else:
                return {
                    "execution_success": False,
                    "test_results": None,
                    "error": "No test_api_endpoint function found in code"
                }

        except Exception as e:
            return {
                "execution_success": False,
                "test_results": None,
                "error": str(e)
            }

    def analyze_test_results(self, results):
        """
        TODO: Use AI to analyze test results and provide insights

        Args:
            results: Dict with test execution results

        Returns:
            String with AI analysis of results
        """
        # TODO: Create prompt for result analysis
        # TODO: Call the model
        # TODO: Return analysis

        return "TODO: Implement result analysis"

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

    results = engine.execute_test(test_code)

    print(f"\nExecution Results:")
    print(json.dumps(results, indent=2))

    # TODO: Analyze results with AI
    analysis = engine.analyze_test_results(results)
    print(f"\nAI Analysis: {analysis}")


if __name__ == "__main__":
    main()
