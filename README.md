
# openai-bender

Project to create chatbots with custom responses based on a jsonl file using OPENAI API and LANGCHAIN


<img src="bender.png" alt="drawing" width="200"/>


## Deployment

To use this project run

```bash
pip install -r requirements.txt
```

```bash
from bender.controller.chatbot_controller import ChatbotController

query = "pregunta al chatbot"
jsonl_path = 'company_data.jsonl'

instance = ChatbotController(jsonl_path=jsonl_path)

instance.set_question(query)

response = instance.get_answer()

print(response)

```

or


```bash
python main.py

```


#### Author
Alejandro Castellanos
