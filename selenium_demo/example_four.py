import time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
dir=os.path.dirname(__file__)
dir_chrome_driver=dir+"\chromedriver.exe"
driver=webdriver.Chrome(dir_chrome_driver)
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")
a_list=driver.find_elements_by_tag_name("a")
for i in a_list:
    print(i.text)

# dir=os.path.dirname(__file__)
# dir_chrome_driver=dir+"\chromedriver.exe"
# driver=webdriver.Chrome(dir_chrome_driver)
# driver.implicitly_wait(5)
# driver.get("https://www.qiushibaike.com/text/page/13")
# print(driver.find_element_by_css_selector(".pagination").text)