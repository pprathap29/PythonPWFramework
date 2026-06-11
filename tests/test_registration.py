import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.registration_page import Registration
from utilities.radom_data_util import RandomDataUtil

@pytest.mark.sanity
def test_user_registration(page):

    home_page = HomePage(page)
    registration = Registration(page)

    home_page.click_my_account()
    home_page.click_register()

    random_data = RandomDataUtil()
    first_name = random_data.get_first_name()
    last_name = random_data.get_last_name()
    email = random_data.get_email()
    phone_number = random_data.get_phone_number()
    password = random_data.get_password()


    registration.set_first_name(first_name)
    registration.set_last_name(last_name)
    registration.set_email(email)
    registration.set_tel_number(phone_number)
    registration.set_password(password)
    registration.set_confirm_password(password)
    registration.privacy_policy()
    registration.click_continue_button()
    confirm_message = registration.get_confirm_message()
    expect(confirm_message).to_be_visible()