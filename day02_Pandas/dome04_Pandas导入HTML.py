'''
    导入cvs文件的语法：
    pd.read_csv(filepath_or_buffer,sep='\t',header,encoding=None)
    filepath_or_buffer:代表文件目录
    sep:字符串、分隔符
    heade:默认值为0，取第一行的值为列名，数据为除列以外的数据，如果数据不包含列名，则设置header=None
    encoding:字符串，默认为None，文件的编码格式
    
    
    导入HTML的语法：
    pr.read_html(io,match='.+',flavor,header,encoding)
    io:字符串、文件路径、可以是URL链接，网址不接受HTTPS
    match:正则表达式
    flavor:解释器默认为'.xml'
    header:指定列标题所在的行
    encoding:文件的编码格式

'''

import pandas as pd

# 导入csv数据
pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_csv('csv数据.csv',sep=',',encoding='gbk')
print(df)
print('\n')


# 导入HTML数据
url = 'http://www.espn.com/nba/salaries'
# 创建一个空的DataFrame数据
df = pd.DataFrame()
df = df.append(pd.read_html(url))
print(df)
print('\n')