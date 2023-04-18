import pandas as pd

data = [[45,65,200],[56,37,50],[67,82,141]]
index = ['张三','李四','王五']
columns = ['数学','英语','语文']

pd.set_option('display.unicode.east_asian_width',True)
df = pd.DataFrame(data=data,index=index,columns=columns)
print(df)

# 提取行数据
print(df.loc['张三'])   # 行索引名称

print(df.iloc[0])   # 行索引的编号

# 提取多行数据 （谁和谁）
print(df.loc[['张三','王五']])   # 行索引名称

print(df.iloc[[0,2]])   # 行索引名称

# 提取连续的多行数据（从谁到谁）
print(df.loc['张三':'王五'])  # 行索引名称，包含王五

print(df.iloc[:2])  # 行索引序号，含0 不含2

print('----------------------------')
print(df.loc[:,['数学','语文']]) # 逗号的左侧表示是行，右侧表示的是列
print(df.iloc[:,[0,1]])

print('---------提取连续的列---------')
print(df.loc[:,'英语':])
print(df.iloc[:,1:])


# 提取区域数据
print(df.loc['张三','数学'],type(df.loc['张三','数学']))
print(df.loc[['张三','王五'],['数学','语文']])

print(df.iloc[0,0])
print(df.iloc[0:1,0:1])

print('---------提取非连续的区域数据---------')
print(df.iloc[[0,2],[0,2]]) # 第0行和第2行，第0列和第2列
print(df.iloc[:,1]) 

print('-------提取指定条件数据---------')
print(df.loc[df['语文']>=60])   # 提取语文成绩大于60的学生信息
# 从个条件之间使用关系运算符
print(df.loc[(df['语文']>60) & (df['数学']>60)])

# 数据的增加、修改和删除
# 数据增加 - 按列增加
# 采用之间赋值的方式
df['政治'] = [90,80,89]
print(df)

# 使用loc属性在DataFrame的最后一列增加
df.loc[:,'化学']=[100,43,87]
print(df)

# 在指定的所有位置上插入一列
lst = [100,90,99]
df.insert(1,'历史',lst)
print(df)

# 按行增加
df.loc['陈柳'] = [69,87,91,19,54,78]
print(df)


# 修改操作
print('-------修改操作---------')

data = [[45,65,200],[56,37,50],[67,82,141]]
index = ['张三','李四','王五']
columns = ['数学','英语','语文']

pd.set_option('display.unicode.east_asian_width',True)
df = pd.DataFrame(data=data,index=index,columns=columns)

df.columns = ['数学.上','英语.上','语文.上']

print(df)