import urllib.request
from lxml import etree

# 请求对象的定制
# 获取网页源码
# 下载

# 需求 下载的前十页的图片
# https://sc.chinaz.com/tupian/index.html
# https://sc.chinaz.com/tupian/index_2.html

# https://scpic1.chinaz.net/files/default/imgs/2023-03-24/51c2665b1f604a73_s.jpg
# https://scpic.chinaz.net/files/default/imgs/2023-03-27/3d1d11b9996860fa_s.jpg

# 请求对象的定制
def create_request(page):
    if page >=2:
        url = f'https://sc.chinaz.com/tupian/index_{str(page)}.html'
    else:  
        url = 'https://sc.chinaz.com/tupian/index.html'
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    return urllib.request.Request(url=url,headers=headers)
    
def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')

def down_load(content):
    
    try:        
        # 下载图片
        # urllib.request.urlretrieve('图片地址','文件的名字')
        # 解析网页属性
        html_tree = etree.HTML(content)

        name_list = html_tree.xpath('//img/@alt')
        # 一般涉及到图片的页面都会遇到懒加载
        img_tags = html_tree.xpath('//img/@data-original')

        for i in range(len(name_list)):
            name = name_list[i]
            src = img_tags[i]
            url = f'https:{src}'
            urllib.request.urlretrieve(url=url,filename=f'./img/{name}.jpg')
            
        print('导出成功: 200')
        
    except Exception as e:
        print(f'导出失败: {e}')
     
    

if __name__ == '__main__':
    start_page = int(input('请输入起始的页码：'))
    end_page = int(input('请输入起始的页码：'))
    
    for page in range(start_page,end_page+1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(content)
    