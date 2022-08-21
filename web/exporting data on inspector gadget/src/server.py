import os
from flask import Flask, request, send_file, render_template, flash
from constants import ROOT
from urllib.parse import unquote


app = Flask(__name__)
app.secret_key = os.urandom(38).hex()
allowed_paths = ["guide.html", "secrets.html", "about.html"]

def sanitize(path):
    """Filtering for the data"""
    if path in allowed_paths:
        return path
    return path.replace("/", "").replace(".html", "")


@app.route("/", methods=["GET"])
def index():
    location = request.query_string.decode()
    if not len(location):
        return render_template("index.html")
    location = sanitize(location.split("=")[1])
    path = unquote(os.path.normpath(os.path.join(ROOT, location)))
    
    try:
        return send_file(path)
    except (FileNotFoundError, IsADirectoryError):
        flash(f"File not found: {location}")
        return render_template("index.html")
