
from data_collector import ArXivCollector
from vector_store import VectorStore
from text_processor import TextProcessor
from llm_engine import LLMEngine

import shutil 
import os

def make_clickable(url, label):
    """Creates a clickable link for modern terminals"""
    # ESC ] 8 ; ; URL ESC \ Label ESC ] 8 ; ; ESC \
    return f"\033]8;;{url}\033\\{label}\033]8;;\033\\"


def run_research_assistant(topic, question):
    # Fresh start: Clear old vector data
    if os.path.exists("./data/vector_db"):
        shutil.rmtree("./data/vector_db")
        print("--- Cleared old database for fresh research ---")

    # 1. Collect Papers
    collector = ArXivCollector()
    papers = collector.search_papers(topic, max_results=5)
    
    if not papers:
        print("No papers found.")
        return

    # 2. Generate Executive Summary (New Step!)
    llm_engine = LLMEngine()
    print("\n--- Generating Research Executive Summary ---")
    summary = llm_engine.generate_summary(papers)
    # print(f"\nSUMMARY:\n{summary}\n")


    # 3. Build Vector DB
    processor = TextProcessor()
    docs = processor.papers_to_documents(papers)
    chunks = processor.chunk_documents(docs)
    
    vs_manager = VectorStore()
    vector_store = vs_manager.create_from_documents(chunks)
    
    # 4. Specific Question Answering
    qa_chain = llm_engine.get_qa_chain(vector_store)
    
    # print(f"\n--- Answering specific question: {question} ---")
    response = qa_chain.invoke(question)
    # print("\nDETAILED ANSWER:")
    # print(response["result"])
    detailed_answer = response["result"]



    print("\n--- SOURCES VERIFIED (Click to open) ---")
    
    verified_sources = []
    unique_titles = set()
    for doc in response["source_documents"]:
        title = doc.metadata.get("title", "Research Paper")
        url = doc.metadata.get("source", "") 
        page_num = doc.metadata.get("page", 0) + 1 
        
        if url and title not in unique_titles:
            verified_sources.append({
                "title": title,
                "url": url,
                "page": page_num
            })
            unique_titles.add(title)

    # NEW: Return everything as a tuple
    return summary, detailed_answer, verified_sources







    # --- END OF NEW CODE BLOCK ---







if __name__ == "__main__":
    topic = "LoRA fine-tuning efficiency"
    question = "How much VRAM does LoRA save compared to full fine-tuning?"
    run_research_assistant(topic, question)