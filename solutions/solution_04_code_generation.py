"""
Solution 4: Test Code Generation
Your task: Generate Python test code
"""

import ast
import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class TestCodeGenerator:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=500)

    def generate_test_function(self, test_description, endpoint_info):
        """
        Generate executable Python test code
        """
        prompt = f"""
        Generate a Python test function for this scenario:

        Test Description: {test_description}
        API Method: {endpoint_info['method']}
        API Path: {endpoint_info['path']}
        Base URL: {endpoint_info.get('base_url', 'https://jsonplaceholder.typicode.com')}

        Requirements:
        - Use the requests library
        - Create a function named 'test_api_endpoint'
        - Include proper error handling with try/except
        - Return a dictionary with test results including:
          * 'success': boolean
          * 'status_code': HTTP status code
          * 'response_time': response time in seconds
          * 'error': error message if any
          * 'data': response data if successful
        - Include assertions where appropriate
        - Handle timeouts (set timeout=10)

        Return ONLY the Python function code, no explanation.
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an expert Python developer. Generate clean, executable test code.")]
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
    print("=== Solution 4: Test Code Generation ===")

    generator = TestCodeGenerator(GEMINI_API_KEY)

    # Test scenario
    test_description = "Test that GET /posts/1 returns a valid post with required fields (id, title, body, userId)"
    endpoint = {
        "method": "GET",
        "path": "/posts/1",
        "description": "Get specific post",
        "base_url": "https://jsonplaceholder.typicode.com"
    }

    print(f"Generating code for: {test_description}")

    # Generate test code
    code = generator.generate_test_function(test_description, endpoint)
    # Remove the python code wrapper
    code = code.strip().replace("```python", "").replace("```", "")

    print(f"\nGenerated Code:")
    print("=" * 50)
    print(code)
    print("=" * 50)



if __name__ == "__main__":
    main()
