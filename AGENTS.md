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

## Merge Conflict Resolution Strategy

When merging main into harpertoken branch (or vice versa):

1. **For harpertoken branch**: Keep our versions of package.json, README.md, CHANGELOG.md, CircleCI config
2. **Delete main's files**: Remove Python/Flask files (path/app.py, requirements*.txt, templates/*.html, static/*)
3. **Commands**:
   ```bash
   git merge origin/main --no-commit --no-ff
   git checkout --ours .circleci/config.yml CHANGELOG.md README.md package.json
   rm -f .github/workflows/auto-release.yml path/app.py requirements*.txt static/css/style.css templates/privacy.html templates/terms.html templates/updates.html
   git add -A && git commit -m "chore: merge main with conflicts resolved"
   ```

4. **Important**: These are separate projects - prefer keeping them separate rather than forcing merges
