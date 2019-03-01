import time,unittest
from testsuites.base_testcase import BaseTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.baidu_homepage import HomePage
from framework.browser_engine import BrowserEngine
from ddt import ddt,data,unpack
from unit_test.util import Util

testdata=Util.read_excel('G:\\pythonWorkSpace\\workspace\\UI_autotest\\data\\data.xlsx', 'Sheet1')

@ddt
class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome('../tools/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(5)

    @data(*testdata)
    def test_baidu_search_by_ddt(self,data):
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
        # home_page = HomePage(self.driver)
        # home_page.get('https://www.baidu.com')
        # home_page.search('java')
        search_string=data['content']
        print('搜索内容：%s'%search_string)
        search_input=self.driver.find_element_by_css_selector('.quickdelete-wrap .s_ipt')
        search_input.send_keys(search_string)
        time.sleep(3)
        search_input.submit()

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()