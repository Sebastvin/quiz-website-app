from dotenv import load_dotenv, find_dotenv
import os
import pprint
from datetime import datetime as dt
from pymongo import MongoClient

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://x_cherry:{password}@disk0.t55my.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(connection_string)

dbs = client.list_database_names()
production = client.production


def create_validator():
    book_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "year"],
            "properties": {
                "name": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "objectId",
                        "description": "must be a string and is required"
                    }
                },
                "year": {
                    "bsonType": "int",
                    "minimum": 2017,
                    "maximum": 3017,
                    "description": "must be an integer in [ 2017, 3017 ] and is required"
                }
            }
        }
    }

    try:
        production.create_collection("book")
    except Exception as e:
        print(e)

    production.command("collMod", "book", validator=book_validator)


# create_validator()

def create_author_collection():
    author_collection = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                }
            }
        }
    }

    try:
        production.create_collection("author")
    except Exception as e:
        print(e)

    production.command("collMod", "author", validator=author_collection)


# create_author_collection()

def create_data():
    authors = [
        {
            "name": "Jonny"
        },
        {
            "name": "Wozniak"
        },
        {
            "name": "Lenny"
        },
    ]

    author_collection = production.author

    authors = author_collection.insert_many(authors).inserted_ids

    books = [
        {
            "name": [authors[0]],
            "year": 2019,
        },
        {
            "name": [authors[0]],
            "year": 2020,
        },
        {
            "name": [authors[1]],
            "year": 2049,
        }
    ]

    book_collection = production.book
    book_collection.insert_many(books)


# books_containing_year = production.book.find({"year": {"$gt": 2030}})
#
print = pprint.PrettyPrinter()
#
# print.pprint(list(books_containing_year))


authors_and_books = production.author.aggregate([{
    "$lookup": {
        "from": "book",
        "localField": "_id",
        "foreignField": "name",
        "as": "books"
    }
}])

# print.pprint(list(authors_and_books))

# import pyarrow
# from pymongoarrow.api import Schema
# from pymongoarrow.monkey import patch_all
# import pymongoarrow as pma
# from bson import ObjectId
#
# patch_all()
#
# author = Schema({"_id": ObjectId, "first_name": pyarrow.string(), "last_name": pyarrow.string()})
#
# df = production.author.find_pandas_all({}, schema=author)
# arrow_table = production.author.find_arrow_all({}, schema=author)
# ndarrays = production.author.find_numpy_all({}, schema=author)
# print(df)
