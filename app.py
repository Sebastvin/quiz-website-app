from flask import Flask, render_template, request
import db_functions
from pymongo import MongoClient

app = Flask(__name__)

connection_string = "mongodb+srv://x_cherry:GCQ8MPFozVMML8XO@disk0.t55my.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(connection_string)
db = client.quiz


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/quiz", methods=['POST'])
def quiz():
    category = request.form["quiz_button"]
    # print(category)
    data = list(db_functions.format_questions(db_functions.generate_questions(10, category, db)))
    print(data)
    if request.method == 'POST':
        return render_template("questions.html", data=data)


if __name__ == "__main__":
    app.run()
