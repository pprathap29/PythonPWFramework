from playwright.sync_api import Page
class SearchResult(Page):
    def __init__(self, page:Page):
        self.page = page