# # from dotenv import load_dotenv, find_dotenv
# # import os
# # import pprint
# from pymongo import MongoClient
# from converter import convert_json_data, clean_data_json
#
# # load_dotenv(find_dotenv())
# #
# # password = os.environ.get("MONGODB_PWD")
#
# connection_string = "mongodb+srv://x_cherry:GCQ8MPFozVMML8XO@disk0.t55my.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&authSource=admin"
#
# client = MongoClient(connection_string)
#
# printer = pprint.PrettyPrinter()
#
# quiz_db = client.quiz
# collections = quiz_db.list_collection_names()
#
#
# def get_category(category):
#     if "different" == category:
#         return quiz_db.questions
#
#     if "video_games" == category:
#         return quiz_db.video_games
#
#     if "books" == category:
#         return quiz_db.books
#
#     if "sports" == category:
#         return quiz_db.sports
#
#     if "music" == category:
#         return quiz_db.music
#
#     if "math" == category:
#         return quiz_db.math
#
#     if "geography" == category:
#         return quiz_db.geography
#
#     if "computer_science" == category:
#         return quiz_db.computer_science
#
#
# def count_elements():
#     return quiz_different.count_documents(filter={})
#
#
# def project_columns():
#     columns = {"_id": 0, "question": 1, "A": 2, "B": 3, "C": 4, "D": 5, "answer": 6}
#     people = quiz_different.find({}, columns)
#     for person in people:
#         print(list(person.values()))
#
#
# def generate_questions(number_questions, category):
#     data = get_category(category)
#     return list(data.aggregate([{"$sample": {"size": number_questions}}]))
#
#
# def format_questions(data):
#     question, type_a = [], []
#     type_b, type_c = [], []
#     type_d, answer = [], []
#
#     for idx, _ in enumerate(data):
#         question.append(list(data[idx].values())[1])
#         type_a.append(list(data[idx].values())[2])
#         type_b.append(list(data[idx].values())[3])
#         type_c.append(list(data[idx].values())[4])
#         type_d.append(list(data[idx].values())[5])
#         answer.append(list(data[idx].values())[6])
#
#     return zip(question, type_a, type_b, type_c, type_d, answer)
#
#
# def create_documents(docs, category):
#     tmp = get_category(category)
#     tmp.insert_many(docs)
#
#
# def delete_duplicates(category):
#     coll = get_category(category)
#     cursor = coll.aggregate(
#         [
#             {"$group":
#                 {
#                     "_id": "$question",
#                     "unique_ids": {"$addToSet": "$_id"},
#                     "count": {"$sum": 1}
#                 }
#             },
#             {"$match":
#                  {"count": {"$gte": 2}}
#              }
#         ]
#     )
#
#     response = []
#     for doc in cursor:
#         response.append(doc["unique_ids"][0])
#
#     coll.delete_many({"_id": {"$in": response}})
#
#
# def delete_all(category):
#     data = get_category(category)
#
#     # person_collection.delete_one({"_id": _id})
#     data.delete_many({})
#
#
# if __name__ == "__main__":
#     pass
#     # x = generate_questions(2)
#     # printer.pprint(x)
#     # print(list(format_questions(x)))
#
#     # docs = convert_json_data("data.json")
#     # create_documents(docs, "books")
#     # delete_duplicates("books")
#
#     # delete_all("video_games")
