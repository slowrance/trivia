from pyramid.view import view_config
from trivia.sandbox.opentriviadb import get_questions


@view_config(route_name='home', renderer="templates/trivia_home.pt")
def my_view(request):
    questions = get_questions()
    return {'project': 'trivia', 'questions': questions}
