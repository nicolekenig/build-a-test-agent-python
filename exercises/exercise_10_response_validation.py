"""
Exercise 10: Response Validation
Your task: Validate the response structure of API calls using AI
"""

import requests
import json
import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class ResponseValidator:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=150)

    def validate_response_structure(self, response_data, expected_structure):
        """
        TODO: Validate API response structure using AI

        Args:
            response_data: Actual API response
            expected_structure: Expected response structure

        Returns:
            Dict with validation results
        """
        # TODO: Create validation prompt
        # TODO: Call the model
        # TODO: Parse validation results

        return {
            "is_valid": False,
            "issues": ["TODO: Implement structure validation"]
        }

def main():
    print("=== Exercise 10: Response Validation ===")

    validator = ResponseValidator(GEMINI_API_KEY)

    # Get sample response
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response_data = response.json()

    print(f"API Response: {json.dumps(response_data, indent=2)}")

    # Expected structure
    expected_structure = {
        "userId": "integer",
        "id": "integer",
        "title": "string",
        "body": "string"
    }

    # TODO: Validate structure
    validation_results = validator.validate_response_structure(response_data, expected_structure)

    print(f"\nValidation Results:")
    print(f"Valid: {validation_results['is_valid']}")
    if validation_results['issues']:
        print("Issues found:")
        for issue in validation_results['issues']:
            print(f"  - {issue}")


if __name__ == "__main__":
    main()
