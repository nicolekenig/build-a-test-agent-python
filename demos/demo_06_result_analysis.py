"""
Demo 6: Result analysis - Shows how to use AI to evaluate the response of as a test
"""

import requests
import json
import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


def simple_api_test():
    """A simple API test that we'll run"""
    print("Running simple API test...")

    # Test a simple GET request
    url = "https://httpbin.org/get"
    response = requests.get(url)

    result = {
        "status_code": response.status_code,
        "success": response.status_code == 200,
        "response_time": response.elapsed.total_seconds(),
        "data_received": len(response.text) > 0
    }

    print(f"Test Results: {json.dumps(result, indent=2)}")
    return result


def analyze_with_gemini(result):
    """Use Gemini to analyze the API test result"""
    client = genai.Client(api_key=GEMINI_API_KEY)
    model_name = GEMINI_MODEL_NAME
    config = types.GenerateContentConfig(max_output_tokens=300)
    prompt = f"""
    Here is the result of an API test:
    {json.dumps(result, indent=2)}
    
    Please analyze the result.
    Return a JSON object with key "success" (boolean) indicating if the test passed, and key "analysis_result" containing the whole analysis.
    """
    response = client.models.generate_content(
        model=model_name,
        contents=[
            types.Content(
                role="user",
                parts=[types.Part.from_text(text = "You are an expert API tester.")]
            ),
            types.Content(
                role="user",
                parts=[types.Part.from_text(text = prompt)]
            )
        ],
        config=config
    )
    result = response.text
    result = result.strip().replace("```json", "").replace("```", "")

    return result


def main():
    print("=== Code Execution Demo ===")

    # Run our test
    result = simple_api_test()

    # Analyze results
    if result["success"]:
        print("\n✅ Call SUCCEEDED!")
    else:
        print("\n❌ Call FAILED!")

    print(f"Response time: {result['response_time']:.2f} seconds")

    # Use Gemini to analyze the result
    print("\nGemini Analysis:")
    analysis = analyze_with_gemini(result)
    analysis_json = json.loads(analysis)
    if analysis_json["success"]:
        print("\n✅ Test PASSED!")
    else:
        print("\n❌ Test FAILED!")

    print(analysis_json["analysis_result"])


if __name__ == "__main__":
    main()
