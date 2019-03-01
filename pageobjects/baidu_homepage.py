from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    home_page_input_search_loc=(By.CSS_SELECTOR,'.quickdelete-wrap .s_ipt')
    home_page_button_search_loc=(By.CSS_SELECTOR,'.s_btn_wr .s_btn')

    def search(self,content):
        self.clear(*self.home_page_input_search_loc)
        self.sendkeys(content,*self.home_page_input_search_loc)
        self.click(*self.home_page_button_search_loc)