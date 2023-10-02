from bender.controller.chatbot_controller import ChatbotController


def test_success_chat_bot_response(mocker, mocker_set_question, mocker_get_answer):
    query = "cual es la pagina web de wikipedia?"
    jsonl_path = 'company_data.jsonl'

    instance = ChatbotController(jsonl_path=jsonl_path)
    instance.set_question(query)
    assert instance.get_answer() == 'La página web de Wikipedia es https://es.wikipedia.org/'
