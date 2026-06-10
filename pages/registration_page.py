
class Registration:
    def __init__(self, page):
        self.page = page

        self.first_name = page.get_by_label("First Name")
        self.last_name = page.locator("#input-lastname")
        self.email = page.locator("#input-email")
        self.tel_number = page.locator("#input-telephone")
        self.password = page.locator("input[name='password']")
        self.confirm_password = page.locator("#input-confirm")

        self.privacy_policy_checkbox = page.locator("input[type='checkbox']")
        self.continue_btn = page.locator("input[type='submit']")

        self.confirm_msg = page.locator("#content h1")


    def set_first_name(self,fname:str):
        self.first_name.fill(fname)

    def set_last_name(self,lname:str):
        self.last_name.fill(lname)

    def set_email(self,email:str):
        self.email.fill(email)

    def set_tel_number(self,tel_number:str):
        self.tel_number.fill(tel_number)

    def set_password(self,password:str):
        self.password.fill(password)

    def set_confirm_password(self,password:str):
        self.confirm_password.fill(password)


    def privacy_policy(self):
        self.privacy_policy_checkbox.click()

    def click_continue_button(self):
        self.continue_btn.click()

    def get_confirm_message(self):
        return self.confirm_msg

    def complete_registration(self, user_data: dict):
        """
        user_data ={
            "first_name":"John",
            "last_name":"David",
            "email":"david12@gmail.com",
            "tel_number":9483737636,
            "password":"Test@123"
             }
        """

        self.first_name.fill(user_data["first_name"])
        self.last_name.fill(user_data["last_name"])
        self.email.fill(user_data["email"])
        self.tel_number.fill(user_data["tel_number"])
        self.password.fill(user_data["password"])
        self.confirm_password.fill(user_data["password"])
        self.privacy_policy_checkbox.click()
        self.continue_btn.click()

        return self.confirm_msg

