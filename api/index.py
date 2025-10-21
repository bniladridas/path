from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Vercel! Flask app is working."


@app.route("/test")
def test():
    return "Test route is working."


# This is required for Vercel
if __name__ == "__main__":
    app.run()
