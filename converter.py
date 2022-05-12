import json

f = open('data.json')

data = json.load(f)

for x in data:
    print(x['question'].replace("&quot;", "\"").replace("&#039;", "`"))
    print(x['correct_answer'])
    print(x['incorrect_answers'])