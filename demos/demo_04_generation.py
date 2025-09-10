"""
Demo 4: Test Code Generation - Shows how AI can generate code
"""

import google.genai as genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class HelloWorldCodeGenAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_name = GEMINI_MODEL_NAME
        self.config = types.GenerateContentConfig(max_output_tokens=100)

    def generate_hello_function(self, name):
        prompt = f"""
        Generate a Python function named 'hello_name' that takes a parameter 'name' and prints 'Hello, {{name}}!'.
        Return ONLY the function code, no explanation.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Content(role="user", parts=[types.Part.from_text(text=prompt)])
            ],
            config=self.config
        )
        return response.text

def main():
    print("=== Demo: Generate and Execute Hello World Function ===")
    agent = HelloWorldCodeGenAgent(GEMINI_API_KEY)
    name = "Gil"
    code = agent.generate_hello_function(name)
    print("Generated function code:\n")
    # Remove the python code wrapper
    print(code)

if __name__ == "__main__":
    main()