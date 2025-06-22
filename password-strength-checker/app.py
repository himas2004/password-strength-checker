from flask import Flask, request, render_template
import re

app = Flask(__name__)

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search("[a-z]", password): score += 1
    if re.search("[A-Z]", password): score += 1
    if re.search("[0-9]", password): score += 1
    if re.search("[!@#$%^&*()_+]", password): score += 1
    return ["Very Weak", "Weak", "Medium", "Strong", "Very Strong", "Excellent"][score]

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        pwd = request.form["password"]
        result = check_strength(pwd)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)