# PATH API Documentation

This document provides detailed information about the PATH API endpoints, request/response formats, and usage examples.

## Base URL
All API endpoints are relative to the base URL of your deployment (e.g., `https://your-vercel-app.vercel.app`).

## Authentication
Most endpoints require human verification. The verification is handled via session cookies after completing the verification challenge.

## Endpoints

### 1. Home Page
- **URL**: `/`
- **Method**: `GET`
- **Description**: Main application interface
- **Response**: HTML page with the PATH application interface
- **Redirects**:
  - If not verified: Redirects to `/verify`
  - If verified: Serves the main application interface

### 2. Human Verification

#### Display Verification Challenge
- **URL**: `/verify`
- **Method**: `GET`
- **Description**: Shows the human verification challenge
- **Response**: HTML page with verification challenge

#### Process Verification
- **URL**: `/verify`
- **Method**: `POST`
- **Description**: Processes the verification response
- **Form Data**:
  - `answer`: (string) User's response to the verification challenge
- **Responses**:
  - Success: Redirects to home page with verification cookie set
  - Failure: Returns to verification page with error message

### 3. Search Endpoint
- **URL**: `/search`
- **Method**: `POST`
- **Description**: Processes search queries using Google's Gemini 2.0 Flash model
- **Headers**:
  - `Content-Type: application/x-www-form-urlencoded`
- **Form Data**:
  - `query`: (string) The search query or question
- **Responses**:
  - Success (200):
    ```json
    {
      "response": "ai-generated response text"
    }
    ```
  - Error (400/401/500):
    ```json
    {
      "error": "Error message describing the issue"
    }
    ```

### 4. Information Pages

#### Terms of Use
- **URL**: `/terms`
- **Method**: `GET`
- **Description**: Displays the Terms of Use
- **Response**: HTML page with terms of service

#### Privacy Policy
- **URL**: `/privacy`
- **Method**: `GET`
- **Description**: Displays the Privacy Policy
- **Response**: HTML page with privacy policy

#### Updates
- **URL**: `/updates`
- **Method**: `GET`
- **Description**: Displays application updates and changelog
- **Response**: HTML page with updates information

## Example Usage

### JavaScript (Browser)

```javascript
// Perform a search query
async function searchPath(query) {
  const formData = new FormData();
  formData.append('query', query);

  try {
    const response = await fetch('/search', {
      method: 'POST',
      body: new URLSearchParams(formData)
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Search failed');
    }

    const data = await response.json();
    return data.response;
  } catch (error) {
    console.error('Search error:', error);
    throw error;
  }
}

// Example usage
searchPath('What are some thought-provoking science fiction books?')
  .then(response => console.log(response))
  .catch(error => console.error(error));
```

### Python (Requests)

```python
import requests

def search_path(query, base_url='https://your-vercel-app.vercel.app'):
    """
    Perform a search query against the PATH API

    Args:
        query (str): The search query or question
        base_url (str): Base URL of the PATH API

    Returns:
        str: The AI-generated response
    """
    try:
        response = requests.post(
            f"{base_url}/search",
            data={"query": query},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        print(f"Error performing search: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        result = search_path("Recommend some mind-expanding documentaries")
        print(result)
    except Exception as e:
        print(f"Failed to get response: {e}")
```

## Rate Limiting
To ensure fair usage and maintain service quality, the API implements rate limiting. If you exceed the allowed number of requests, you may receive a `429 Too Many Requests` response.

## Error Handling
All error responses follow a consistent format:

```json
{
  "error": "Human-readable error message",
  "code": "optional_error_code"
}
```

## Support
For support or to report issues, please open an issue in the [GitHub repository](https://github.com/bniladridas/path).
