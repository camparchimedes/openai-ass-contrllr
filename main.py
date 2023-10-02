#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bender.controller.chatbot_controller import ChatbotController


def main():
    query = "mi pregunta"

    jsonl_path = 'company_data.jsonl'

    instance = ChatbotController(jsonl_path=jsonl_path)
    instance.set_question(query)
    response = instance.get_answer()
    print('chatbot response', response)


if __name__ == "__main__":
    main()
