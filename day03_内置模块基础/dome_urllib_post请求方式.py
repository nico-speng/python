# 引入urllib的模块
import urllib.request
import urllib.parse
import json

# 获取url地址
url = 'https://fanyi.baidu.com/sug'

data = {
    'kw':'spider'
}

# post请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 模拟浏览器向服务器发送请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

# 定制化请求
# 注意：post的请求参数 是不会拼接在url的后面 而是需要放在请求对象定制的参数中
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
# 将str转换成json
content = json.loads(response.read().decode('utf-8'))
print(content)