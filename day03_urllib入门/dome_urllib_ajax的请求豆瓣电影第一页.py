import urllib.request
import urllib.parse
import json

# 获取url地址
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'

headers = {
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 获取响应数据
response = urllib.request.urlopen(request)

# 将str转换成json
content = response.read().decode('utf-8')

# 数据下载到本地
# 方式一：
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)

# 方式二：
try:
    with open('douban.json', 'w', encoding='utf-8') as fp:
        if len(content) != 0:
            res = fp.write(content)
            print('导出成功')
        else:
            print('导出失败')
except Exception as e:
    print(f'导出失败: {e}')