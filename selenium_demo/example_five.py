import time
from selenium import webdriver
import os,re
from selenium.webdriver.common.keys import Keys
dir=os.path.dirname(__file__)
dir_chrome_driver=dir+"\chromedriver.exe"
driver=webdriver.Chrome(dir_chrome_driver)
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")
elem=driver.find_element_by_link_text("关于百度")
elem.click()
elem_lian=driver.find_element_by_link_text("联系我们")
elem_lian.click()
for handle in driver.window_handles:
    driver.switch_to_window(handle)
print("页面已打开",driver.title)
you=driver.find_elements_by_class_name("mail-content-text")
for i in you:
    str=i.text
    if '@' in str:
        print(i.text)

# 正则表达式
doc = driver.page_source
emails = re.findall(r'[\w]+@[\w\.-]+', doc)  # 利用正则，找出 xxx@xxx.xxx 的字段，保存到emails列表
# 循环打印匹配的邮箱
for email in emails:
    print(email)

# driver.close()
# # driver.switch_to.window(driver.fullscreen_window())
# driver.switch_to.window(driver.current_window_handle)
# current_url=driver.current_url
# driver.get(current_url)
# you=driver.find_elements_by_tag_name("span")
# you=driver.find_elements_by_class_name("mail-content-text")

