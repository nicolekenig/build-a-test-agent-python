"""
Exercise 2: API Analysis Agent
Your task: Complete the missing method to create test suggestions for the analyzed
            API endpoints
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME
from utils.sample_apis import get_sample_api


class APIAnalysisAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=100)

    def analyze_api_endpoint(self, endpoint_info):
        """
        Analyze an API endpoint and understand its purpose
        """
        prompt = f"""
        Analyze this API endpoint and explain what it does:

        Method: {endpoint_info['method']}
        Path: {endpoint_info['path']}
        Description: {endpoint_info['description']}

        Provide a concise analysis of:
        1. What this endpoint does
        2. What data it likely returns
        3. Common use cases
        4. Potential issues to test for

        Keep response under 150 words.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text="You are an expert API analyst focused on testing scenarios.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=prompt)]
                )
            ],
            config=self.config
        )
        return response.text

    def get_test_suggestions(self, endpoint_info):
        """
        TODO: Generate testing suggestions for an endpoint

        Args:
            endpoint_info: Dict with endpoint details

        Returns:
            List of testing suggestions
        """
        # TODO: Create prompt for test suggestions
        prompt = f"""

                """

        # TODO: Call the model and return suggestions as list
        return ["TODO: Implement testing suggestions"]


def main():
    print("=== Exercise 2: API Analysis Agent ===")

    # Get sample API
    sample_api = get_sample_api()
    endpoint = sample_api["endpoints"][0]

    print(f"Analyzing endpoint: {endpoint['method']} {endpoint['path']}")

    agent = APIAnalysisAgent(GEMINI_API_KEY)

    analysis = agent.analyze_api_endpoint(endpoint)
    print(f"\nAnalysis: {analysis}")

    # TODO: Get testing suggestions
    suggestions = agent.get_test_suggestions(endpoint)
    print(f"\nTesting Suggestions:")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion}")


if __name__ == "__main__":
    main()
