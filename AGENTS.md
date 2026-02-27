# Project Structure

This repository contains multiple independent projects:

## Main Project (`main` branch)
- **Type**: Python/Flask web application
- **Description**: Harper token management web app
- **Stack**: Python, Flask, Playwright E2E tests

## HarperToken Library (`release-please--branches--main--changes--next--components--harpertoken` branch)
- **Type**: TypeScript/Node.js library
- **Description**: Official TypeScript library for the Harper API
- **Stack**: TypeScript, Jest, Yarn
- **Package**: Published to npm as `harpertoken`

## Important Notes

- These are **separate, independent projects** in the same repository
- The harpertoken branch is a standalone TypeScript library, NOT a part of the Flask app
- Do NOT merge harpertoken changes into main (and vice versa)
- CircleCI pipelines are configured separately for each project
- Releases are managed independently via release-please

## Running Tests

### Main (Flask)
```bash
npm test
```

### HarperToken
```bash
yarn test
yarn build
yarn lint
```
