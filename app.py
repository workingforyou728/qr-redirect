from flask import Flask, redirect

app = Flask(__name__)

# Set your redirect link here
REDIRECT_URL = "https://inspireoneeducationalservices.com/index.html"   # <-- change after 3 days

@app.route("/")
def home():
    return redirect(REDIRECT_URL)
