import time,unittest
from testsuites.base_testcase import BaseTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from framework.browser_engine import BrowserEngine
from pageobjects.testone_homepage import Test_one_HomePage
from ddt import ddt,data,unpack

@ddt
class Testone_test(BaseTestCase):

    @unpack
    def test_one(self):
        test_one_homepage=Test_one_HomePage(self.driver)
        test_one_homepage.login('admin','admin')
        test_one_homepage.send_post('搭建框架','今天学习搭建自动化测试框架')
        test_one_homepage.reply_post('好好努力，加油鸭')
        test_one_homepage.logout()

if __name__=='__main__':
    unittest.main()