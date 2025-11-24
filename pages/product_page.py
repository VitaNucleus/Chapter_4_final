import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_on_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ARTICLE), f'Opened page is not product page is {self.url}'

    def should_be_a_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), f'Button add to basket not exist'
        return self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.TEXT_TO_CHECK), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.TEXT_TO_CHECK), \
            "Success message is disappeared, but should not be"

    def should_be_a_added_product(self):
        assert self.is_element_present(*ProductPageLocators.TEXT_TO_CHECK), f'Product shouldnt add to basket'
        assert self.is_element_present(*ProductPageLocators.VALUE_TO_CHECK), f'Product shouldnt add to basket'

        expexted_text = self.browser.find_element(*ProductPageLocators.EXPECTED_TEXT).text
        expexted_value = self.browser.find_element(*ProductPageLocators.EXPECTED_VALUE).text

        text = self.browser.find_element(*ProductPageLocators.TEXT_TO_CHECK).text
        value = self.browser.find_element(*ProductPageLocators.VALUE_TO_CHECK).text

        assert expexted_text == text, f'Book name is another {text}, but should be {expexted_text}'
        assert expexted_value == value, f'Book value is another {value}, but should be {expexted_value}'
