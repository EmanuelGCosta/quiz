from requests import *

questions = get("https://opentdb.com/api.php?amount=10&type=boolean")
questions.raise_for_status()
question_data = questions.json()["results"]
