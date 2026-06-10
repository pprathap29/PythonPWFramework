from playwright.sync_api import Page
class LogoutPage:
    def __init__(self,page:Page):
        self.page = page