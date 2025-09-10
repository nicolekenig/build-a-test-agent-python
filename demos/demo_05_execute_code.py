"""
Demo 5: Code execution - Shows how AI can generate code,
        how to run it and extract results from it
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
    # Remove the python code wrapper
    code = code.strip().replace("```python", "").replace("```", "")

    print("Generated function code:\n")
    print(code)

    # Execute the generated code and call the function
    exec_globals = {}  # Dictionary to hold the execution context
    exec(code, exec_globals)
    print("\nFunction output:")
    exec_globals['hello_name'](name)

if __name__ == "__main__":
    main()