from flask import Flask, render_template, request
import os
import db_functions
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

password = os.environ.get("MONGODB_PWD", "")


connection_string = f"mongodb+srv://x_cherry:{password}@disk0.t55my.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&authSource=admin"
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
    if request.method == 'POST':
        return render_template("questions.html", data=data)


if __name__ == "__main__":
    app.run()
