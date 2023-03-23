# 引入模块


import urllib.request

import urllib.parse


# 定制每页的请求对象
def create_request(page):
    
    # 模拟浏览器向服务器发送请求
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',

    }


    # 获取网页url
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&'



    # 定义url传递的参数
    data = {

        'start':(page-1)*20,

        'limit':20

    }

    # 参数进行编译
    new_data = urllib.parse.urlencode(data)

    # 拼接url地址
    url = base_url + new_data

    return urllib.request.Request(url=url,headers=headers)
    


# 获取网页数据
def jls_extract_def(response):
    
    return response.read().decode('utf-8')


def get_content(request):
    # 通过urlopen发送请求
    response = urllib.request.urlopen(request)

    # 读取网页数据
    return jls_extract_def(response)



# 下载数据
def down_load(content):
    
    try:

        with open(f'demo_{page}.json','w',encoding='utf-8') as fp:

            if len(content)!=0:
                
                fp.write(content)

                print('导出成功')

            else:
                print('导出失败')


    except Exception as e:

        print(f'导出网页数据失败：{e}')



# 页码的公式是：(页数-1)× 每页条数


# 程序自动调用


if __name__ == '__main__':

    start_page = int(input('请输入起始的页码：'))

    end_page = int(input('请输入结束的页码：'))    


    for page in range(start_page,end_page):

        # 定制每页的请求对象
        request = create_request(page)

        # 获取网页数据
        content = get_content(request)

        # 下载数据
        down_load(content)