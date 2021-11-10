class MainPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("http://localhost:5000")

    def submit(self, text):
        # self.page.fill('[aria-label="Enter your search term"]', text)
        self.page.press('[class="btn btn-primary"]', "Enter")
