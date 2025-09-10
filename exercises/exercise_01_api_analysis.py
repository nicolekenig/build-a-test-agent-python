"""
Exercise 1: API Analyzer
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
        self.config = types.GenerateContentConfig(max_output_tokens=100)

    def analyze_api_endpoint(self, endpoint_info):
        """
        TODO: Call the model to analyze an API endpoint

        Args:
            endpoint_info: Dict with 'method', 'path', 'description'

        Returns:
            String with analysis of what this endpoint does
        """
        # HINT: Create a prompt that asks the AI to analyze the endpoint
        # Consider what kind of testing might be needed

        # TODO: Add your analysis prompt here
        prompt = f"""
            
        """

        # TODO: Call the model and return the response
        return "TODO: Implement API analysis"




def main():
    print("=== Exercise 1: API Analysis Agent ===")

    # Get sample API
    sample_api = get_sample_api()
    endpoint = sample_api["endpoints"][0]

    print(f"Analyzing endpoint: {endpoint['method']} {endpoint['path']}")

    # TODO: Create agent instance
    agent = APIAnalyzer(GEMINI_API_KEY)

    # TODO: Analyze the endpoint
    analysis = agent.analyze_api_endpoint(endpoint)
    print(f"\nAnalysis: {analysis}")



if __name__ == "__main__":
    main()
