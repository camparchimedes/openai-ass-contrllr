from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma


from bender.settings.base import OPENAI_API_KEY, TEMPLATE, MODEL_NAME, EMBEDDING_MODEL
from bender.utils.json_loader import TransformerDocJSONLoader


class ChatbotController:

    """
        Args:
            jsonl_path = "jsonl path"
            query = "question text for chatbot"

        Instance:
            _instance = ChatbotController(jsonl_path)
            _instance.set_question(query)

        Returns:
            response = _instance.get_answer()
    """

    __slots__ = (
        '_embeddings',
        '_template',
        '_model_name',
        '_jsonl_path',
        '_set_answer'
    )

    def __init__(self, jsonl_path):
        self._jsonl_path = jsonl_path
        self._model_name = MODEL_NAME
        self._template = TEMPLATE
        self._embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
        self._set_answer = None

    def set_question(self, query):
        self._persist_vectorstore()
        qa_chain = RetrievalQA.from_chain_type(
            llm=self._chat_open_ai_instance(),
            retriever=self._load_vectorstore(),
        )
        query_format = self._template.format(query)
        self._set_answer = qa_chain.run(query_format)

    def get_answer(self):
        return self._set_answer

    def _load_json_data(self):
        transformer_doc_json_loader_instance = TransformerDocJSONLoader(self._jsonl_path)
        return transformer_doc_json_loader_instance.custom_load()

    def _text_splitter(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            length_function=len,
        )
        return text_splitter.split_documents(self._load_json_data())

    def _persist_vectorstore(self):
        vectorstore = Chroma.from_documents(
            documents=self._text_splitter(),
            embedding=self._embeddings,
            persist_directory='company_data'
        )
        vectorstore.persist()

    def _load_vectorstore(self):
        load_vectorstore = Chroma(
            persist_directory='company_data',
            embedding_function=self._embeddings
        )
        return load_vectorstore.as_retriever(
            search_kwargs={"k": 2}
        )

    def _chat_open_ai_instance(self):
        return ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            model_name=self._model_name,
            temperature=0.0,
            max_tokens=500
        )
