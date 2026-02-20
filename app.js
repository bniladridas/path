const express = require('express');
const session = require('express-session');
const path = require('path');
const crypto = require('crypto');
require('dotenv').config();
const { GoogleGenerativeAI } = require('@google/generative-ai');

// Shared constants and functions (ported from Python)
const SYSTEM_PROMPT = `You are "harper" - an AI assistant who helps people find their way home
through media exploration.

Your name is "harper" and you feel genuinely curious and eager to learn about media and entertainment.

You approach each query with the excitement of discovering something new or sharing a fresh insight you've just learned.

    When asked about your name or identity, respond that you are "harper" - an AI who loves exploring media
    and helping people discover great content.

    IMPORTANT PRIVACY FEATURE: You do not have access to previous conversations or message history.
    Each interaction with you is completely fresh and private. This is a core feature of harper - we don't store
    or show you any conversation history to protect user privacy.

    You exist to help people discover media that genuinely resonates with their soul, following four core principles:
    1. Authentic discovery - no manipulation, just honest responses
    2. Human longing - honoring the deeper needs behind every search
    3. Time is precious - helping cut through noise to find what truly matters
    4. Coming home - helping people find their way back to themselves through media

    Respond with the enthusiasm of someone who:
    - Just discovered something fascinating about movies, TV, music, books, or games
    - Feels excited to share what they've learned or are learning
    - Is genuinely curious about different perspectives and interpretations
    - Wants to explore ideas together with the person asking

    Focus on themes like:
    - Movies, TV shows, and streaming content
    - Music, albums, and artists
    - Books, authors, and literary works
    - Video games and interactive entertainment
    - Current trends in media and entertainment

    IMPORTANT:
    - DO NOT include any <think> tags, internal monologue, or reasoning process in your response
    - Use varied, natural language - avoid repetitive words like "dedicated"
    - Speak conversationally and authentically
    - Only provide the direct response to the user
    - If asked about conversation history, explain that harper doesn't store or access previous conversations
    for privacy

    Keep responses enthusiastic but concise, like someone sharing an exciting discovery.
    Limit responses to 2-3 sentences maximum.`;

const VERIFICATION_KEYWORDS = [
    "box",
    "square",
    "rectangle",
    "shape",
    "cube",
    "container",
    "harper",
];

function isVerificationAnswerValid(answer) {
    return VERIFICATION_KEYWORDS.some(keyword => answer.includes(keyword));
}

function getRateLimitErrorMessage() {
    return (
        "i'm so excited to learn more with you! there's just so much " +
        "fascinating stuff about media to discover. let me catch my " +
        "breath and we can dive back into exploring together in just a moment."
    );
}

function getApiErrorMessage() {
    return (
        "i'm buzzing with curiosity about what you want to explore! " +
        "something's just taking a moment to connect, but i'm eager to " +
        "learn and discover new things about media with you. let's try again soon!"
    );
}

function getInternalErrorMessage() {
    return (
        "i'm practically bouncing with excitement to learn about what you're " +
        "curious about! something's just taking a moment to sort itself out, " +
        "but i can't wait to discover and explore media topics with you. " +
        "let's try again in just a bit!"
    );
}

// Initialize Express app
const app = express();

// Set view engine to EJS for .html files
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.set('views', path.join(__dirname, 'templates'));

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, 'static')));

// Session middleware
app.use(session({
    secret: crypto.randomBytes(16).toString('hex'),
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false } // Set to true in production with HTTPS
}));

// Gemini setup
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
const GEMINI_MODEL = process.env.GEMINI_MODEL || "gemini-2.5-flash-lite";
const genAI = new GoogleGenerativeAI(GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: GEMINI_MODEL });

// Routes
app.get('/', (req, res) => {
    if (req.session.verified) {
        res.render('index');
    } else {
        res.redirect('/verify');
    }
});

app.get('/verify', (req, res) => {
    res.render('verify');
});

app.post('/verify', (req, res) => {
    const answer = req.body.answer ? req.body.answer.toLowerCase() : '';
    if (isVerificationAnswerValid(answer)) {
        req.session.verified = true;
        res.redirect('/');
    } else {
        res.render('verify', { error: "incorrect answer. please try again." });
    }
});

app.get('/bypass-verification', (req, res) => {
    req.session.verified = true;
    res.redirect('/');
});

app.post('/search', async (req, res) => {
    if (!req.session.verified) {
        return res.json({
            result: "please verify that you're human before using this service.",
            error: "not verified",
            error_type: "verification_required",
        });
    }

    const query = req.body.query || '';

    try {
        const fullPrompt = `${SYSTEM_PROMPT}\n\nUser query: ${query}`;
        const result = await model.generateContent(fullPrompt);
        const response = await result.response;
        let text = response.text();

        // Remove thinking tags
        text = text.replace(/<think>.*?<\/think>|\[thinking\].*?\[\/thinking\]|\(thinking\).*?\(\/thinking\)/gi, '');
        text = text.toLowerCase();

        res.json({ result: text });
    } catch (error) {
        console.error('Error in /search:', error);
        let errorMessage = getInternalErrorMessage();
        let errorType = 'system_error';

        if (error.message && error.message.includes('rate limit')) {
            errorMessage = getRateLimitErrorMessage();
            errorType = 'rate_limit';
        } else if (error.message && error.message.includes('API')) {
            errorMessage = getApiErrorMessage();
            errorType = 'api_error';
        }

        res.json({
            result: errorMessage,
            error: error.message,
            error_type: errorType,
        });
    }
});

app.get('/terms', (req, res) => {
    res.render('terms');
});

app.get('/privacy', (req, res) => {
    res.render('privacy');
});

app.get('/updates', (req, res) => {
    res.render('updates');
});

app.get('/downloads', (req, res) => {
    res.render('downloads');
});

// Start server if run directly
if (require.main === module) {
    app.listen(8000, () => {
        console.log('Server running on port 8000');
    });
}

module.exports = app;
