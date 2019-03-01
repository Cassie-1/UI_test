# POM设计模式具体应用：
# 1. 封装一个所有页面的父类，存放的是与业务无关的，所有页面的公共方法（一个基类）
#    方法：back、forward、open_url、quit_browser、close、find_element、sendkeys、click、clear
# 2. 某一个具体页面来说，存放的是该页面的元素，以及该页面所特有的业务方法（所有的产品页面）
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
import os,time

logger=Logger(logger='BasePage').getlog()

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.actions = ActionChains(self.driver)

    def back(self):
        self.driver.back()

    def get(self,url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info('找到页面元素')
            return self.driver.find_element(*loc)
        except Exception as e:
            logger.info('未找到页面元素：%s'%e)
            self.get_windows_img()

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except Exception as e:
            logger.info('未找到页面元素：%s'%e)
            self.get_windows_img()

    def sendkeys(self,text,*loc):
        try:
            e1 = self.find_element(*loc)
            e1.send_keys(text)
            logger.info('文本框成功写入文本：%s'%text)
        except Exception as e:
            logger.error('文本框写入文本失败：%s'%e)
            self.get_windows_img()

    def clear(self,*loc):
        try:
            e1 = self.find_element(*loc)
            e1.clear()
            logger.info('清除文本框成功')
        except Exception as e:
            logger.error('清楚文本框失败：%s'%e)
            self.get_windows_img()

    def click(self,*loc):
        try:
            e1 = self.find_element(*loc)
            e1.click()
            logger.info('点击操作成功')
        except Exception as e:
            logger.error('点击操作失败：%s'%e)
            self.get_windows_img()

    def change_window(self):
        try:
            windows_list = self.driver.window_handles
            self.driver.switch_to.window(windows_list[len(windows_list)-1])
            logger.info('切换窗口成功')
        except Exception as e:
            logger.error('切换窗口失败：%s'%e)
            self.get_windows_img()

    def get_text(self,*loc):
        try:
            e1=self.find_element(*loc)
            text=e1.text
            logger.info('得到文本内容：%s'%text)
            return text
        except Exception as e:
            logger.error('未得到文本：%s'%e)
            self.get_windows_img()

    def enter_iframe(self):
        self.driver.switch_to.frame(0)

    # def select_hidden_menu(self,*loc):
    #     # actions = ActionChains(self.driver)
    #     menu=self.find_element(*loc)
    #     self.actions.move_to_element(menu)
    # def select_hidden(self,*loc):
    #     # actions = ActionChains(self.driver)
    #     hidden_submenu=self.find_element(*loc)
    #     self.actions.click(hidden_submenu)
    #     self.actions.perform()

    def get_texts(self,*loc):
        e1=self.find_elements(*loc)
        text_list=[]
        for i in e1:
            text_list.append(i.text)
        return text_list

    def get_ratios(self,*loc):
        e1=self.find_elements(*loc)
        ratio_list=[]
        text_list = []
        # text_ratio_list=[]
        for i in range(0,len(e1)):
            # text_ratio_list.append(e1[i].text)
            if i%2!=0:
                ratio_list.append(e1[i].text)
            else:
                text_list.append(e1[i].text)
        return ratio_list

    # 得到截屏
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name=file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('截图保存到 /screenshots')
        except Exception as e:
            self.get_windows_img()
            logger.error('获取截图失败，因为%s'%e)



