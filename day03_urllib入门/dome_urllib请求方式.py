import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

# 请求对象的定制，为了解决反爬的第第一种手段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


# 将搜索的参数变成unicode编码的格式
# 我们需要依赖urllib.parse.quote(参数)
# name = urllib.parse.quote('周杰伦')
# url += name

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

# 使用urllib.parse.quote将参数编码转换为unicode
new_data = urllib.parse.quote(str(data))

url = base_url + new_data

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
