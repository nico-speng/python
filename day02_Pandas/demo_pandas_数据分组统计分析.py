import pandas as pd


'''
分组统计函数groupby的功能:
·根据给定的条件将数据拆分成组
·每个组可以独立应用函数（如sum())
·将结果合并到一个数据结构中

语法:
df.groupby(by=None,axis=O,as_index=True,sort=Ture)

分组计算:
·按照单列分组计算
·按照多列分组计算
·按照指定列分组计算

'''
pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_excel('电脑配置销售记录.xlsx')
print(df)

# 按照单列分组计算
print('\n------按照单列分组计算-------')
df1 = df[['产品名称','数量','标准单价']]
print(df1)
print(df1.groupby('产品名称').sum()) # 对数量，标准单价都进行求和统计

# 按照多列分组计算
print('\n------按照多列分组计算-------')
df1 = df[['产品名称','销售员','数量']]
print(df1)
print(df1.groupby(['销售员','数量']).sum())

# 按照指定列分组计算

