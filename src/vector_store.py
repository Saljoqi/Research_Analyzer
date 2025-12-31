
import os
from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from config import Config

class VectorStore:
    def __init__(self):
        # Use the model defined in your Config
        self.embeddings = HuggingFaceEmbeddings(model_name=Config.EMBEDDING_MODEL)
        self.persist_directory = Config.VECTOR_DB_PATH
        
        # Ensure the storage directory exists
        os.makedirs(self.persist_directory, exist_ok=True)
        self.vector_store = None
    
    def create_from_documents(self, documents):
        """Step 5: Persist embeddings + metadata in vector DB"""
        print(f"Creating vector store at {self.persist_directory}...")
        
        # Using Chroma.from_documents initializes the DB and saves it
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        print("Vector store created and persisted!")
        return self.vector_store
    
    def load_existing(self):
        """Load the indexed vector DB for retrieval"""
        self.vector_store = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings
        )
        return self.vector_store
    
    def search(self, query, k=5):
        """Step 6: Perform semantic similarity search"""
        if self.vector_store is None:
            self.load_existing()
        
        # Returns relevant Document objects with metadata
        return self.vector_store.similarity_search(query, k=k)

    def as_retriever(self, k=5):
        """Helper to convert the store into a LangChain retriever"""
        if self.vector_store is None:
            self.load_existing()
        return self.vector_store.as_retriever(search_kwargs={"k": k})