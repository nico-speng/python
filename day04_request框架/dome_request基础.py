import requests


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

# post请求