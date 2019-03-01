import time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
dir=os.path.dirname(__file__)
dir_chrome_driver=dir+"\chromedriver.exe"
driver=webdriver.Chrome(dir_chrome_driver)
try:

    driver.implicitly_wait(5)
    driver.get("http://www.baidu.com")
    driver.switch_to.window(driver.current_window_handle)
    print("成功打开百度窗口：",driver.title)
    elem=driver.find_element_by_id("kw")
    elem.send_keys("java")
    elem.submit()
    driver.switch_to.window(driver.current_window_handle)
    elem_result=driver.find_element_by_class_name("nums_text")
    print(elem_result.text)
    driver.switch_to.window(driver.current_window_handle)
    wait_second=5
    # driver.execute_script("window.alert(\"{}, {}秒后关闭\")".format(nums.text.replace("\n", "$"), wait_seconds))
    driver.execute_script("window.alert(\"{},{}秒后自动关闭\")".format(elem_result.text.replace("\n", "$"),wait_second))
    time.sleep(wait_second)
finally:
    driver.quit()