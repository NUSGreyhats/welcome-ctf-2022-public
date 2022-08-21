import sqlite3
import logging
from uuid import uuid4
from flask import Flask, render_template, request, abort, redirect
from flask.globals import g
from admin import visit
from urllib.parse import urlparse
from constants import BANNED, WEB_LOCATION

app = Flask(__name__)   


logging.basicConfig(filename="log.txt", level=logging.INFO)

@app.before_first_request
def setup_db():
    db = sqlite3.connect("reports.db")
    db.cursor().execute(
        "CREATE TABLE IF NOT EXISTS reports (report_id UNSIGNED BIG INT PRIMARY KEY, report TEXT)"
    )
    db.close()


@app.before_request
def make_cursor():
    g.db = sqlite3.connect("reports.db")


@app.after_request
def close_db(response):
    g.db.close()
    return response


def generate_random_id() -> int:
    """Generate a random id"""
    return uuid4().int & (1 << 32) - 1


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    if request.method == "GET":
        return render_template("index.html")

    # Get the Report arguments
    report: str = request.form.get("report", None)

    if report is None:
        return abort(400, "Field cannot be empty")

    report_id = generate_random_id()
    db = g.db
    cursor = db.cursor()

    cursor.execute("INSERT INTO reports VALUES (?, ?)", (report_id, sanitize(report)))
    db.commit()

    return_msg = visit(f"{WEB_LOCATION}/report/{report_id}")

    logging.info(f"Visit message: {return_msg}")
    return redirect(f"/report/{report_id}")


def sanitize(report: str) -> str:
    """Sanitize the report"""
    for tag in BANNED:
        report = report.replace(f"<{tag}>", "").replace(f"</{tag}>", "")
    return report


@app.route("/report/<int:report_id>")
def view_report(report_id: int) -> str:
    try:
        report = (
            g.db.cursor()
            .execute("SELECT report FROM reports WHERE report_id = ?", (report_id,))
            .fetchone()[0]
        )
    except:
        return abort(404, "Report not found")
    return render_template("report.html", report_id=report_id, report=report)
