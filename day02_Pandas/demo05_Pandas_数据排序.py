# sourcery skip: replace-apply-with-numpy-operation
import pandas as pd

# 数据排序和排名
'''
DataFrame排序时主要使用sort_values()方法
语法：
df.sort_values(by,axis=0,ascending=True,inplace=False,kind='quicksort ,na_position='last,ignore_index=False)
'''
pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_excel('电脑配置销售记录.xlsx')
S1 = df.sort_values(by='成交金额',ascending=False) # 降序排序，ascending 默认为升序
print(S1.head())

# 根据多列进行排序，数量和成交金额  数量相同的时候 成交金额采用的是降序排序
S2 = df.sort_values(by=['数量','成交金额'],ascending=False) 
print(S2)

# 按数量排序
S3 = df.sort_values(by='数量',ascending=False)
# S3['顺序排名'] = S3['数量'].rank(ascending=False) # 默认采用顺序排名的平均值
S3['顺序排名'] = S3['数量'].rank(method='min',ascending=False) # 默认采用最小值排名的平均值
print(S3)

# 数据计算
'''
sum([axis,skipna])
求和:axis=1表示按行加，axis=0表示按列加，默认列加 skipna=1表示将NaN转0，skipna=0表示不转

求平均值 mean([axis,skipna])
求最大值 max([axis,skipna])
求最小值 min([axis,skipna])

median(axis=None,skipna=None)
中位数:axis=1表示行，axis=0表示列，默认为None skipna布尔值，表示计算结果是否排除了NaN/Null,默认为True

mode(axis=0,dropna=True)
求众数:axis=1表示行，axis=0表示列，默认为0  dropna是否删除缺失值，布尔型，默认为True

求方差  var(axis=None,skipna=None)
标准差  std(axis=None,skipna=None)

quantile(q=0.5,axis=0,numeric_only=True)
分位差:numeric_only的值为False 将计算日期、时间和时间增量数据的分位数

'''

data = [[100,80,100],[78,86,78],[75,85,85]]
columns = ['数学','语文','英语']
df = pd.DataFrame(data=data,columns=columns,index=[1,2,3])
print(df)

print('---------求和----------')
df['学生'] = ['张三','王五','李四']
df['行-总成绩'] = df.sum(axis=1) # 按行相加
print(df)

print('---------求平均值----------')
S1 = df.append(df.mean(),ignore_index=True)    # 默认按照列计算平均值
print(S1)

print('---------求最大值----------')
S1 = df.append(df.max(),ignore_index=True)    
print(S1)

print('---------求最小值----------')
S1 = df.append(df.min(),ignore_index=True)    
print(S1)

print('---------求中位数----------')
S1 = df.append(df.median(),ignore_index=True)    
print(S1)

print('---------求众位数----------')  
data = [[100,90,100],[100,78,78],[78,90,78]]
columns = ['数学','语文','英语']
df = pd.DataFrame(data=data,columns=columns,index=[0,1,2])
print(df)
print(df.mode())
# 按行的众数
print(df.mode(axis=1))
print('---------求数学的众数----------')  
# 数学的众数
print(df['数学'].mode())

print('---------求方差----------')  
data = [[135,140,138,145,140],[140,145,139,142,132]]
index = ['李凡','郭曙光']
columns = ['一模','二模','三模','四模','五模']
df = pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print(df.var(axis=1))   # pandas 采用的是无偏样式方差  方差和/样品数-1

print('---------求标准差----------')  
data = [[100,90,100],[100,78,78],[78,90,78]]
columns = ['数学','语文','英语']
df = pd.DataFrame(data=data,columns=columns,index=[0,1,2])
print(df)
print(df.std(axis=0))  

print('---------求分位数----------')  
data = [120,110,112,100,98,34,123,115]
columns = ['数学']
df = pd.DataFrame(data=data,columns=columns)
print(df)
# 计算35%
x = df['数学'].quantile(0.35)
print(x)

print(df[df['数学']<x])

print('---------------')
df = pd.DataFrame({
    'A':[1,2],
    'B':[pd.Timestamp('2020'),pd.Timestamp('2022')],
    'C':[pd.Timedelta('1 days'),pd.Timedelta('2 days')]
})
print(df.quantile(0.5,numeric_only=False))


print('---------数据格式化-------')
df = pd.read_excel('格式化数据.xlsx')
print(df)
print(df.round(2))  # 对所有元素起作用 保留两位小数

# 对指定列保留小数位数
print(df.round({'A1':1,'A2':2}))    # round中的参数是一个字典

S1 = pd.Series([1,0,2,1,1],index=['A1','A2','A3','A4','A5'])
print(S1)

print('---------------')
df2 = df.round(S1)
print(df2)

print('---------------')
# 还可以使用自定义函数实现保留小数位置
df3 = df.applymap(lambda x : '{:.2f}'.format(x))
print(df3)


# 设置百分比
print('-------设置百分比--------')

df = pd.read_excel('格式化数据.xlsx')
print(df)

print('---------------')
df['百分比'] = df['A1'].apply(lambda x : format(x,'.0%'))   # 对A1列进行设置百分比
print(df)

print('---------------')
df['百分比'] = df['A1'].apply(lambda x : format(x,'.2%'))   # 对A1列进行设置百分比
print(df)

# map()函数
print('-------map()函数设置百分比--------')
df['百分比'] = df['A1'].map(lambda x : format(x,'.2%'))   # 对A1列进行设置百分比
print(df)

# 设置千位分隔符
print('-------设置千位分隔符--------')
df = pd.read_excel('msb课程记录.xlsx')
print(df)
print('---------------')
df['买家实际支付金额'] = df['买家实际支付金额'].apply(lambda x : format(int(x),','))
print(df)
print(df.info())

# apply(),map(),applymap()的区别
#apply()可以在Series，对Series的每一个元素都执行一次函数，也可以在DataFrame中起作用，对DataFrame中的某一行或某一列执行函数
s = pd.Series(data=[10,20,30,40],index=['a','b','c','d'])
print(s)
print('---------------')
s=s.apply(lambda x : x+10)
print(s)

print('---------------')
data = [[76,90,82,74],[84,78,91,71]]
columns = ['A','B','C','D']
index=['a','b']
df = pd.DataFrame(data=data,columns=columns,index=index)
print(df)

print('---------------')
df2 = df.apply(lambda x : x.sum(),axis=0)
print(df2)

# map只能应用在Series的每个元素上
df = pd.DataFrame(data=['男','女','男','男'],columns=['性别'],index=['张三','王五','李四','陈六'])
print(df)

def gender(g):
    return 0 if g == '男' else 1

# map()的参数可传递一个函数 也可以传递一个字典
df2 = df['性别'].map(gender)
print(df2)

df2 = df['性别'].map({'男':0,'女':1})
print(df2)

# applymap()将函数应用在DataFrame每个元素上
data = [[76,90,82,74],[84,78,91,71]]
columns = ['A','B','C','D']
index=['a','b']
df = pd.DataFrame(data=data,columns=columns,index=index)
print(df)

print('---------------')
df=df.applymap(lambda x : x+10)
print(df)
