
import arxiv
import time
import fitz  # PyMuPDF
import requests
import io

class ArXivCollector:
    def __init__(self):
        self.client = arxiv.Client()
    
    def search_papers(self, query, max_results=20):
        """Search and extract full text from PDFs"""
        print(f"Searching arXiv for: {query}")
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )
        
        papers = []
        for result in self.client.results(search):
            print(f"Downloading/Parsing: {result.title}")
            full_text = self._download_and_extract_pdf(result.pdf_url)
            
            papers.append({
                'id': result.get_short_id(),
                'title': result.title,
                'authors': [author.name for author in result.authors],
                'abstract': result.summary,
                'full_text': full_text, # Added full text
                'published': result.published.date(),
                'pdf_url': result.pdf_url,
                'source': 'arxiv'
            })
            time.sleep(1.0) 
        return papers

    def _download_and_extract_pdf(self, url):
        """Downloads PDF and converts to text"""
        try:
            response = requests.get(url)
            with fitz.open(stream=io.BytesIO(response.content), filetype="pdf") as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
                return text
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return ""
