import pytest
from unittest.mock import patch
import unittest.mock as mock
import random

from trivia.sandbox.TriviaQuestion import TriviaQuestion
@mock.patch('trivia.sandbox.TriviaQuestion.TriviaQuestion.randomize_choices', side_effect=lambda x: x)
@pytest.mark.parametrize("test_input, expected", [
                        (TriviaQuestion('','','','','True',['False']), ['True', 'False']),
                        (TriviaQuestion('','','','','True',['F&amp;alse']), ['True', 'F&alse']),
                        (TriviaQuestion('','','','','True',['F&amp;alse', '1']), ['True', 'F&alse', '1']),

                        ]
                         )
def test_choices_amp_replace(mock_shuffle, test_input, expected):
    assert mock_shuffle.called
    # print(test_input.choices)
    assert test_input.choices == expected


