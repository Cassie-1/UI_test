from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

# 打开一个chrome浏览器，百度官网
# dir=os.path.dirname(__file__)
# chrome_dir_path=dir+"\chromedriver.exe"
# driver=webdriver.Chrome(chrome_dir_path)
# driver.get("http://www.baidu.com")
# assert "百度" in driver.title

# 打开一个火狐浏览器，百度官网
# dir_fire=os.path.dirname(__file__)
# fire_dir_path=dir_fire+"\geckodriver.exe"
# driver_fire=webdriver.Firefox(executable_path=fire_dir_path)
# driver_fire.get("http://www.baidu.com")
# assert "百度" in driver_fire.title

# 打开一个IE浏览器，百度官网
# dir_Ie=os.path.dirname(__file__)
# Ie_dir_path=dir_Ie+"\IEDriverServer.exe"
# driver_Ie=webdriver.Ie(Ie_dir_path)
# driver_Ie.get("http://www.baidu.com")
# assert "百度" in driver_Ie.title

# dir=os.path.dirname(__file__)
# chrome_driver_path=dir+"\chromedriver.exe"
# driver=webdriver.Chrome(chrome_driver_path)
# driver.get("http://www.python.org")
# assert "Python" in driver.title


# 1. 打开 www.python.org 页面，并通过断言判断是否成功打开对应页面；
# dir_one=os.path.dirname(__file__)
# chrome_driver_path_one=dir_one+"\chromedriver.exe"
# driver_one=webdriver.Chrome(chrome_driver_path_one)
# driver_one.get("http://python.org")
# assert "Python" in driver_one.title

# 2. 打开 www.yahoo.com 页面,进行页面判断，在搜索输入框中，输入seleniumhq 与回车键，进行搜索。         搜索按钮的id是uh-search-button
# dir_two=os.path.dirname(__file__)
# chrome_driver_path_two=dir_two+"\chromedriver.exe"
# driver_two=webdriver.Chrome(chrome_driver_path_two)
# driver_two.get("http://www.yahoo.com")
# assert "Yahoo" in driver_two.title
# elem = driver_two.find_element_by_name("p")
# elem.clear()
# elem.send_keys("seleniumhq")
# # elem.send_keys("seleniumhq"+Keys.RETURN)
# # elem.send_keys(Keys.ENTER)
# elem_search=driver_two.find_element_by_id("uh-search-button")
# elem_search.click()
# assert "ERR_CONNECTION_TIMED_OUT" in driver_two.page_source


# 3. 打开 www.baidu.com 页面，激活当前窗口，并输出百度首页已打开；通过 id 查找搜索框，键入 java 并提交搜索； 获取页面中“百度已为您找到
# 相关结果约 xxx 个”； 执行 js 脚本，显示一个框提示用户已经找到相关结果。
dir_three=os.path.dirname(__file__)
chrome_dir_path=dir_three+"\chromedriver.exe"
driver_three=webdriver.Chrome(chrome_dir_path)
driver_three.get("http://www.baidu.com")
if "百度" in driver_three.title:
    print("百度首页已打开")
elem = driver_three.find_element_by_id("kw")
elem.clear()
elem.send_keys("java"+Keys.ENTER)
current_url=driver_three.current_url
driver_three.get(current_url)
elem_result=driver_three.find_element_by_class_name("nums_text")
print(elem_result.text)
assert "百度为您找到相关结果" in driver_three.page_source


