import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

try:
    with webdriver.Chrome(options=chrome_options) as browser:
        url = 'https://www.baidu.com'
        browser.get(url)
        browser.save_screenshot(os.path.join(os.getcwd(), 'baidu.png'))
        
        time.sleep(2)
        inputs = browser.find_element(By.ID, 'kw')
        # 获取文本框的对象
        inputs.send_keys('周杰伦')
        
        time.sleep(2)
        # browser.save_screenshot(os.path.join(os.getcwd(), 'zhoujie.png'))
        
        # selenium框架 没整明白
        
        
except Exception as e:
    print(e)