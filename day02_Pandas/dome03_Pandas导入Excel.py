'''
    导入.xls或.xlsx文件
    语法：pd.read_excel(io,sheet_name,header)
    常用参数说明：
    io：表示.xls或.xlsx文件路径或类文件对象
    sheet_name：表示工作表
    header：默认值为0，取第一行的值为列名，数据为除列以外的数据，如果数据不包含列名，则设置header=None
    usecols：指定某列的数据，可多指定几条，单个以[x]，例如：usecols=[1]
    多个以表格中具体的列名获取数据，例如：usecols=['ID','评论内容']
'''

import pandas as pd

# 导入Excel数据
print('导入Excel数据：')
df = pd.read_excel('comment.xlsx')
print(df)
print('\n')

print('导入指定的工作表Excel数据：')
df = pd.read_excel('comment.xlsx',sheet_name='Sheet2')
print(df)
print('\n')

# 导入一列数据
print('导入一列数据：')
df = pd.read_excel('comment.xlsx',usecols=[2])
print(df)
print('\n')
df = pd.read_excel('comment.xlsx',usecols=['ID','评论内容'])
print(df)
