"""
Solution 1: API Analyzer
Your task: Complete the missing method to analyze API endpoints
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME
from utils.sample_apis import get_sample_api


class APIAnalyzer:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=500)

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
                    parts=[types.Part.from_text(text = "You are an expert API analyst focused on testing scenarios.")]
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
    print("=== Solution 1: API Analyzer ===")

    # Get sample API
    sample_api = get_sample_api()
    endpoint = sample_api["endpoints"][0]

    print(f"Analyzing endpoint: {endpoint['method']} {endpoint['path']}")

    # Create agent instance
    agent = APIAnalyzer(GEMINI_API_KEY)

    # Analyze the endpoint
    analysis = agent.analyze_api_endpoint(endpoint)
    print(f"\nAnalysis: {analysis}")



if __name__ == "__main__":
    main()
