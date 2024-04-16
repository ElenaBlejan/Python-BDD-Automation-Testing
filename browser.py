from selenium import webdriver


class Browser:
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(3)

    def close(self):
        self.chrome.delete_all_cookies()
        self.chrome.quit()