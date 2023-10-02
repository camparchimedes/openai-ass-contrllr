import jsonlines

from langchain.schema import Document
from typing import List


class TransformerDocJSONLoader:

    """
        Args:
            file_path = "jsonl path"
            JSONL Format {"title": "", "repo_owner": "", "repo_name": "", "text": ""}

        Instance:
            _instance = TransformerDocJSONLoader()

        Returns:
            jsonl_document_obj = loader.custom_load()
    """

    def __init__(self, file_path):
        self._file_path = file_path

    def custom_load(self) -> List[Document]:
        with jsonlines.open(self._file_path) as reader:
            documents = []
            for obj in reader:
                page_content = obj.get("text", "")
                metadata = {
                    'title': obj.get("title", ""),
                    'repo_owner': obj.get("repo_owner", ""),
                    'repo_name': obj.get("repo_name", ""),
                }
                documents.append(
                    Document(page_content=page_content, metadata=metadata)
                )
        return documents
