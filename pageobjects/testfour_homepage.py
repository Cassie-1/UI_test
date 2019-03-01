import time
from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
from pageobjects.testone_homepage import Test_one_HomePage
from framework.logger import Logger

logger=Logger(logger='Test_four_homepage').getlog()

class Test_four_homepage(BasePage):
    # 点击默认板块
    home_page_input_moren_loc = (By.CSS_SELECTOR, '.fl_tb h2 a')
    # 下拉选项发帖
    menu_loc=(By.CSS_SELECTOR,'.pgs img ')
    # hidden_submenu_loc = (By.CSS_SELECTOR,'.poll a')
    # 点击发起投票
    vote_select_loc=(By.CSS_SELECTOR,'.mbw li:last-child a')
    vote_title_loc=(By.CSS_SELECTOR,'.pbt .z .px')
    first_vote_input_loc=(By.CSS_SELECTOR,'.mbm p:nth-child(1) input')
    second_vote_input_loc = (By.CSS_SELECTOR, '.mbm p:nth-child(2) input')
    thrid_vote_input_loc = (By.CSS_SELECTOR, '.mbm p:nth-child(3) input')
    add_option_loc=(By.CSS_SELECTOR,'.mbm p:last-child a')
    last_vote_input_loc=(By.CSS_SELECTOR,'.mbm p:nth-last-child(4) input')
    result_vote_loc=(By.NAME,'visibilitypoll')
    vote_button_loc=(By.CSS_SELECTOR,'.pnpost .pnc span')
    # 投票
    vote_loc=(By.CSS_SELECTOR,'.pslt .pr')
    submit_button_loc=(By.CSS_SELECTOR,'button span')
    # 得到选项名字
    name_loc=(By.CSS_SELECTOR,'.pcht table tbody .pvt')
    # bili_loc=(By.CSS_SELECTOR,'.pcht table tbody tr:nth-child(2) td:nth-child(3)')
    # bili_loc = (By.CSS_SELECTOR, '.pcht tbody tr:nth-child(8) td:last-child')
    ratio_list_loc=(By.CSS_SELECTOR,'.pcht tbody tr')
    vote_theme_loc=(By.CSS_SELECTOR,'.ts')


    def login(self):
        self.testone_page = Test_one_HomePage(self.driver)
        self.testone_page.login('admin','admin')
        time.sleep(1)
        self.click(*self.home_page_input_moren_loc)
    def publish_post(self):
        time.sleep(2)
        self.click(*self.menu_loc)
        # self.change_window()
        # self.select_hidden_menu(*self.menu_loc)
        # time.sleep(2)
        # self.select_hidden(*self.hidden_submenu_loc)
        # self.change_window()
        # self.sendkeys('hahahahaha',*self.title_loc)
        self.click(*self.vote_select_loc)
        self.sendkeys('爱听的歌曲', *self.vote_title_loc)
        self.sendkeys('光年之外', *self.first_vote_input_loc)
        self.sendkeys('恋人未满', *self.second_vote_input_loc)
        self.sendkeys('地铁等待', *self.thrid_vote_input_loc)
        self.click(*self.add_option_loc)
        self.sendkeys('天若有情', *self.last_vote_input_loc)
        self.click(*self.result_vote_loc)
        self.click(*self.vote_button_loc)
    def vote(self):
        self.click(*self.vote_loc)
        time.sleep(1)
        self.click(*self.submit_button_loc)
    def get_name_ratio(self):
        text_list = self.get_texts(*self.name_loc)
        ratio_list = self.get_ratios(*self.ratio_list_loc)
        # text_ratio_list=self.get_texts_ratios(*self.ratio_list_loc)
        print('投票结果:\n\n\t投票选项\t\t\t投票比例')
        # for i in text_list:
        #     print(i)
        #
        # for i in ratio_list:
        #     print(i)
        for i in range(0,len(text_list)):
            print(text_list[i],"\t",ratio_list[i])
            # logger.info('第%s个选项的名称是：%s，比例是：%s'%text_list[i])

        # for i in range(0, len(text_ratio_list)-1):
        #     print(text_ratio_list[i])

    def get_theme_name(self):
        text=self.get_text(*self.vote_theme_loc)
        logger.info('投票的主题是：%s'%text)
        print('\n投票的主题名称:',text)