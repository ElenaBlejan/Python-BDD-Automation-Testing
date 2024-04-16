from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    SIGNUP_LOGIN_BUTTON = (By.PARTIAL_LINK_TEXT, "Signup")

    def navigate_to_home_page(self):
        self.chrome.get("https://automationexercise.com/")

    def click_on_signup_login_button(self):
        self.chrome.find_element(*self.SIGNUP_LOGIN_BUTTON).click()