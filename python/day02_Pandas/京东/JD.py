# -*- coding:utf-8 -*-
import requests
import urllib
import time
import threading
import json
import pandas
import os
import re 
import jieba
import wordcloud
from PIL import Image
 
 
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" )
        get_information()
        print ("退出线程：" )
 
 
#找出字符串str中最多的字
def max_letter_count(str):
    count_max=0
    for i in str:
        if str.count(i)>count_max:
            max_char=i
            count_max = str.count(i)
    list=[]
    list.append(max_char)
    list.append(count_max)
    return list
 
 
def get_information(id,headers,start_page,end_page,result,reason):
    #目前整理的一些好评关键词
    GoodComment={'推荐','好用','满意','舒服','喜欢','买它','优惠','很值','赞','精美','回购','漂亮','好看','不错','新款','实惠','速度快','效果好','很舒适','很柔软','很合身','真好','继续买','非常好','很好','质量不错','挺好的','继续购买','特别好','蛮好','一直在用','非常满意','特别好看'}
    #输出每一页的评论
    for page in range(start_page,end_page):
        print("正在爬第"+str(page)+"页",end='')
        url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId='+id+'&score=0&sortType=5&page='+str(page)+'&pageSize=10&isShadowSku=0&fold=1'
        data=requests.get(url,headers=headers).content.decode('gbk')
        data=data[data.find('{'):data.rfind('}')+1]
        data=json.loads(data)
        #筛选出有用评论
        for num in data['comments']:
            #如果在某一个评论中某个字重复出现率高达30%，判断为买家的垃圾评论,不写入评论中
            if max_letter_count(num['content'])[1]/len(num['content'])>0.3:    #30%保证了评论字数不得低于4个
                reason.append({
                    "ID":str(num['id']),
                    "评论时间":num['creationTime'],
                    "评论内容":num['content'],
                    "理由":max_letter_count(num['content'])[0]+"重复出现率高达30%"
                    })
            else:
                GoodCommentNum=0
                for Comment in GoodComment:               #如果评论中出现好评关键字，记录加1
                    if Comment in num['content']:
                        GoodCommentNum=GoodCommentNum+1
                        if GoodCommentNum>5:              #如果好评数量大于5，判断为虚假评论
                            reason.append({
                            "ID":str(num['id']),
                            "评论时间":num['creationTime'],
                            "评论内容":num['content'],
                            "理由":"好评过多"
                            })                                
                if len(num['content'])<30:                    #评论字数少于30字
                    if GoodCommentNum<=10 and GoodCommentNum/len(num['content'])<=2/10:    #如果每10字评论有好评关键字小于2,存入评论
                        result.append({
                        "ID":str(num['id']),
                        "评论时间":num['creationTime'],
                        "评论内容":num['content']
                        })
                    else:
                        reason.append({
                        "ID":str(num['id']),
                        "评论时间":num['creationTime'],
                        "评论内容":num['content'],
                        "理由":"好评过多"
                        })
                else:                                         #评论字数大于30字
                    if max_letter_count(num['content'])[1]/len(num['content'])>0.2:
                        reason.append({
                            "ID":str(num['id']),
                            "评论时间":num['creationTime'],
                            "评论内容":num['content'],
                            "理由":max_letter_count(num['content'])[0]+"重复出现率高达20%"
                            })
                    else:
                        if GoodCommentNum<=10 and GoodCommentNum/len(num['content'])<1/10:    #如果每10字评论有好评关键字小于1,存入评论
                            result.append({
                            "ID":str(num['id']),
                            "评论时间":num['creationTime'],
                            "评论内容":num['content']
                            })
                        else:
                            reason.append({
                            "ID":str(num['id']),
                            "评论时间":num['creationTime'],
                            "评论内容":num['content'],
                            "理由":"好评过多"
                            })
        print("\n爬完第"+str(page)+"页")
 
 
def cloud_word(comment_word,name):      #生成词云
    stopwords = [line.strip() for line in open('stop_words.txt', encoding='UTF-8').readlines()]    #加载停用词表
    comment_word=comment_word.encode('utf-8')
    comment_word=jieba.cut(comment_word)     #未去掉停用词的分词结果
    comment_word_spite = []
    for word in comment_word:                #去掉停分词
        if word not in stopwords:
            comment_word_spite.append(word)
    comment_word_spite=' '.join(comment_word_spite)
    wc=wordcloud.WordCloud(           #创建wordcloud对象
        r'msyh.ttc',width=500,height=500,
        background_color='white',font_step=2,
        random_state=False,prefer_horizontal=0.9
        )
    t=wc.generate(comment_word_spite)
    t.to_image().save(name+'.png')
 
 
 
def main():
    #浏览器访问伪装
    headers={
             'cookie':'unpl=JF8EALpnNSttXE0GBU4ATxMZSl1SW1RdSkQCPWIGXVpdT11VSVISRxV7XlVdXxRKFR9vZhRUXFNKUA4eASsSEHtdVV9cCE0VA2tvNWRdWUpUBBwLGBsSe15Ublw4SxAFZmIFVlVdTF0MEgIfEBZIWF1ZWw57FjNvbwJkXltJXA0cBhgTE0ttZF9tCEoXAmdXBV1bUU5RBBgGHCJRJVtRWFwJSloDaGEMUV1aQ1ECEgsSEhRJW1dbVA9NETNuVwY; __jdv=123|tophub.today|t_1000173159_|jingfen|57c1d3e0801748d0b0c4286458aca8d4|1678413949703; shshshfpa=3308a17c-6ff0-fd05-ea7d-ef412a953d60-1678413958; shshshfpx=3308a17c-6ff0-fd05-ea7d-ef412a953d60-1678413958; shshshfpb=jJTjy0Uhj4W4jW-4oy0LFtw; __jdu=16784139468881537248677; TrackID=1JCcdckgwQ-3MFxoCv-pgweUNgScoWcHzxlz7wGnfhetwX_-fStIUsvwVlqCm8eE8sflBjSVumtrSCtrBdOZGYFdHvo_iwm2WY430bgmxvbQ; pinId=XGlvmJe0JABzYc34QxmXpLV9-x-f3wj7; pin=jd_6c3dfcab9abfe; unick=u_3qvvk7xdebvf; ceshi3.com=103; _tp=yChC7wnJDqSHo/HszcmntJPvmQZLRRTSQkJTQMGlzMI=; _pst=jd_6c3dfcab9abfe; areaId=19; ipLoc-djd=19-1607-4773-62121; jwotest_product=99; user-key=f76be44c-e121-4ea4-b8ac-a4eb399fc623; cn=13; PCSYCityID=CN_440000_440300_0; __jdc=122270672; shshshfp=f702d8175d492445b22500b9cd4fa016; JSESSIONID=D1F83906E1537222187C5759D97D9B8D.s1; __jda=122270672.16784139468881537248677.1678413946.1678431451.1678438534.5; jsavif=1; 3AB9D23F7A4B3C9B=F34NLHL2MS2N3NAQJW34IR7YNXHXHL3AS4GG6PWEFCVQ2NB4WYPQPJ325562CUTIVWNIKTVZSA7L57A4TGJHFMJH6Q; token=3bb9113f3b87914587d8703d2d8c1352,3,932465; __tk=b83378894770ab0e53d3cb80c0f7b0b0,3,932465; RT="z=1&dm=jd.com&si=ich70irlduh&ss=lf2ayspv&sl=2&tt=0&obo=2"; shshshsID=a7a89fb3034130d0efe633cd0386deb0_3_1678438653972; __jdb=122270672.3.16784139468881537248677|5.1678438534; thor=A646B59BA648DF4A955DB2839141B9D9E2715A2F2BB88AA84DD53F96117A94DA5A44633EB3597A6001840B00CE58EFC714670C41835FD06C046B76C74C3AB0BE67EBBBDAB15CF7CEF650CFCDD1E3485906F7C7F979F00363640376F6A231083DEDA3D06A1BE7BF611B403B963FF84256EE69E309B2D5B7BA7BE0032B426AEF1CC5770865A15571D87281926FB19702E73AC444E9A8096290D1BB8343DAA5A246',
             'referer':'https://item.jd.com/',
             'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            }
    url_input=input("请输入京东商品网址：")
    try:
        result=[]    #筛选过后的评论
        reason=[]    #统计每个被筛选淘汰的评论的淘汰理由
        id=''.join(re.findall(r'com/(.*?)\.html',url_input))
        url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId='+str(id)+'&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
        
        data=requests.get(url,headers=headers).content.decode('gbk')

        if len(data) ==0 :
            print("反爬了:",url)
            return
        
        
        data=data[data.find('{'):data.rfind('}')+1]
      
        data=json.loads(data)
        lastpage=data['maxPage']
        print('共有'+str(lastpage)+'页评论')
        threads=[]
        threads.append(threading.Thread(target=get_information,args=(id,headers,0,lastpage//2,result,reason)))
        threads.append(threading.Thread(target=get_information,args=(id,headers,lastpage//2,lastpage,result,reason)))
        # 开启新线程
        for t in threads:
            t.start()
        # 等待所有线程完成
        for t in threads:
            t.join()
        print ("退出主线程")
    except Exception as e:
        # 访问异常的错误编号和详细信息
        print(e)
        print(str(e))
        print("提取商品网址信息出错，请重新输入京东商品网址：")
        main()
    # 创建新线程,分2个线程（太少了速度慢，太快了容易被封）
    #将筛选后的评论装入文件
    print("有效评论已装入NEW评论.xlsx文件")
    print("淘汰评论已装入淘汰评论.xlsx文件")
    NEW=pandas.DataFrame(result)
    NEW.to_excel('NEW评论.xlsx')
    Eliminate=pandas.DataFrame(reason)
    Eliminate.to_excel('淘汰评论.xlsx')
    comment_word=''
    for _comment in result:
        comment_word+=_comment["评论内容"]
    all_word=comment_word
    cloud_word(comment_word,'comment_word')
    print("comment云图制作完成")
    for _comment in reason:
        all_word+=_comment["评论内容"]
    cloud_word(all_word,'all_word')
    print("all_comment云图制作完成")
 
if __name__=='__main__':
    main()