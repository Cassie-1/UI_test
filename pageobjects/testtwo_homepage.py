from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
from pageobjects.testone_homepage import Test_one_HomePage

class Test_Two_HomePage(BasePage):
    # 点击默认板块
    home_page_input_moren_loc = (By.CSS_SELECTOR, '.fl_tb h2 a')
    # 选择要删除的选项
    home_page_select_loc=(By.CSS_SELECTOR,'.o input')
    home_page_delete_loc=(By.XPATH,'//div[@id="mdly"]/p[1]/strong[1]/a')
    home_page_delete_enter_loc=(By.CSS_SELECTOR,'.pns .pnc span')
    # 点击管理中心
    home_page_guanli_loc=(By.LINK_TEXT,'管理中心')
    # 输入管理员密码
    home_page_password_loc=(By.CSS_SELECTOR,'.loginform .txt')
    home_page_submit_loc=(By.CSS_SELECTOR,'.btn')
    # 点击论坛
    home_page_click_luntan_loc=(By.CSS_SELECTOR,'.nav ul li:nth-child(7)')
    # 点击添加新版块
    home_page_click_new_border_loc=(By.CSS_SELECTOR,'.lastboard .addtr')
    # 找到新模块文本框
    home_page_new_txt_loc=(By.CSS_SELECTOR,'form .tb2 tbody:nth-last-child(2) .board .txt')
    # 找到提交按钮
    home_page_submit_new_loc=(By.CSS_SELECTOR,'.fixsel .btn')
    # 点击新增的板块
    home_page_click_new_loc=(By.CSS_SELECTOR,'.fl_tb tbody tr:nth-last-child(2) td:nth-child(2) a')
    # 发帖子
    home_page_input_title_loc = (By.NAME, 'subject')
    home_page_input_content_loc = (By.NAME, 'message')
    home_page_input_send_loc = (By.CSS_SELECTOR, '.pnpost .pn strong')

    def admin_login(self,username,password):
        self.testone=Test_one_HomePage(self.driver)
        self.testone.login(username,password)

    def delete(self):
        time.sleep(1)
        self.click(*self.home_page_input_moren_loc)
        time.sleep(1)
        self.click(*self.home_page_select_loc)
        print('111')
        time.sleep(1)
        self.click(*self.home_page_delete_loc)
        print('222')
        time.sleep(2)
        self.click(*self.home_page_delete_enter_loc)
        print('333')
        time.sleep(2)

    def enter_plate(self,password):
        time.sleep(1)
        self.click(*self.home_page_guanli_loc)
        time.sleep(1)
        self.change_window()
        time.sleep(1)
        self.sendkeys(password,*self.home_page_password_loc)
        time.sleep(1)
        self.click(*self.home_page_submit_loc)
        time.sleep(1)
        self.click(*self.home_page_click_luntan_loc)


    def new_plate(self,name):
        time.sleep(1)
        self.change_window()
        self.enter_iframe()
        time.sleep(2)
        self.click(*self.home_page_click_new_border_loc)
        print('点击新增版块按钮成功')
        time.sleep(1)
        self.clear(*self.home_page_new_txt_loc)
        time.sleep(1)
        print('清除新板块的名字成功')
        self.sendkeys(name,*self.home_page_new_txt_loc)
        print('输入新板块的名字成功')
        time.sleep(1)
        self.click(*self.home_page_submit_new_loc)
        # 退出管理中心
        time.sleep(2)
        self.change_window()
        self.testone.logout()

    def logout(self):
        # 管理员退出
        time.sleep(1)
        self.testone.logout()
        time.sleep(2)

    def login(self,name,pasw):
        time.sleep(1)
        self.testone.login(name,pasw)

    def send_post(self,title,content):
        time.sleep(3)
        self.click(*self.home_page_click_new_loc)
        print('lalalalala')
        time.sleep(1)
        self.sendkeys(title, *self.home_page_input_title_loc)
        self.sendkeys(content, *self.home_page_input_content_loc)
        self.click(*self.home_page_input_send_loc)

    def reply_post(self,content):
        time.sleep(1)
        self.testone.reply_post(content)