from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
import json
from pprint import PrettyPrinter
from pymongo import MongoClient

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://x_cherry:{password}@disk0.t55my.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(connection_string)

jeoprady_db = client.jeoprady_db
question = jeoprady_db.question

printer = PrettyPrinter()


def fuzzy_matching():
    result = question.aggregate([
        {
            "$search":
                {
                    "index": "language_search",
                    "text": {
                        "query": "computer",
                        "path": "category",
                        "synonyms": "mapping"
                    }
                }
        }
    ])
    printer.pprint(list(result))


def autocomplete():
    result = question.aggregate([
        {
            "$search": {
                "index": "language_search",
                "autocomplete":
                    {
                        "query": "computer programmer",
                        "path": "question",
                        "tokenOrder": "sequential",
                        "fuzzy": {}
                    }
            }
        },
        {
            "$project":
                {
                    "_id": 0,
                    "question": 1
                }
        }
    ])

    printer.pprint(list(result))


autocomplete()
