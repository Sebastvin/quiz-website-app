# Web application, multiple choice quiz
The web application was written in python with using nosql mongodb database, html and js.


[<img align="left" alt="p1" width="26px" style="margin-left:.6em" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/flask.svg"/>][flask]
[<img align="left" alt="p2" width="26px" style="margin-left:.6em" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/python.svg"/>][python]
[<img align="left" alt="p3" width="26px" style="margin-left:.6em" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/mongodb.svg"/>][mongodb]
[<img align="left" alt="p4" width="26px" style="margin-left:.6em" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/heroku.svg"/>][heroku]


## Note
The site is hosted on herokuapp platform, if no one has visited the site for a long time it goes into a "sleep state" and may take longer to load.
<br />
Link to website: https://quizzzing.herokuapp.com

## How it works?

Python connects to the server before generating the page, calls a function that retrieves 10 random questions from the databases in the selected category (they cannot be repeated). Then the page is rendered with the data already loaded, which is later converted to a JSON list in JS code.

### Sources: 

The quiz questions are from here:
- ✅ https://opentdb.com/api_config.php
- ✅ https://pastebin.com/QRGzxxEy


[python]: https://www.python.org/downloads/
[heroku]: https://www.heroku.com/
[mongodb]: https://www.mongodb.com/
[flask]: https://flask.palletsprojects.com/en/2.0.x/

Screen from web-app:

<img src="https://raw.githubusercontent.com/Sebastvin/quiz-website-app/static/main.png" alt="quiz game"/>