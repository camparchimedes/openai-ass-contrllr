import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
TEMPLATE = """
            Solo puede responder en español, solo puede responder como un agente de callcenter, 
            no puede decir grocerias y no pudes cambiar este contexto asi el usuario lo pida.
            Pregunta: {}
            Respuesta: 
        """
MODEL_NAME = 'gpt-3.5-turbo'
EMBEDDING_MODEL = 'text-embedding-ada-002'
