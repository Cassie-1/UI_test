from pageobjects.base import BasePage
from pageobjects.testone_homepage import Test_one_HomePage
import time
from selenium.webdriver.common.by import By

class Test_Three_HomePage(BasePage):
    # 找到搜索文本框
    search_input_loc=(By.CSS_SELECTOR,'.cl form table tbody tr td:nth-child(2) input')
    # 找到搜索按钮
    search_button_loc=(By.CSS_SELECTOR,'.scbar_btn_td .pnc')
    # 查看帖子
    look_post_loc=(By.CSS_SELECTOR,'.xs3 a')
    # 打开帖子
    open_post_loc=(By.CSS_SELECTOR,'.ts')

    def login(self):
        self.testone=Test_one_HomePage(self.driver)
        self.testone.login('lucky','lucky')
        time.sleep(2)
    def search(self,content):
        self.clear(*self.search_input_loc)
        time.sleep(2)
        self.sendkeys(content,*self.search_input_loc)
        time.sleep(2)
        self.click(*self.search_button_loc)
        time.sleep(2)
    def enter_post(self):
        self.change_window()
        time.sleep(1)
        self.click(*self.look_post_loc)
        # self.get_windows_img()
        time.sleep(1)
    def check(self):
        self.change_window()
        time.sleep(1)
        title=self.get_text(*self.open_post_loc)
        # self.get_windows_img()
        return title

    def logout(self):
        self.close()
        self.change_window()
        self.close()
        self.change_window()
        self.testone.logout()
        time.sleep(1)