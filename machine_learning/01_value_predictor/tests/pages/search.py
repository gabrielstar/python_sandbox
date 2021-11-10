class SearchPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://bing.com")

    def search(self, text):
        self.page.fill('[aria-label="Enter your search term"]', text)
        self.page.press('[aria-label="Enter your search term"]', "Enter")
