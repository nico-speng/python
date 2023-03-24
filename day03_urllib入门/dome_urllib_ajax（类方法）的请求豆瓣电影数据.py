# 引入模块

import urllib.request


import urllib.parse


import json


class MovieData:
    data_list = []

    # 定义初始化变量

    def __init__(self,headers):

        self.headers = headers

    
    def create_request(self,url,values):
         # 合并参数到 url
        full_url = f'{url}?{urllib.parse.urlencode(values)}'
        print(full_url)
        # 发送请求
        request = urllib.request.Request(url=full_url, headers=self.headers)
        response = urllib.request.urlopen(request)
        data = self.jls_extract_def(response)
        return self.down_content(data)
    

    # 获取网页数据

    def jls_extract_def(self,response):

        content = response.read().decode()
        self.data_list.append(content)
        return self.data_list
    

    # 下载数据

    def down_content(self,content):
        try:
            # 将列表中的数据合并为一个字符串
            json_data = ''.join(content)
            print(type(content))
            # 将字符串解析为 JSON 对象
            data = json.loads(json_data)
            with open('data.json', 'w', encoding='utf-8') as fp:
                # 将数据写入到 JSON 文件中
                json.dump(data, fp, ensure_ascii=False, indent=2)
                return True, 200
        except Exception as e:
            return False, 400, e
    
    

# 模拟浏览器向服务器发送请求

headers = {


    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',

}

# 实例化类

movie = MovieData(headers)

# 获取输入的页码

next_page = int(input('请输入要获取的截止页码：'))

url = 'https://movie.douban.com/j/chart/top_list'

for i in range(1,next_page+1):
    values = {
        'type':'5',
        'interval_id':'100:90',
        'action':'',
        'start': i-1,
        'limit':20  
    }

    content = movie.create_request(url,values)
    print(content)
    
    if 200 in content:
        print(f'第{i}页数据已导出成功')
    else:
        print(f'导出失败，失败原因\n{content}') 
        break