from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    NAME_FIELD = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_ADRESS = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    BUTTON_SIGNUP = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def insert_name(self,name):
        self.chrome.find_element(*self.NAME_FIELD).send_keys(name)

    def insert_email_adress(self,email_adress):
        self.chrome.find_element(*self.EMAIL_ADRESS).send_keys(email_adress)

    def click_button_signup(self):
        self.chrome.find_element(*self.BUTTON_SIGNUP).click()