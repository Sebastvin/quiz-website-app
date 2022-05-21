from converter_to_json import convert_json_data, clean_data_json


def get_category(category, db):
    """Returns a database of questions from the selected category"""
    if "different" == category:
        return db.questions

    if "video_games" == category:
        return db.video_games

    if "books" == category:
        return db.books

    if "sports" == category:
        return db.sports

    if "music" == category:
        return db.music

    if "math" == category:
        return db.math

    if "geography" == category:
        return db.geography

    if "computer_science" == category:
        return db.computer_science


def count_elements(db, category):
    """Count all records from specific category"""
    data = get_category(category, db)
    return data.count_documents(filter={})


def project_columns(db):
    """Shows all specific data from category in console"""
    data = get_category(category, db)
    columns = {"_id": 0, "question": 1, "A": 2, "B": 3, "C": 4, "D": 5, "answer": 6}
    people = data.find({}, columns)
    for person in people:
        print(list(person.values()))


def generate_questions(number_questions, category, db):
    """Randomly draws a given number (number_questions) of questions from the indicated category from database"""
    data = get_category(category, db)
    return list(data.aggregate([{"$sample": {"size": number_questions}}]))


def format_questions(data):
    """Format json data to the required format"""
    """Data are downloaded from https://opentdb.com/api_config.php"""

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


def create_documents(docs, category, db):
    """Add to specific database news records"""
    tmp = get_category(category, db)
    tmp.insert_many(docs)


def delete_duplicates(category, db):
    """Delete duplicates by question in specific category"""
    coll = get_category(category, db)
    cursor = coll.aggregate(
        [
            {"$group":
                {
                    "_id": "$question",
                    "unique_ids": {"$addToSet": "$_id"},
                    "count": {"$sum": 1}
                }
            },
            {"$match":
                 {"count": {"$gte": 2}}
             }
        ]
    )

    response = []
    for doc in cursor:
        response.append(doc["unique_ids"][0])

    coll.delete_many({"_id": {"$in": response}})


def delete_all(category, db):
    """--------------WARNING----------------"""
    """Delete all database specific category"""

    data = get_category(category, db)
    data.delete_many({})

    """Delete one element by specific key, argument"""
    # person_collection.delete_one({"_id": _id})

