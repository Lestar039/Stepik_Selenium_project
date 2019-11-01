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

    def register_new_user(self, email, password):
        MainPage.go_to_login_page(self)
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_pass_input1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_INPUT1)
        input_pass_input1.send_keys(password)
        input_pass_input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_INPUT2)
        input_pass_input2.send_keys(password)
        btn_submit = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        btn_submit.click()
