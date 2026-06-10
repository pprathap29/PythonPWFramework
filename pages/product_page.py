from playwright.sync_api import Page
class ProductPage(Page):
    def __init__(self, page:Page):
        self.page = page