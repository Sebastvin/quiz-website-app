import json

f = open('data.json')

data = json.load(f)

# for x in data:
#     print(x['question'].replace("&quot;", "\"").replace("&#039;", "`"))
#     print(x['correct_answer'].replace("&quot;", "\"").replace("&#039;", "`"))
#     x['incorrect_answers'] = [x.replace("&quot;", "\"").replace("&#039;", "`") for x in x['incorrect_answers']]
#     print(x['incorrect_answers'])

# print(data)

def randomize_questions_and_answers(questions, answer):


for x in data[:1]:
    x['incorrect_answers'].append(x['correct_answer'])

    print(x['incorrect_answers'])
    print(x['correct_answer'])
    picks = x['incorrect_answers']

    tmp = {
        "question": x['question'],
        "A": picks[0],
        "B": picks[1],
        "C": picks[2],
        "D": picks[3],
        "answer": x['correct_answer']
    }



print(tmp)
