# my_account_page.py
# =====================
# This class represents the "My Account Page" of the application.
# It is designed using the Page Object Model (POM) pattern.

from playwright.sync_api import Page

from pages.logout_page import LogoutPage


class MyAccountPage:
    """Page Object Model class for the My Account Page."""

    def __init__(self, page: Page):
        """
        Constructor that initializes the Playwright Page instance
        and defines all locators used on the My Account Page.
        """
        self.page = page

        # ===== Locators =====
        self.heading_my_account = page.locator('#content h2:nth-child(1)')
        self.lnk_logout = page.locator("//a[@class='list-group-item'][normalize-space()='Logout']")


    # ===== Action Methods =====

    def get_my_account_page_heading(self):
        """
        Return the My Account page heading element.
        Example use:
            expect(my_account_page.get_my_account_page_heading()).to_be_visible()
        """
        try:
            return self.heading_my_account
        except Exception as e:
            print(f" Exception while fetching My Account page heading: {e}")
            return None# my_account_page.py

    def click_logout(self) -> LogoutPage:
        """
        Clicks on the 'Logout' link to log out the user.
        Returns an instance of the LogoutPage class
        to allow chained navigation in tests.

        Example:
            logout_page = my_account_page.click_logout()
        """
        try:
            self.lnk_logout.click()
            return LogoutPage(self.page)
        except Exception as e:
            print(f"Unable to click Logout link: {e}")
            raise e

    def page_title(self):
        try:
            return self.page.title()
        except Exception as e:
            print(f" Exception while fetching page title: {e}")
            raise ""



