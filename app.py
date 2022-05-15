from flask import Flask, render_template, request, json
import main

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("test.html")


@app.route("/quiz", methods=['POST'])
def quiz():
    diff = list(main.format_questions(main.generate_questions(10, "different")))
    book = list(main.format_questions(main.generate_questions(10, "books")))
    print(diff)
    print(book)
    if request.method == 'POST':
        return render_template("main.html", data=book)


if __name__ == "__main__":
    app.run(debug=True)
