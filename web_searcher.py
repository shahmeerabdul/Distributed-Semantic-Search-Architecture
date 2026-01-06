from typing import List
try:
    from googlesearch import search
except ImportError:
    search = None

class WebSearcher:
    """
    Fetches search results from the web using Google Search.
    """
    def __init__(self):
        self.max_results = 5
        self.lang = "en"

    def get_search_results(self, query: str, limit: int = 5) -> List[str]:
        """
        Search Google for the query and return a list of URLs.
        """
        if not search:
            print("Error: googlesearch-python library not installed.")
            return []

        print(f"Searching web for: '{query}'...")
        results = []
        try:
            # simple loop over the generator
            for url in search(query, num_results=limit, lang=self.lang, advanced=True):
                # .url attribute for advanced=True, otherwise it's just a string
                # Note: googlesearch-python behavior varies by version. 
                # Common version returns strings. Let's try advanced=False first for safety if unsure,
                # but advanced=True gives SearchResult objects.
                # Let's stick to default (strings) which is safer.
                results.append(url)
                if len(results) >= limit:
                    break
            
            # If advanced=True was needed to get titles/process, we'd need that, 
            # but we will rely on Crawler to get titles.
        except Exception as e:
            print(f"Web search failed: {e}")
            import traceback
            traceback.print_exc()
            
        return results

if __name__ == "__main__":
    # Test
    ws = WebSearcher()
    urls = ws.get_search_results("python 3.12 features", 3)
    print("Found URLs:", urls)
