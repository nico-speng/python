'''
爬取天气信息并分析：爬取某个城市未来一周的天气信息，分析每天的最高温度、最低温度、平均温度等指标，并绘制相应的图表。

爬取股票信息并分析：爬取某只股票的历史K线数据，分析每天的开盘价、收盘价、最高价、最低价等指标，并绘制相应的图表。

爬取新闻信息并分析：爬取某个新闻网站的新闻信息，分析新闻的关键词、情感倾向等指标，并对新闻进行聚类分析。

爬取电影信息并分析：爬取某个电影网站的电影信息，分析电影的评分、票房、类型等指标，并绘制相应的图表。

爬取社交网络信息并分析：爬取某个社交网络平台的用户信息和关系信息，分析用户之间的社交网络结构、关系强度等指标，并绘制相应的图表。

'''

import requests

# 获取URL地址
url = 'http://lishi.tianqi.com/'

# 发送请求
re = requests.get(url)
print(re)