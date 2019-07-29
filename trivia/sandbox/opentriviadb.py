import requests
import json
import html
from trivia.sandbox.TriviaQuestion import TriviaQuestion


def get_questions():
    url = 'https://opentdb.com/api.php?amount=10'
    r = requests.get(url)
    raw_json = json.loads(r.text)
    questions = []
    for result in raw_json['results']:
        tq = TriviaQuestion(result.get('category'),
                            result.get('type'),
                            result.get('difficulty'),
                            html.unescape(result.get('question')),
                            html.unescape(result.get('correct_answer')),
                            html.unescape(result.get('incorrect_answers')),
                            )
        questions.append(tq)

    return questions

if __name__ == '__main__':
    pass
