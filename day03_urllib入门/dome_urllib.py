'''
    使用urllib来获取百度首页的源码
    一个类型：HTTPResponse
    六个方法：read、readline、readlines、getcode、getrul、getheaders
    
'''

import urllib.request

# 定义一个url地址，就是你要访问的地址
url_page =  'http://www.baidu.com'

# 模拟浏览器想服务器发送请求
response = urllib.request.urlopen(url_page)

# 返回的是HTTPrespose类型数据
print(response)
print(type(response))

# 获取响应中页面的源码
# read方法    返回的字节形式的二进制数据    按照一个字节一个字节的去读
# 我们要将二进制的数据转为字符串
# 二进制 => 字符串 设置字符串编码格式
conten = response.read().decode('utf-8')
# print(conten)

conten = response.readline().decode('utf-8')
print(conten)

conten = response.readlines()
print(conten)

# 返回状态码 200代表成功
print(response.getcode())

# 返回URL地址
print(response.geturl())

# 返回一个状态信息
print(response.getheaders())
