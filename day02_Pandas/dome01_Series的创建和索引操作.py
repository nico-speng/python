import pandas as pd

'''' 
    Series(data,index,dtype,name,copy)
    data：一组数据（ndarray 类型）
    index：数据索引标签，如果不知道，默认从0开始
    dtype：数据类型，默认会自己判断
    name：设置名称
    copy：拷贝数据，默认为false
    
    
'''

# Series对象创建
data = ['90','87','71']
index = ['make','nico','stm']
print('Series对象创建语法:' )
df = pd.Series(data=data,index=index)
print(df)
print('\n')

# 列表多个值获取的语法
print('列表多个值获取的语法:' )
print(df[['make','stm']])
print('\n')

# 切片索引的语法
print('切片索引的语法:' )
print(df['make':'stm'])
print('\n')

# 位置索引语法 去尾留头
print('位置索引语法:')
print(df[0:2:1])

# 获取对象的索引  返回的是DataFrame对象
print('获取对象的索引')
print(df.index)
print('\n')

# 通过list可将索引转化成列表
print('list将索引转变成列表')
print(list(df.index))

# 获取索引的值  
# 返回结果：['90' '87' '71']  
# 注意：列表数据是以","进行分隔。
print('获取索引的值')
print(df.values)
print('\n')

# 获取数据值的类型
# class 'numpy.ndarray'
print(type(df.values))
