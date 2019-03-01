import time,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
dir=os.path.dirname(__file__)
dir_chrome_driver=dir+"\chromedriver.exe"
driver=webdriver.Chrome(dir_chrome_driver)
driver.implicitly_wait(5)
driver.get("https://www.qiushibaike.com/text")
# 输出页面内容的函数
def output():
    author_list=driver.find_elements_by_css_selector(".author h2")
    content_list=driver.find_elements_by_css_selector(".content")
    smile_list=driver.find_elements_by_css_selector(".stats-vote .number")
    for i in range(0,len(author_list)):
        print("第",i+1,"条：\n作者：",author_list[i].text,"\n笑话内容：",content_list[i].text,"\n好笑数：",smile_list[i].text,"\n")

while(1):
    print("* * * * * * * * * * * * * * * * * * * *第",driver.find_element_by_css_selector(".pagination .current").text,"页* * * * * * * * * * * * * * * * * * * *\n")
    output()
    if "下一页" in driver.find_element_by_css_selector(".pagination").text:
        driver.find_element_by_css_selector(".next").click()
    else:
        driver.quit()
        quit()

