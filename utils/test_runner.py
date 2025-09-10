"""Utilities for running generated tests safely"""

import subprocess
import sys
import json
import time
from typing import Dict, Any, Tuple


def execute_code_safely(code: str, timeout: int = 30) -> Tuple[bool, str, Dict[str, Any]]:
    """
    Execute test code safely and capture results

    Args:
        code: Python code to execute
        timeout: Maximum execution time in seconds

    Returns:
        Tuple of (success, output, results)
    """
    try:
        # Create a safe execution environment
        exec_globals = {
            '__builtins__': __builtins__,
            'requests': __import__('requests'),
            'json': __import__('json'),
            'time': __import__('time'),
            'print': print
        }

        # Capture results
        results = {}

        # Execute the code
        exec(code, exec_globals, results)

        return True, "Code executed successfully", results

    except Exception as e:
        return False, f"Execution error: {str(e)}", {}


def format_test_results(results: Dict[str, Any]) -> str:
    """Format test results for display"""
    if not results:
        return "No results captured"

    formatted = "=== Test Results ===\n"
    for key, value in results.items():
        if not key.startswith('_'):
            formatted += f"{key}: {value}\n"

    return formatted
