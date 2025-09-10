"""
Solution 6: Test Execution Result Analysis
Your task: Execute generated test code safely and send results to the model
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
        self.config = types.GenerateContentConfig(max_output_tokens=1500)

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
        Use AI to analyze test results and provide insights
        """
        prompt = f"""
        Analyze these API test results and provide insights:

        Execution Success: {results.get('execution_success', False)}
        Test Results: {json.dumps(results.get('test_results', {}), indent=2)}
        Error: {results.get('error', 'None')}

        Provide:
        1. Overall assessment (passed/failed/warning)
        2. Key findings
        3. Potential issues or concerns
        4. Recommendations for next steps

        Keep response concise and actionable.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an expert API test analyst. Provide clear, actionable insights.")]
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
    print("=== Solution 6: Test Execution Engine ===")

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

    analysis = engine.analyze_test_results(results)
    print(f"\nAI Analysis: {analysis}")


if __name__ == "__main__":
    main()
