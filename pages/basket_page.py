from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT), 'Basket not empty, but should not be'

    def should_not_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.TEXT), 'Basket empty, but should not be'

    def should_be_empty_text_basket(self):
        text = self.browser.find_element(*BasketPageLocators.TEXT).text
        assert len(text) != 0, f'Basket have some text, but should not {text}'

    def should_not_be_empty_text_basket(self):
        text = self.browser.find_element(*BasketPageLocators.TEXT).text
        assert len(text) > 0, f'Basket have not some text, but should'