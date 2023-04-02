'''

作业:

今日头条

'''

import urllib.request
import json
import jsonpath

class dataList:
        
    def __init__(self,headers):
        self.headers = headers
    
    def create_Requst(self,url):
        request = urllib.request.Request(url = url,headers=self.headers)
        return urllib.request.urlopen(request)
    
    def get_conten(self,response):
        return  response.read().decode('utf-8')
        # print(response)
    
    # Boss直聘_josnPath
    def down_load(self,content,filename):
        
        try:
            with open(filename,'w',encoding='utf-8') as fp:
                fp.write(content)
            return 200
        except Exception as e:
            return 400,{e}

    def read_content(self,filename):
        obj = json.load(open(filename,'r',encoding='utf-8'))
        return obj['data']

url = 'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398996&max_behot_time=1680228169&category=pc_profile_channel&client_extra_params={"short_video_item":"filter"}'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

# 实例化对象
dataContent = dataList(headers)
file_name = '今日头条数据.json'
# 发送请求
request = dataContent.create_Requst(url)
# 获取内容
json_str = dataContent.get_conten(request)
# 下载数据
# content = dataContent.down_load(json_str,file_name)
# 读取下载到本地的json数据，通过jsonpath解析
feedText = dataContent.read_content(file_name)
title = jsonpath.jsonpath(feedText, '$..title')
media_name = jsonpath.jsonpath(feedText, '$..media_name')

print(title)
print(media_name)
    