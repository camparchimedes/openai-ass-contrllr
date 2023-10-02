from pytest import fixture

from bender.controller.chatbot_controller import ChatbotController


@fixture
def mocker_set_question(mocker):
    mocker.patch.object(ChatbotController, 'set_question', return_value=True)


@fixture
def mocker_get_answer(mocker):
    response = 'La página web de Wikipedia es https://es.wikipedia.org/'
    mocker.patch.object(ChatbotController, 'get_answer', return_value=response)
