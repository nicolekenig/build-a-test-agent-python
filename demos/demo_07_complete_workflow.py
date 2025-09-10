"""
Demo 7: Complete Workflow - Shows all pieces working together
"""

import requests
import json
import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class MiniTestAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=100)

    def analyze_and_test(self, api_url):
        """Complete workflow: analyze → generate → execute → report"""

        print("🔍 Step 1: Analyzing API...")
        analysis = self._analyze_api(api_url)
        print(f"Analysis: {analysis}")

        print("\n💡 Step 2: Generating test...")
        test_plan = self._generate_test_plan(api_url)
        print(f"Test Plan: {test_plan}")

        print("\n🚀 Step 3: Executing test...")
        results = self._execute_test(api_url)
        print(f"Results: {json.dumps(results, indent=2)}")

        print("\n📊 Step 4: Generating report...")
        report = self._generate_report(results)
        print(f"Report: {report}")

        return results

    def _analyze_api(self, api_url):
        """Analyze what the API does"""
        prompt = f"API URL: {api_url}\nAnalyze what this API does in one sentence."
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "You are an API analyst. Analyze what this API does in one sentence.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )
        return response.text

    def _generate_test_plan(self, api_url):
        """Generate a simple test plan"""
        prompt = f"API URL: {api_url}\nGenerate a one-sentence test plan for this API."
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = "Generate a one-sentence test plan for this API.")]
                ),
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text = prompt)]
                )
            ],
            config=self.config
        )
        return response.text

    def _execute_test(self, api_url):
        """Execute the actual test"""
        try:
            response = requests.get(api_url, timeout=10)
            return {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response_time": response.elapsed.total_seconds(),
                "content_length": len(response.text)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def _generate_report(self, results):
        """Generate a summary report"""
        if results.get("success"):
            return f"✅ API test passed! Response time: {results.get('response_time', 0):.2f}s"
        else:
            return f"❌ API test failed: {results.get('error', 'Unknown error')}"


def main():
    print("=== Complete Workflow Demo ===")

    agent = MiniTestAgent(GEMINI_API_KEY)

    # Test a simple API
    api_url = "https://httpbin.org/get"

    print(f"Testing API: {api_url}")
    print("=" * 50)

    results = agent.analyze_and_test(api_url)

    print("=" * 50)
    print("🎉 Demo complete!")


if __name__ == "__main__":
    main()