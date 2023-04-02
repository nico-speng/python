from lxml import etree
import urllib.request

# xpath解析:

# ①本地文件
# ②服务器响应的数据 response.read().decode('utf-8')
html_etree = etree.parse('xpath.html')
# print(html_etree)

# 获取标签中有id属性的li标签
# text()获取标签中的内容
li_list = html_etree.xpath('//body/ul/li[@id]/text()')
print(li_list)
print(len(li_list))

# 找到id为l1的li标签  注意引号问题
li_list = html_etree.xpath('//ul/li[@id="l1"]/text()')
print(li_list)
print(len(li_list))

# 查找到id为l1的li标签的class的属性
li_list = html_etree.xpath('//ul/li[@id="l1"]/@class')
print(li_list)
print(len(li_list))

# 查询id中包含l的li标签 模糊查询
li_list = html_etree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list)
print(len(li_list))

# 查询id的值以l开头的li标签     模糊查询
li_list = html_etree.xpath('//ul/li[starts-with(@id,"l")]/text()')
print(li_list)
print(len(li_list))

# 查询id为l1 class为clas01的li标签      逻辑查询 
li_list = html_etree.xpath('//ul/li[@id="l1" and @class="cls01"]/text()')
print(li_list)
print(len(li_list))

url = 'https://www.baidu.com/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode('utf-8')
# print(content)

# 解析网页源码
tree = etree.HTML(content)
# xpath 返回的都是list类型数据
list_title = tree.xpath('//body//input[@id="su"]/@value')
print(list_title)