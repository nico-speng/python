import urllib.request

# url = 'https://dianying.taobao.com/cityAction.json?city=&_ksTS=1680153964797_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true'
url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1680154709378_188&jsoncallback=jsonp189&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'cookie':'t=735123a09c4ec082677c07019efd8865; cna=0DmIHMD0ZWECAbc4mVsWSd16; cookie2=171030ef2161e03c0bfe04789982c68b; v=0; _tb_token_=5776873e5e6be; xlly_s=1; isg=BAQE9x_sPNKHXYg9fK2mHa9u1YL2HSiHs1D_7R6k6U-SSaYTRC0UFRSoieGR0WDf; tfstk=cUQlB7Ze_g-7BLzdhTT77BlYf9EAaUueIw7fuSpomRQHAWQkasXt0coSFSvuC8oC.; l=fBMufEEINjmfF0oKBO5alurza77tBIObzsPzaNbMiIEGa6td9F1s-NCsVVKXWdtjgT5qqexr24w81dHDJ5U_WFkDBeYQKtyuJXJwReM3N7AN.',
    'referer': 'https://dianying.taobao.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    
}
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]


try:
    with open('淘票票_jsonPath.json','w',encoding='utf-8') as fp:
        fp.write(content)
except Exception as e:
    print(f'爬取数据失败，{e}')

import json
import jsonpath

obj = json.load(open('淘票票_jsonPath.json','r',encoding='utf-8'))

city = jsonpath.jsonpath(obj, '$..regionName')
print(city)
