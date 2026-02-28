# Agent Guidelines

## CircleCI Docker Image Pull Failure

The CircleCI pipeline may fail because the Docker image `cimg/node:20-browsers` cannot be pulled from Docker Hub. The daemon returns a "manifest unknown" error.

### Recommended Fix

Use the correct CircleCI Node image tag with a full version number:

```yaml
jobs:
    build:
        docker:
            - image: cimg/node:20.11.0-browsers
```

Or use a base Node image without browsers:

```yaml
jobs:
    build:
        docker:
            - image: cimg/node:20.11.0
```

## Discord Welcome Message

:wave: Hey! Welcome to Harper

Just a heads up - this is a small community for Harper, an AI-powered media exploration app using Google Gemini.

:clipboard: What we have here:

- General chat
- Support (if you get stuck)
- Showcase (share your projects)
- Feedback

:link: Links:

- GitHub: github.com/bniladridas/path

No pressure to introduce yourself - just hang out and chat!
