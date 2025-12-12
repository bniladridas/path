# API Key Test

To verify your Gemini API key is valid:

```bash
source .env && curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY" | head -20
```

A successful response returns a JSON list of available models.
