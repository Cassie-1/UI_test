from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Test_one_HomePage(BasePage):
    # 登录
    home_page_input_username_loc = (By.NAME, 'username')
    home_page_input_password_loc = (By.NAME, 'password')
    home_page_input_login_loc = (By.CSS_SELECTOR, '.vm em')
    # 点击默认板块
    home_page_input_moren_loc = (By.CSS_SELECTOR, '.fl_tb h2 a')
    # 发帖子
    home_page_input_title_loc = (By.NAME, 'subject')
    home_page_input_content_loc = (By.NAME, 'message')
    home_page_input_send_loc = (By.CSS_SELECTOR, '.pnpost .pn strong')
    # 回复帖子
    home_page_input_reply_kuang_loc = (By.CSS_SELECTOR,'.pt')
    home_page_input_reply_button_loc = (By.CSS_SELECTOR,'.vm strong')
    # 退出
    home_page_input_logout_loc=(By.LINK_TEXT,'退出')

    def login(self,username,password):
        self.clear(*self.home_page_input_username_loc)
        self.sendkeys(username,*self.home_page_input_username_loc)
        self.clear(*self.home_page_input_password_loc)
        self.sendkeys(password, *self.home_page_input_password_loc)
        self.click(*self.home_page_input_login_loc)

    def send_post(self,title,content):
        time.sleep(1)
        self.click(*self.home_page_input_moren_loc)
        time.sleep(1)
        self.sendkeys(title, *self.home_page_input_title_loc)
        self.sendkeys(content, *self.home_page_input_content_loc)
        self.click(*self.home_page_input_send_loc)

    def reply_post(self,content):
        self.sendkeys(content, *self.home_page_input_reply_kuang_loc)
        self.click(*self.home_page_input_reply_button_loc)

    def logout(self):
        time.sleep(1)
        self.click(*self.home_page_input_logout_loc)