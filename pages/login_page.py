from .base_page import BasePage
from .locators import LoginPageLocators
from .main_page import MainPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        MainPage.go_to_login_page(self)
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        MainPage.go_to_login_page(self)
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'There is not a login form'

    def should_be_register_form(self):
        MainPage.go_to_login_page(self)
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'There is not a register form'
