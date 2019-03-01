import time,unittest
from testsuites.base_testcase import BaseTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.baidu_homepage import HomePage
from framework.browser_engine import BrowserEngine

class BaiduSearch(BaseTestCase):
    def test_baidu_search(self):
        # self.driver.get('https://www.baidu.com')
        # text_kuang=self.driver.find_element_by_css_selector('.quickdelete-wrap .s_ipt')
        # text_kuang.send_keys('java')
        # search_button=self.driver.find_element_by_css_selector('.s_btn_wr .s_btn')
        # search_button.click()
        # self.assertEqual()

        # brower_engine=BrowerEngine(self.driver)

        # home_page=HomePage(self.driver)
        # home_page.get('https://www.baidu.com')
        # home_page.search('java')

        # brower_engine=BrowerEngine()
        home_page = HomePage(self.driver)
        # home_page.get('https://www.baidu.com')
        home_page.search('java')

if __name__=='__main__':
    unittest.main()