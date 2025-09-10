"""
Exercise 7: Complete API Test Agent
Your task: Integrate all components into a complete workflow
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME
from utils.sample_apis import SAMPLE_ENDPOINTS


class APITestAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=200)
        self.test_results = []

    def run_complete_analysis(self, api_endpoints):
        """
        TODO: Run complete analysis workflow
        Instructions for run_complete_analysis:
        - For each endpoint:
            1. Analyze the endpoint (use APIAnalyzer from previous exercises)
            2. Suggest test cases
            3. Generate test code
            4. Execute the test code
            5. Analyze the results
        - Collect and aggregate results for all endpoints
        - Calculate success rate and prepare a summary report
        - Use methods/classes from previous exercises (solutions 01-06)


        Args:
            api_endpoints: List of API endpoints to test

        Returns:
            Complete test report
        """
        # TODO: Implement complete workflow
        # TODO: Use methods from previous exercises
        # TODO: Collect results
        # TODO: Generate final report

        return {
            "total_endpoints": 0,
            "tests_run": 0,
            "success_rate": 0.0,
            "report": "TODO: Implement complete workflow"
        }

    def generate_executive_summary(self, test_results):
        """
        TODO: Generate executive summary using AI

        Args:
            test_results: Complete test results

        Returns:
            Executive summary string
        """
        # TODO: Create summary prompt
        # TODO: Make API call
        # TODO: Return formatted summary

        return "TODO: Implement executive summary"




def main():
    print("=== Solution 7: Complete API Test Agent ===")

    agent = APITestAgent(GEMINI_API_KEY)

    # Use sample endpoint
    endpoints = SAMPLE_ENDPOINTS[0]["endpoints"]

    print(f"Testing one endpoint...")
    print("=" * 60)

    # TODO: Run complete analysis
    results = agent.run_complete_analysis([endpoints[0]])

    print("\n" + "=" * 60)
    print("🎉 ANALYSIS COMPLETE!")
    print("=" * 60)

    print(f"\nTest Results Summary:")
    print(f"Endpoints analyzed: {results['total_endpoints']}")
    print(f"Tests executed: {results['tests_run']}")
    print(f"Successful tests: {results.get('successful_tests', 0)}")
    print(f"Failed tests: {results.get('failed_tests', 0)}")
    print(f"Success rate: {results['success_rate']:.1%}")

    # TODO: Generate executive summary
    print("\n" + "=" * 60)
    print("📊 EXECUTIVE SUMMARY")
    print("=" * 60)
    summary = agent.generate_executive_summary(results)
    print(summary)


if __name__ == "__main__":
    main()