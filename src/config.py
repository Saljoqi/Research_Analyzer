import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Vector Database
    VECTOR_DB_PATH = "./data/vector_db"
    
    # Embeddings Model 
    EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"
    
    # arXiv Settings
    ARXIV_MAX_RESULTS = 20
    
    # Text Processing
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200