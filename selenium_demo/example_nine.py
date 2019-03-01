from selenium import webdriver
import time,os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome('./chromedriver.exe')
driver.get("http://127.0.0.1/forum.php")
# 登录
driver.implicitly_wait(5)
username=driver.find_element_by_name('username')
username.clear()
username.send_keys('admin')
password=driver.find_element_by_name('password')
password.clear()
password.send_keys('admin')
driver.find_element_by_css_selector('.vm em').click()
time.sleep(1)
# 点击默认板块
driver.switch_to.window(driver.current_window_handle)
moren=driver.find_element_by_css_selector('.fl_tb h2 a')
moren.click()
time.sleep(1)

# 快速发帖
# title=driver.find_element_by_name('subject')
# title.send_keys('加油鸭呀')
# content=driver.find_element_by_name('message')
# content.send_keys('啦啦啦')
# send=driver.find_element_by_css_selector('.pnpost .pn strong')
# send.click()

# 点击第一条帖子
# title_name_list=driver.find_elements_by_css_selector('.new .xst')
# title_name_list[0].click()

# 回复帖子
# reply_kuang=driver.find_element_by_css_selector('.pt')
# reply_kuang.send_keys('嘿嘿，加油鸭')
# reply_button=driver.find_element_by_css_selector('.vm strong')
# reply_button.click()



# 下拉选项发帖
driver.switch_to.window(driver.current_window_handle)
menu = driver.find_element_by_id('newspecial')
hidden_submenu = driver.find_elements_by_css_selector('.hidefocus')
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
time.sleep(2)
driver.switch_to.window(driver.current_window_handle)
title=driver.find_element_by_id('subject')
title.send_keys('加油鸭233')
time.sleep(2)
content=driver.switch_to.frame('.area .pt:last-child')
# driver.switch_to.frame('message')
# content=driver.find_element_by_css_selector('.area .pt:last-child')
content.click()
content.send_keys('12345678')
fabiao=driver.find_element_by_id('postsubmit')
fabiao.click()
# ActionChains(driver).move_to_element(driver.find_element_by_id('newspecial')).click(driver.find_element_by_css_selector('.hidefocus')).perform()

# 退出
driver.find_element_by_link_text('退出').click()