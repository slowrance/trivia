import random
from itertools import chain
from typing import List

class TriviaQuestion:
    def __init__(self, category, question_type, difficulty, question, correct_answer, incorrect_answers):
        self.category = category
        self.question_type = question_type
        self.difficulty = difficulty
        self.question = question
        self._correct_answer = correct_answer
        self._incorrect_answers = incorrect_answers
        self.correct_index = None
        self._choices = self.randomize_choices(list(chain(self._incorrect_answers, [self._correct_answer])))

    def randomize_choices(self, choices) -> List:
        random.shuffle(choices)
        self.correct_index = next((i for i, c in enumerate(choices) if c == self._correct_answer))
        # shuffle
        # find correct answer
        return choices

    def __repr__(self):
        return f'TriviaQuestion({self.category}, ' \
               f'{self.question_type}, ' \
               f'{self.difficulty}, ' \
               f'{self.question}, ' \
               f'{self._correct_answer}, ' \
               f'{self._incorrect_answers})'

    @property
    def choices(self):
        return [x.replace('&amp;', '&') for x in self._choices]
    #
    # @property
    # def correct_answers(self):
    #     return self._correct_answer.replace('&amp;', '&')
    #
    # @property
    # def incorrect_answers(self):
    #     return [x.replace('&amp;', '&') for x in self._incorrect_answers]
