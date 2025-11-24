from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, f'Incorrect url. {self.url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTER_LOGIN), 'Login input is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_1), 'Password1 input is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_2), 'Password2 input is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), 'Registration button is not presented'

        login = self.browser.find_element(*LoginPageLocators.REGISTER_LOGIN)
        login.send_keys(email)
        password_1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        password_1.send_keys(password)
        password_2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        password_2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()