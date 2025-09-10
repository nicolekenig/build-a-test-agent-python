"""
Exercise 11: Detect anomalies
Your task: Identify anomalies in the response
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
        Validate API response structure using AI
        """
        prompt = f"""
        Validate this API response against the expected structure:

        ACTUAL RESPONSE:
        {json.dumps(response_data, indent=2)}

        EXPECTED STRUCTURE:
        {json.dumps(expected_structure, indent=2)}

        Check:
        1. Are all required fields present?
        2. Are the data types correct?
        3. Are there any unexpected fields?
        4. Are there any missing fields?

        Respond with:
        VALID: true/false
        ISSUES: list any problems found

        Be specific about what's wrong if validation fails.
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an API response validator. Be thorough and specific.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )

        content = response.text

        # Parse the response
        is_valid = "VALID: true" in content.lower() or "valid: true" in content.lower()

        # Extract issues
        issues = []
        lines = content.split('\n')
        capture_issues = False

        for line in lines:
            if 'ISSUES:' in line.upper() or 'PROBLEMS:' in line.upper():
                capture_issues = True
                # Check if issue is on the same line
                if ':' in line:
                    issue_text = line.split(':', 1)[1].strip()
                    if issue_text and issue_text.lower() != 'none':
                        issues.append(issue_text)
            elif capture_issues and line.strip():
                if line.strip().startswith('-') or line.strip().startswith('*'):
                    issues.append(line.strip()[1:].strip())
                elif not line.strip().startswith('VALID'):
                    issues.append(line.strip())

        return {
            "is_valid": is_valid,
            "issues": issues if issues else ([] if is_valid else ["Structure validation failed"])
        }


    def detect_anomalies(self, response_data):
        """
        TODO: Use AI to detect anomalies in API responses

        Args:
            response_data: API response to analyze

        Returns:
            List of detected anomalies
        """
        # TODO: Create anomaly detection prompt
        # TODO: Call the model
        # TODO: Parse anomalies

        return ["TODO: Implement anomaly detection"]


def main():
    print("=== Exercise 11: Response Validation ===")

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

    # TODO: Detect anomalies
    anomalies = validator.detect_anomalies(response_data)

    print(f"\nAnomalies Detected:")
    for anomaly in anomalies:
        print(f"  - {anomaly}")


if __name__ == "__main__":
    main()
