from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://x_cherry:{password}@disk0.t55my.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&authSource=admin"

client = MongoClient(connection_string)

printer = pprint.PrettyPrinter()

quiz_db = client.quiz
quiz_collections = quiz_db.questions
collections = quiz_db.list_collection_names()


def count_elements():
    return quiz_collections.count_documents(filter={})


def project_columns():
    columns = {"_id": 0, "question": 1, "A": 2, "B": 3, "C": 4, "D": 5, "answer": 6}
    people = quiz_collections.find({}, columns)
    for person in people:
        print(list(person.values()))


def generate_questions(number_questions):
    return list(quiz_collections.aggregate([{"$sample": {"size": number_questions}}]))


def format_questions(data):
    question, type_a = [], []
    type_b, type_c = [], []
    type_d, answer = [], []

    for idx, _ in enumerate(data):
        question.append(list(data[idx].values())[1])
        type_a.append(list(data[idx].values())[2])
        type_b.append(list(data[idx].values())[3])
        type_c.append(list(data[idx].values())[4])
        type_d.append(list(data[idx].values())[5])
        answer.append(list(data[idx].values())[6])

    return zip(question, type_a, type_b, type_c, type_d, answer)


if __name__ == "__main__":
    x = generate_questions(2)

    printer.pprint(x)

    print(list(format_questions(x)))
