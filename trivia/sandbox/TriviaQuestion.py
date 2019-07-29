class TriviaQuestion:
    def __init__(self, category, question_type, difficulty, question, correct_answer, incorrect_answers):
        self.category = category
        self.question_type = question_type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

    def __repr__(self):
        return f'TriviaQuestion({self.category}, ' \
            f'{self.question_type}, ' \
            f'{self.difficulty}, ' \
            f'{self.question}, ' \
            f'{self.correct_answer}, ' \
            f'{self.incorrect_answers})'

    @property
    def choices(self):
        choices = [x for x in self.incorrect_answers]
        # choices.append(self.incorrect_answers)
        choices.append(self.correct_answer)
        return sorted(choices)