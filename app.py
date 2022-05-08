from flask import Flask, render_template, request, json
import main

app = Flask(__name__)

data = list(main.format_questions(main.generate_questions(10)))



@app.route("/")
def main_page():
    return render_template("test.html")


@app.route("/quiz", methods=['POST'])
def some():
    if request.method == 'POST':
        return render_template("main.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)


