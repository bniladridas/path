
---

<div align="center">
  <img src="static/images/logo.svg" alt="path Logo" width="120" height="120">
  <h1>path</h1>
  <p>come home before it's too late</p>
  <p>helping people find their way home through media exploration</p>
  <p>
    <a href="https://github.com/bniladridas/path/stargazers"><img src="https://img.shields.io/github/stars/bniladridas/path" alt="Stars Badge"/></a>
    <a href="https://github.com/bniladridas/path/network/members"><img src="https://img.shields.io/github/forks/bniladridas/path" alt="Forks Badge"/></a>
    <a href="https://github.com/bniladridas/path/issues"><img src="https://img.shields.io/github/issues/bniladridas/path" alt="Issues Badge"/></a>
    <a href="https://github.com/bniladridas/path/blob/main/LICENSE"><img src="https://img.shields.io/github/license/bniladridas/path" alt="License Badge"/></a>
  </p>
</div>

## a different kind of ai

path is an ai-powered media exploration interface that helps you discover movies, music, books, and games with radical transparency and human dignity. powered by google's gemini 1.5 flash, path exists to help people find their way back to themselves through authentic media discovery.

## four pillars of authentic discovery

- **authentic discovery**: no manipulation, just honest responses that honor your curiosity
- **human longing**: recognizing the deeper needs behind every search for meaning
- **time is precious**: cutting through noise to help you find what truly matters
- **coming home**: helping you find your way back to yourself through media

## features that serve human flourishing

- **radical transparency**: complete visibility into ai costs, data usage, and system operations
- **privacy by design**: no conversation history stored, fresh interactions every time
- **theme customization**: 5 beautiful color themes that adapt the entire interface
- **keyboard shortcuts**: efficient navigation with single-key access to all tools
- **comprehensive tools**: about, product, token pricing, protocol details, gmail integration, neural networks explanation, blog, and developer resources
- **human verification**: thoughtful protection against automated access
- **legal transparency**: complete terms of use, privacy policy, and updates tracking
- **responsive design**: beautiful on desktop and mobile devices

## getting started

### what you need
- python 3.8 or later
- a [google gemini api](https://ai.google.dev/) key

### local development
1. clone the repository:
   ```bash
   git clone https://github.com/bniladridas/path.git
   cd path
   ```
2. install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. add your api key to a `.env` file:
   ```
   GEMINI_API_KEY=your-gemini-api-key
   ```
4. launch the app:
   ```bash
   python app.py
   ```
5. visit `http://127.0.0.1:8000` in your browser

## deployment

### vercel deployment (recommended)
1. install vercel cli:
   ```bash
   npm install -g vercel
   ```
2. log in to vercel:
   ```bash
   vercel login
   ```
3. deploy to preview:
   ```bash
   vercel
   ```
4. set your environment variable:
   ```bash
   vercel env add GEMINI_API_KEY
   ```
5. deploy to production:
   ```bash
   vercel --prod
   ```

path is optimized for vercel's serverless platform with automatic scaling and global edge deployment.

## how path works

### user experience
- first-time visitors complete human verification (or use gmail for automatic bypass)
- enter media queries and press enter (or press `/` to focus search)
- google gemini 1.5 flash processes requests with path's specialized prompt
- responses appear below the search bar in a clean, readable format
- access tools via three-dot menu or keyboard shortcuts (a, r, h, p, t, o, g, n, b, c)
- switch themes instantly with number keys (1-5) or via menu
- all interactions are private - no conversation history stored

### keyboard shortcuts
- **/** - focus search input
- **escape** - close modals and return to home
- **a** - about path
- **r** - reset interface
- **h** - help and usage guide
- **p** - product philosophy (four pillars)
- **t** - token pricing transparency
- **o** - protocol and connection details
- **g** - gmail integration benefits
- **n** - neural networks explanation
- **b** - blog (why path exists)
- **c** - coders (developer inspection guide)
- **1-5** - theme selection (908b70, 4e4c40, a9844f, d5c9bc, 141614)

### human verification
the verification system shows an image requiring description. for development, use `/bypass-verification` to skip this step. gmail users receive automatic verification bypass for streamlined access.

## project structure

```
path/
├── app.py                 # flask application with all routes
├── templates/
│   ├── index.html         # main interface with tools and themes
│   ├── terms.html         # comprehensive terms of use
│   ├── privacy.html       # privacy policy with tables
│   ├── updates.html       # changelog and version history
│   └── verify.html        # human verification page
├── static/
│   ├── css/
│   │   └── style.css      # complete styling with theme system
│   └── images/
│       ├── favicon.svg    # path logo favicon
│       ├── logo.svg       # main logo
│       └── verification.jpg # human verification image
├── vercel.json            # vercel deployment configuration
├── requirements.txt       # python dependencies (flask, requests, python-dotenv)
├── .env.example           # environment variable template
├── LICENSE                # mit license
└── README.md              # this documentation
```

## ux philosophy & prompt methodology

### interface design principles

#### minimalist interaction
- **single search input**: one text field, infinite possibilities
- **progressive disclosure**: tools appear when needed, hidden when not
- **keyboard-first**: every action accessible via shortcuts
- **visual hierarchy**: content first, chrome second

#### emotional design
- **curiosity-driven**: interface encourages exploration
- **learning-oriented**: errors become opportunities to discover
- **human warmth**: technology that feels approachable, not intimidating
- **coming home**: familiar patterns that feel safe and welcoming

### prompt engineering methodology

#### ai personality design
```
"path" - an AI assistant who helps people find their way home through media exploration
```

#### core prompt architecture
- **identity establishment**: clear name and purpose ("path")
- **privacy transparency**: explicit mention of no conversation history
- **enthusiasm modeling**: genuine curiosity and excitement about discovery
- **boundary setting**: media-focused scope with gentle redirects
- **response constraints**: 2-3 sentences maximum for focused interactions

#### conversation flow design
- **fresh context**: each interaction starts completely clean
- **no memory burden**: users don't need to repeat context
- **immediate value**: every response provides actionable insights
- **natural language**: conversational tone, not robotic responses

#### error handling philosophy
- **maintain curiosity**: errors don't break the learning mindset
- **honest communication**: transparent about what went wrong
- **encouraging tone**: setbacks become part of the exploration journey
- **system resilience**: graceful degradation maintains user confidence

### user experience patterns

#### discovery workflow
1. **arrival**: clean interface invites exploration
2. **verification**: human-friendly process with gmail bypass
3. **exploration**: search reveals path's personality and capabilities
4. **tool discovery**: three-dot menu reveals deeper functionality
5. **customization**: themes allow personal expression
6. **mastery**: keyboard shortcuts enable power user efficiency

#### information architecture
- **search-centric**: primary interaction model
- **tool constellation**: related functions grouped logically
- **theme system**: visual customization without complexity
- **transparency layers**: increasing detail available on demand

## technical philosophy

### privacy by design
- no conversation history stored or accessed
- fresh ai interactions every time
- minimal data collection with transparent policies
- gmail domain verification only (no email storage)

### radical transparency
- complete token pricing visibility
- open source codebase for inspection
- detailed protocol and connection information
- honest error handling with learning-oriented messages

### human-centered technology
- keyboard shortcuts for efficiency
- responsive design for all devices
- thoughtful error messages that maintain curiosity
- clean interface that puts content first

## license

open and free under the [mit license](LICENSE).

## connect

- **author**: niladri das (@bniladridas)
- **github**: [github.com/bniladridas](https://github.com/bniladridas)
- **linkedin**: [linkedin.com/in/bniladridas](https://www.linkedin.com/in/bniladridas)

## built with love and

- [google gemini 1.5 flash](https://ai.google.dev/) - ai processing
- [flask](https://flask.palletsprojects.com/) - web framework
- [vercel](https://vercel.com/) - deployment platform
- vanilla javascript - no frameworks, just honest code
- css custom properties - theme system
- human curiosity and the desire to come home

---

*path exists to help people find their way home through media exploration. every line of code reflects our commitment to honest technology that serves human flourishing rather than corporate metrics.*
