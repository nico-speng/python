

# 引入urllib的模块
import urllib.request
import urllib.parse

# 获取url地址
base_url = 'https://www.baidu.com/s?'

data = {
    'wd':'周杰伦',
    'sex':'男',
    'loction':'中国台湾省'
}

# 将参数转为二进制
new_data = urllib.parse.urlencode(data)

# 组成新的url地址
url = base_url + new_data

# 模仿浏览器向服务器发送请求
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 发送请求
response = urllib.request.urlopen(request) 

# 获取网页源码
content = response.read().decode('utf-8')
print(content)
