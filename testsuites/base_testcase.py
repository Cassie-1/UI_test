import unittest,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from framework.browser_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome('../tools/chromedriver.exe')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        self.browserEngine = BrowserEngine()
        self.driver=self.browserEngine.open_browser()

    def tearDown(self):
        time.sleep(3)
        # self.driver.quit()

        self.browserEngine.quit_browser()