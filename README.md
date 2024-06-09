
# openai-ass-contrllr

Project to mess around with Chat-/+GPTs with custom responses based on a jsonl file using OPENAI API and LANGCHAIN


<img src="bender.png" alt="drawing" width="200"/>


## Deployment

To use this project run

```bash
pip install -r requirements.txt
```

```bash
from bender.controller.chatbot_controller import ChatbotController

query = "XXXXXXXXXXXXXXXX?!"
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


#### Credits to Original Author
[See original repo for the original version]
Alejandro Castellanos
