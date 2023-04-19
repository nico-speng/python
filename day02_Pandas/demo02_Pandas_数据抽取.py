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
df.rename(columns={'数学.上':'数学','英语.上':'英语','语文.上':'语文'},inplace=True)
print(df)

# 直接修改行索引名称
df.index=list('123')
print(df)

df.rename({'1':'张三','2':'李四','3':'王五'},inplace=True)
print(df)

# 修改一整行
df.loc['张三'] = [100,100,99]
print(df)
# 修改第0列的所有成绩
df.iloc[0,:] = [99,99,99]
print(df)
# 修改所有数学的成绩
df.loc[:,'数学'] = [100,87,99]
print(df)
# 修改整列数据
df.iloc[:,0] = 90
print(df)

# 修改某一处的成绩
df.loc['李四','语文'] = 69
print(df)

df.iloc[1,1] = 55
print(df)

# 删除数据

'''
参数说明:
labels:表示行标签或列标签
axis:axis=0表示按行删除 axis=1表示按列删除
index :删除行,默认值为None
columns:删除列，默认值为None
inplace:对原数组作出修改并返回一个新数组。默认值为False，如果值为True,那么原数组直接就将被替换
'''
# 删除列的数据
# df.drop(['数学'],axis=1,inplace=True)
# df.drop(columns='数学',axis=1,inplace=True)
df.drop(labels='数学',axis=1,inplace=True)
# print(df)

# 删除行的数据
# df.drop(['张三'],axis=0,inplace=True)
# df.drop(index='张三',axis=0,inplace=True)
df.drop(labels='张三',axis=0,inplace=True)
print(df)

# 带条件的删除，删除数学成绩小于60
print(df[df['英语']<60].index[0])
df.drop(df[df['英语']<60].index[0],inplace=True)
print(df)