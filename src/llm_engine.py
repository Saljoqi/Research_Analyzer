from langchain_openai import ChatOpenAI

from langchain_ollama import ChatOllama
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

class LLMEngine:
    def __init__(self):
        # Requires OPENAI_API_KEY in your .env
        self.llm = ChatOllama(
            model="llama3", 
            base_url="http://localhost:11434",
            temperature=0.5
        )

    def get_qa_chain(self, vector_store):
        template = """You are a professional research assistant. Use the following context 
        to answer the user's question accurately.
        
        Context: {context}
        Question: {question}
        
        Answer:"""
        
        prompt = PromptTemplate(template=template, input_variables=["context", "question"])
        
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt}
        )
    

    def generate_summary(self, papers):
        """Generates a high-level summary of all discovered papers"""
        # Combine all abstracts into one text block
        combined_text = "\n\n".join([
            f"Paper: {p['title']}\nAbstract: {p['abstract']}" 
            for p in papers
        ])

        summary_prompt = f"""
        You are a senior research scientist. Summarize the following research papers 
        into a concise executive summary. Highlight the common themes, 
        key methodologies used, and the overall direction of the field.

        Papers:
        {combined_text}

        Executive Summary:
        """
        
        # Use invoke directly for a one-off generation
        response = self.llm.invoke(summary_prompt)
        return response.content