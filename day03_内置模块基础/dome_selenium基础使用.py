# sourcery skip: avoid-builtin-shadow
from selenium import webdriver
from selenium.webdriver.common.by import By

path = '\day03_内置模块基础\chrome\chromedriver.exe'

browser = webdriver.Chrome(path)

# 元素定位
url = 'https://www.baidu.com'
browser.get(url)

import time
time.sleep(2)

inputs = browser.find_element(By.ID, 'kw')

# 获取文本框的对象
inputs.send_keys('周杰伦')
time.sleep(2)

# 获取百度一下的按钮
button = browser.find_element(By.ID, 'su')

# 点击按钮
button.click()
time.sleep(2)


# 滑到底部
js_button = "document.documentElement.scrollTop=100000"
browser.execute_script(js_button)
time.sleep(2)

# 获取下一页的按钮
next = browser.find_element(By.XPATH,'//a[class="n"]')

# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
browser.forward()

time.sleep(3)

browser.quit()
