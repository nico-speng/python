# 引入模块


import urllib.request

import urllib.parse

import json

next_page = 0
data_list = []

# 模拟浏览器向服务器发送请求
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',

}

while True:
    url = f'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start={next_page}&limit=20'
    
    # 将参数合成 后面通过urlopen发送请求
    request = urllib.request.Request(url=url,headers=headers)
    # 发送请求
    respose = urllib.request.urlopen(request)
    # 获取网页页面的数据
    content = json.loads(respose.read().decode('utf-8'))
    data_list.append(content)
    
    '''
    # 爬取所有数据
    if not content:
        with open('data.json','w',encoding='utf-8') as fp:
            fp.write(data_list)
        print(f'已爬取网页{len(data_list)}条数据')
        break
    '''
    # 爬取10页数据
    print(url)
    
    if next_page == 2 :
        
        try:
            with open('data.json','w',encoding='utf-8') as fp:
                fp.write(json.dumps(data_list))
                print(f'已爬取网页{len(data_list)}条数据')
                break    
        except Exception as e:
            print(f'导出失败: {e}')
            break
        
    next_page += 1