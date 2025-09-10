"""
Solution 5: Test Execution Engine
Your task: Execute generated test code and capture results
"""

import requests
import json
import time
import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class TestExecutionEngine:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=300)

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


def main():
    print("=== Solution 5: Test Execution Engine ===")

    engine = TestExecutionEngine(GEMINI_API_KEY)

    # Sample test code to execute
    test_code = '''
import requests
import json
import time

def test_api_endpoint():
    """Test the JSONPlaceholder API"""
    start_time = time.time()

    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(url, timeout=10)

        response_time = time.time() - start_time

        if response.status_code == 200:
            data = response.json()

            results = {
                "success": True,
                "status_code": response.status_code,
                "response_time": response_time,
                "has_required_fields": all(field in data for field in ['id', 'title', 'body', 'userId']),
                "data_sample": {
                    "id": data.get('id'),
                    "title": data.get('title', '')[:50] + '...' if len(data.get('title', '')) > 50 else data.get('title', ''),
                    "userId": data.get('userId')
                }
            }
        else:
            results = {
                "success": False,
                "status_code": response.status_code,
                "response_time": response_time,
                "error": f"HTTP {response.status_code}"
            }

    except requests.exceptions.RequestException as e:
        results = {
            "success": False,
            "status_code": None,
            "response_time": time.time() - start_time,
            "error": str(e)
        }

    return results
'''

    print("Executing test code...")

    # Execute the test
    results = engine.execute_test(test_code)

    print(f"\nExecution Results:")
    print(json.dumps(results, indent=2))



if __name__ == "__main__":
    main()
