'''

作业:
1.股票信息提取(http://quote.stockstar.com/)
2.boos直聘
3.中华英才
4.汽车之家

'''

import urllib.request
import json
import jsonpath

class dataList:
        
    def __init__(self,headers):
        self.headers = headers
    
    def create_Requst(self,url,values):
         # 合并参数到 url
        full_url = f'{url}?{urllib.parse.urlencode(values)}'
        request = urllib.request.Request(url = full_url,headers=self.headers)
        return urllib.request.urlopen(request)
    
    def get_conten(self,response):
        # print(response)
        content = json.loads(response.read().decode('utf-8'))
        # content = content.get('zpData')
        # .split('}')[0]
        return content

    
    # Boss直聘_josnPath
    def down_load(self, content, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as fp:
                fp.write(content)
            return 200
        except Exception as e:
            return 400, str(e)

    def read_content(self,filename):
        obj = json.load(open(filename,'r',encoding='utf-8'))
        # content = obj.
        # print(jobList)

url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E7%88%AC%E8%99%AB&city=101280600&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30'
headers = {
 "Accept": "application/json, text/plain, */*",
 "Accept-Language": "zh-CN,zh;q=0.9",
 "Connection": "keep-alive",
 "Cookie": "lastCity=101280600; wd_guid=5084ba55-4218-4b66-b5ad-c203f36f5a68; historyState=state; _bl_uid=ygl7nfghvLF6aR4Cj0Xsd4kgddm5; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1680183889,1680186373; __fid=47b786a59be3772e713196e1fbe289f9; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1680186403; __c=1680186373; __l=l=/www.zhipin.com/web/geek/job?query=%E7%88%AC%E8%99%AB&city=101280600&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __a=20938534.1680183889.1680183889.1680186373.7.2.4.7; __zp_stoken__=f4e4eaUsabDwrOX9QaAcFG009MSZfIWkfRn4KKDslA0R4fQgKchIaGEcBbghoIH8GLWQ2dX0udQdLIB1kKGR7MxM7cHYtdkpPXAV5KxAYNUdfA3JZNlFQC1cWI0gsc0FNb10EDgwOBQ0JOmE=",
 "Referer":"https://www.zhipin.com/web/geek/job?query=%E7%88%AC%E8%99%AB&city=101280600",
 "Sec-Fetch-Dest": "empty",
 "Sec-Fetch-Mode": "cors",
 "Sec-Fetch-Site": "same-origin",
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
 "X-Requested-With": "XMLHttpRequest",
 "sec-ch-ua-mobile": "0",
 "sec-ch-ua-platform": "Windows"
}

# 实例化对象
dataContent = dataList(headers)
# 获取输入的页码
next_page = int(input('请输入要获取的截止页码：'))
file_name = 'Boss直聘_jsonPath.json'
url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?'
for page in range(1,next_page+1):
    values = {
        'scene':'1',
        'city':'101280600',
        'experience':'',
        'payType':'',
        'partTime':'',
        'degree':'',
        'industry':'',
        'scale':'',
        'stage':'',
        'position':'',
        'jobType':'',
        'salary':'',
        'multiBusinessDistrict':'',
        'multiSubway':'',
        'page':page,
        'pageSize':30
    }
    # 发送请求
    request = dataContent.create_Requst(url,values)
    # 获取内容
    content = dataContent.get_conten(request)
    print(content)
    # 将数据保持到本地
    # down_load = dataContent.down_load(content,file_name)
# text = dataContent.read_content(file_name)
    