from flask import Flask, render_template, request
import db_functions

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/quiz", methods=['POST'])
def quiz():
    category = request.form["quiz_button"]
    print(category)
    data = list(db_functions.format_questions(db_functions.generate_questions(10, category)))
    if request.method == 'POST':
        return render_template("questions.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
