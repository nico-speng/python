import requests
from bs4 import BeautifulSoup

'''
# request 基本使用：

    # 发送请求
    r = requests.get('https://www.baidu.com')
    # 返回response类型
    print(r)    # <Response [200]>
    # 设置编码格式
    r.encoding = 'utf-8'
    # 获取网页源码
    c = r.text
    print(c)
    # 返回状态码
    print(r.status_code)
    # 返回响应头
    print(r.headers)

'''
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

# 发送请求
response = requests.get(url,headers)
# 获取网页源码
content = response.text
# print(content)

# 通过bs4获取标签属性   __VIEWSTATE     __VIEWSTATEGENERATOR
soup = BeautifulSoup(content,'lxml')

viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = f'https://so.gushiwen.cn/{code}'


# 获取验证码
session = requests.session()
requests_code = session.get(code_url)
# 注意此时要使用二进制，因为我们要使用的是图片的下载
content_code = requests_code.content

# wb的模式就是将二进制数据写入文件
with open('code.jpg','wb') as fp:
    fp.write(content_code)

code_name = input('请输入验证码：')


# post请求
purl = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

data_post = {
    '__VIEWSTATE':viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '1946445144@qq.com',
    'pwd': 'action',
    'code': code_name,
    'denglu': '登录',
}

request_post = session.post(url=purl,data=data_post)
content_post = request_post.text

with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content_post)
