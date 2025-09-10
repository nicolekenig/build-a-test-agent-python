"""
Exercise 9: Generated Code Validation
Your task: Make sure the generated code is valid and executable
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
                    parts=[types.Part.from_text(
                        text="You are an expert Python developer. Generate clean, executable test code.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=prompt)]
                )
            ],
            config=self.config
        )

        return response.text

    def validate_generated_code(self, code):
        """
        TODO: Validate that generated code is syntactically correct

        Args:
            code: Generated Python code

        Returns:
            Tuple of (is_valid, error_message)
        """
        # TODO: Try to compile the code
        # TODO: Check for basic syntax errors
        # TODO: Return validation results

        return True, "TODO: Implement validation"


def main():
    print("=== Exercise 9: Generated Code Validation ===")

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

    # TODO: Validate the code
    is_valid, error = generator.validate_generated_code(code)

    if is_valid:
        print("\n✅ Code validation passed!")
    else:
        print(f"\n❌ Code validation failed: {error}")


if __name__ == "__main__":
    main()
