import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("./chromedriver.exe")
try:
    driver.implicitly_wait(5)
    driver.get("https://www.lagou.com/zhaopin/Java/?filterOption=3")
    driver.switch_to.window(driver.current_window_handle)
    while True:
        # driver.implicitly_wait(3)
        driver.maximize_window()
        print("* * * * * 第",driver.find_element_by_css_selector('.pager_is_current').text,"页 * * * * *")
        position_list = driver.find_elements_by_css_selector(".p_top a h3")         #.position_link h3
        money_list = driver.find_elements_by_css_selector(".money")
        company_list = driver.find_elements_by_css_selector(".company_name")
        num = 0
        while num<3:
            print("职位：", position_list[num].text, "，薪资：", money_list[num].text, "，公司名称：", company_list[num].text)
            position_list[num].click()
            windows_list = driver.window_handles
            driver.switch_to.window(windows_list[1])
            experience = driver.find_element_by_css_selector(".job_request p span:nth-child(3)")
            print("工作经验：", experience.text,"\n")
            driver.close()
            driver.switch_to.window(windows_list[0])
            num+=1
        element_next=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.page_no:last-of-type')))
        if "下一页" in driver.find_element_by_css_selector('.pager_container').text:
            driver.find_element_by_link_text('下一页').click()
        else:
            driver.quit()
finally:
    driver.quit()

# element = WebDriverWait(driver, 5).until( ec.element_to_be_clickable((By.CSS_SELECTOR, '.mnav')))