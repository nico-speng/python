import pandas as pd


# 读取同目录下的表格数据
df = pd.read_excel('中超赛事表.xlsx')
print(df)

# 创建Series对象
# 格式：pd.Series(data,index=index)
# data:表示数据
# index:表示索引

data = ['sun','make','jack']
s = pd.Series(data,index=[1,2,3])
print(s)

# 通过位置索引获取值
print(s[1])

# 标签索引 获取多个标签索引值使用[[标签1],[标签2]]
print(s[[1,2]])

# 切换索引
print(s[:3:2])

# 获取索引
print(s.index)
# 转为list序列
print(list(s.index))

# 获取内容
print(s.values,type(s.values))  # numpy.ndarray类型
print(list(s.values))

# pd.DataFrame(data,index,columns,dtype)
# data:数据 index:索引  columns:列名    dtype:类型
# 列表方式创建DataFrame对象
data = [['小太阳',320.9,100],['鼠标',150.9,50],['小刀',1.5,200]]
columns = ['名称','单价','数据']
df = pd.DataFrame(data,columns)
print(df,type(df))

# 字典方式创建DataFrame对象
data = {
    '名称':['小太阳','鼠标','小刀'],
    '单价':[320.9,150.9,1.5],
    '数量':[100,50,200],
    '公司':'东门超市'
}
df = pd.DataFrame(data=data)
print(df)

# 修改DataFrame对象索引
df.index = [3,4,5]
print(df)
# 获取columns的名称
print(list(df.columns))

# 行列转换
pd.set_option('display.unicode.east_asian_width',True) # 规整格式
new_df = df.T
print(new_df)

print('查看前N条数据\n',df.head(1))
print('查看后N条数据\n',df.tail(1))

# 查看多少行多少列 0表示行  1表示列
print('行',df.shape[0],'列',df.shape[1])

print('查看索引、数据类型、内存信息\n',df.info())

# 查看每列的统计汇总数据，DataFrame类型
print(df.describe())
# 返回每一列的非空个数
print(df.count())
# 返回每一列的和，无法及时返回空值
print(df.sum())
# 返回每一列的最大值
print(df.max())
# 返回每一列的最小值
print(df.min())


# 导入外部数据
# pd.read_excel(io,sheet_name,header)
# io:表示文件路径
# sheet_name:表示工作表，如下所示
# header:默认值为0，取第一行的值为列名，数据为除列名外的数据，如果数据不包含列列名，则header=None 

# sheet_name=0    #第一个sheet页中的数据作为DataFrame对象
# sheet_name=1    #第二个sheet页中的数据作为DataFrame对象
# sheet_name='sheet1' #名称为'sheet1'的sheet页中的数据作为DataFrame对象
# sheet_name=[0,1,'sheet3'] # 第一个、第二个和名称为sheet3的sheet也中的数据作为DataFrame对象
# sheet_name=None  #读取所有工作表

df = pd.read_excel('NEW评论.xlsx')
print(df)

# usecols 导入一列数据
df = pd.read_excel('NEW评论.xlsx',usecols=[2,3])
print(df)

# 导入csv文件
df = pd.read_csv('csv数据.csv',sep=',',encoding='gbk')
print(df)

# 导入html网页
url = 'http://www.espn.com/nba/salaries'
df = pd.DataFrame() # 创建一个空的DataFrame对象

# DataFrame添加数据  只能导入table标签的数据
df = df.append(pd.read_html(url,header=0))
print(df)

# 报存成cvs文件
df.to_csv('nbasalary.csv',index=False)

