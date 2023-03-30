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
        # print(full_url)
        request = urllib.request.Request(url = full_url,headers=self.headers)
        return urllib.request.urlopen(request)
    
    def get_conten(self,response):
        return  response.read().decode('utf-8')
        # print(response)
    
    # Boss直聘_josnPath
    def down_load(self,content,filename):
        try:
            with open(f'{filename}.json','r','utf-8') as fp:
                fp.write(content)
            return 200
        except Exception as e:
            return 400,{e}

    def read_content(self,filename):
        obj = json.load(open(filename,'r','utf-8'))
        print(obj)

url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=爬虫&city=101280600&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30'
headers = {
    'cookie': 'lastCity=101280600; sid=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1680160707; __zp_seo_uuid__=75308d01-787d-49e8-99fd-1f07149503b3; __g=sem_pz_bdpc_dasou_title; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1680162158; __c=1680160707; __l=r=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.a00000jwxXBa_ucFgDScVEdBh9C2_nmCzxV-_LhKJIXIl-9jNCh5RoRpcSgTR01zHamN-eG7pBXV-iGwLOLmdiJkYwalBpuCWnZQzYYUt75NkubJoqZVcoKvdnofR6hUaOpiIZWchwj9Xtwo84e74bQkFeCHMKJPuDopJNTNJNQqKZ93_93-uJdn1Hl0EMEPSJddruDVgPwWB-1p6FFa1dyl6bQ7.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1Tqpkko60IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqmhq1Tqpkko60ThPv5H00IgF_gv-b5HDdPjf4PHTkrjR0UgNxpyfqnHRzn1mYnHc0UNqGujYknWDkrHRLr0KVIZK_gv-b5HDzrjcv0ZKvgv-b5H00pywW5R9rffKspyfqP0KWpyfqrHn0mLFW5HcvPHnd%26dt%3D1680160700%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26tpl%3Dtpl_12826_31784_0%26l%3D1544957185%26us%3DlinkVersion%253D1%2526compPath%253D10036.0-10032.0%2526label%253D%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkType%253D%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258ABOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525EF%2525BC%25258C&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E7%2588%25AC%25E8%2599%25AB%26city%3D101280600&s=3&g=%2Fwww.zhipin.com%2Fshenzhen%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0; __a=51335820.1680160707..1680160707.3.1.3.3; wd_guid=bb260833-f1ed-4ee0-b5f5-ec78d1e94257; historyState=state; _bl_uid=Fml4qfyhu6ttpa6hs3gdb64xnk0n; __zp_stoken__=f4e4eaRQMYSJUPXofNHg6LXB6IGoGDxk8TRx6XEs2IStRTyR3Ag0SH0cgeFRaOycGLWQ2dX0uBwhLCh1kJBQtLTEAYVYhLGV3MmBYKxAYNUdfA3IBLWMMHXYWJEAzA0FNb10EDgwOBQ0JOmE%3D',
    'referer': 'https://www.zhipin.com/web/geek/job?query=%E7%88%AC%E8%99%AB&city=101280600&page=1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

# 实例化对象
dataContent = dataList(headers)
# 获取输入的页码
next_page = int(input('请输入要获取的截止页码：'))
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
        'page':1,
        'pageSize':30
    }
    # 发送请求
    request = dataContent.create_Requst(url,values)
    # 获取内容
    response = dataContent.get_conten(request)
    print(response)