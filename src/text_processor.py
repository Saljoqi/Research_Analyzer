
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import Config

class TextProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE, #
            chunk_overlap=Config.CHUNK_OVERLAP, #
            length_function=len
        )
    
    def papers_to_documents(self, papers):
        documents = []
        for paper in papers:
            # Use full text if available, otherwise abstract
            content = paper['full_text'] if paper['full_text'] else paper['abstract']
            
            metadata = {
                'paper_id': paper['id'],
                'title': paper['title'],
                'authors': ", ".join(paper['authors']), #
                'source': paper['source']
            }
            documents.append(Document(page_content=content, metadata=metadata))
        return documents

    def chunk_documents(self, documents):
        return self.text_splitter.split_documents(documents) #