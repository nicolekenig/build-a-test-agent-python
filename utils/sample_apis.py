"""Sample API endpoints for workshop exercises"""

SAMPLE_ENDPOINTS = [
    {
        "name": "JSONPlaceholder Posts",
        "base_url": "https://jsonplaceholder.typicode.com",
        "endpoints": [
            {"method": "GET", "path": "/posts", "description": "Get all posts"},
            {"method": "GET", "path": "/posts/1", "description": "Get specific post"},
            {"method": "POST", "path": "/posts", "description": "Create new post"},
            {"method": "PUT", "path": "/posts/1", "description": "Update post"},
            {"method": "DELETE", "path": "/posts/1", "description": "Delete post"}
        ]
    },
    {
        "name": "HTTPBin Testing",
        "base_url": "https://httpbin.org",
        "endpoints": [
            {"method": "GET", "path": "/get", "description": "Test GET request"},
            {"method": "POST", "path": "/post", "description": "Test POST request"},
            {"method": "GET", "path": "/status/200", "description": "Return status 200"},
            {"method": "GET", "path": "/status/404", "description": "Return status 404"},
            {"method": "GET", "path": "/delay/2", "description": "Delayed response"}
        ]
    }
]


def get_sample_api():
    """Return a simple API for quick testing"""
    return {
        "name": "Simple Test API",
        "base_url": "https://httpbin.org",
        "endpoints": [
            {"method": "GET", "path": "/get", "description": "Simple GET request test"}
        ]
    }
