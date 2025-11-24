from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_LOGIN = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button')

class ProductPageLocators():
    ARTICLE = (By.CSS_SELECTOR, 'article.product_page')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    TEXT_TO_CHECK = (By.CSS_SELECTOR, '#messages div.alertinner strong')
    VALUE_TO_CHECK = (By.CSS_SELECTOR, '#messages div.alert-info p strong')
    EXPECTED_TEXT = (By.CSS_SELECTOR, 'article.product_page div.product_main h1')
    EXPECTED_VALUE = (By.CSS_SELECTOR, 'article.product_page div.product_main p.price_color')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BUTTON_TO_PAGE = (By.CSS_SELECTOR, 'div.basket-mini a')
    TEXT = (By.CSS_SELECTOR, '#content_inner > p')