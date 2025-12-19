from flask import Flask, render_template, request
from resume_parser import extract_text
from similarity import calculate_match

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files["resume"]
    job_desc = request.form["job_description"]

    resume_text = extract_text(resume)
    score = calculate_match(resume_text, job_desc)

    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)
