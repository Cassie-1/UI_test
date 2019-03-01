import time,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
dir=os.path.dirname(__file__)
dir_chrome_driver=dir+"\chromedriver.exe"
driver=webdriver.Chrome(dir_chrome_driver)
driver.implicitly_wait(5)

driver.get("https://mail.163.com/")
driver.switch_to.frame(0)
num=driver.find_element_by_name('email')
num.send_keys('15935623628')

# 弹窗相关
# driver.get("https://www.baidu.com")
# driver.execute_script("window.alert('这是一个弹出框！')")
# time.sleep(5)
# # driver.switch_to.alert.accept()   #点击弹窗上的确定按钮
# driver.switch_to.alert.dismiss()    #点击弹窗上的X按钮