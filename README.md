# Research_Analyzer
An AI-powered research assistant that automates paper retrieval from arXiv, creates local vector embeddings for semantic search, and generates source-verified answers using Llama 3. It features a professional Streamlit dashboard that provides executive summaries and direct PDF links for evidence-based scholarly analysis.


AI Research AnalyzerAn advanced RAG (Retrieval-Augmented Generation) application that automates the discovery and analysis of academic literature. By integrating the arXiv API with Llama 3, this tool provides source-verified answers and executive summaries for complex research topics.
## Key Features
 # Automated arXiv Ingestion: 
 Automatically searches, downloads, and parses full-text PDFs based on your research topic.
 # Local Vector Intelligence: 
 Uses ChromaDB and HuggingFace embeddings (all-mpnet-base-v2) to create a searchable semantic index of scholarly papers.
 # Privacy-First LLM: 
 Leverages Llama 3 running locally via Ollama, ensuring your research data never leaves your machine.
 # Glassmorphism UI: 
 A high-end Streamlit dashboard featuring real-time status updates and a modern dark-mode aesthetic.
 # Verified Source Proof: 
 Every answer includes clickable links to the original arXiv PDF with specific page number citations.
 ## Project Research_Analyzer/
* ├── src/                    # Core Application Logic
* │   ├── app.py              # Streamlit User Interface
* │   ├── main.py             # Logic Orchestration
* │   ├── data_collector.py   # arXiv API & PDF Extraction
* │   ├── text_processor.py   # Recursive Character Splitting
* │   ├── vector_store.py     # ChromaDB & Embeddings Management
* │   ├── llm_engine.py       # Llama 3 & RAG Chain Setup
* │   └── config.py           # Global Hyperparameters
* ├── research_ui/            # Supplementary UI Components
* ├── .gitignore              # Excludes venv, data, and __pycache__
* └── requirements.txt        # Project Dependencies
* Enter a Research Topic (e.g., "Quantum Computing Errors").

* Input a Specific Question (e.g., "What are the current limitations of surface codes?").

* View the Executive Summary and the Source-Verified Answer.

* Technical ImplementationText Chunking: Documents are split into segments of 1000 characters with a 200-character overlap to maintain context across chunks.

* Embeddings: Powered by sentence-transformers/all-mpnet-base-v2 for state-of-the-art semantic search accuracy.

* Retrieval: Uses a Similarity Search to pull the most relevant context for the LLM.

* Generation: Implements LangChain's RetrievalQA with custom prompt engineering to prevent hallucinations.📜 


LicenseDistributed under the MIT License. See LICENSE for more information.
