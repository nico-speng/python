import pandas as pd
'''
Pandas索引的作用:
·更方便地查询数据
·使用索引可以提升查询性能
·如果索引是唯一的, Pandas会使用哈希表优化
·如果索引不是唯一，但是有序，Pandas分使用二分查找算法·如果索引是完全随机的，那么每次查询都要扫描数据表
重新设置索引:
df.reindex(labels=None,index=None,column=None,axis=None,method=None,fill_value=nan)
·设置某列为行索引
 df.set_index()
·数据清洗后重新设置连续索引
df.reset_index()

'''


S1 = pd.Series([10,8,22],index=['a','b','c'])
S2 = pd.Series([5,8,10],index=['a','b','c'])
print(S1+S2)

S = pd.Series([5,8,10])

# 使用0进行填充
print(S.reindex(range(5),fill_value=0))

# 向前填充和向后填充
print(S.reindex(range(5),method='ffill'))
print(S.reindex(range(5),method='bfill')) # 向后填充没有数值则为NaN


pd.set_option('display.unicode.east_asian.width',True)
data = [[61,78,83],[89,48,81],[49,57,69]]
index = ['msb1001','msb1002','msb1003']
columns = ['数学','语文','英语']
df = pd.DataFrame(data=data,index=index,columns=columns)
print(df)

# 重新设置行索引
print(df.reindex(['msb1001','msb1002','msb1003','msb1004','msb1005']))

# 重新设置列索引
print(df.reindex(columns=['数学','语文','英语','历史','化学']))

index = ['msb1001','msb1002','msb1003','msb1004','msb1005','msb1006']
columns = ['数学','语文','英语','历史','化学','物理']
print(df.reindex(index=index,columns=columns))

# 设置某列为行索引
df = pd.read_excel('msb课程记录.xlsx')
# df = df.set_index(['买家会员名'])
print(df)

# 数据清洗后重新设置连续索引
df = df.dropna().reset_index(drop=True)
print(df)