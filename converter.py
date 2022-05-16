import json
import random


def load_json(filename):
    f = open(filename)
    return json.load(f)


def randomize_questions_and_answers(questions, right_answer):
    choose = []
    prepared_data = []
    values = ["A", "B", "C", "D"]
    random_index = random.randint(0, 3)

    for _ in questions:

        while random_index in choose:
            random_index = random.randint(0, 3)

        choose.append(random_index)
        prepared_data.append(questions[random_index])

    return prepared_data, values[prepared_data.index(right_answer)]


def clean_data_json(data):
    for value in data:
        value['question'] = value['question'].replace("&quot;", "").replace("&#039;", "").replace("&eacute;", "")
        value['correct_answer'] = value['correct_answer'].replace("&quot;", "").replace("&#039;", "").replace("&eacute;", "")
        value['incorrect_answers'] = [x.replace("&quot;", "").replace("&#039;", "").replace("&eacute;", "") for x in
                                      value['incorrect_answers']]
        value['incorrect_answers'].append(value['correct_answer'])

    return data


def convert_json_data(filename):
    full_data = []
    file = load_json(filename)
    file = clean_data_json(file)

    for x in file:
        final_data, answer = randomize_questions_and_answers(x['incorrect_answers'], x['correct_answer'])

        tmp = {
            "question": x['question'],
            "A": final_data[0],
            "B": final_data[1],
            "C": final_data[2],
            "D": final_data[3],
            "answer": answer
        }
        full_data.append(tmp)

    return full_data
