import pandas as pd

'''
    Pandas中str反馈的是object数据类型
    Pandas中float反馈的数据类型是float64
    data 列表数据
    columns 列索引

    DataFrame的重要属性：
    values：查看所有元素的值
    dtype：查看所有元素的类型
    index：查看所有行名、重命名行名
    columns：查看所有列名、重命名列名
    T：行列数据的转换
    head：查看前N条数据，默认是前面5条
    tail：查看后N条数据，默认是前面5条
    shape：查看行数和列数，shape[0]表示行，shape[1]表示列
    info：查看索引、数据类型和内存信息

    DataFrame的重要函数
    describe()：查看每列的统计汇总信息，DataFrame类型
    count()：返回每一列的非空值的个数
    sum()：返回每一列的和，无法统计反馈空值
    max()：返回每列最大值
    min()：返回每一列最小值
'''

# 定义二维序列
data = [['小太阳','233.2','180'],['鼠标','167.6','89'],['小刀','150','35']]
# 设定列索引名称
columns = ['名称','价格','数量']
df = pd.DataFrame(data=data,columns=columns)
print(df)
# 数据类型为 Pands的dataFrame对象类型
print(type(df))
print('\n')

# 通过字典方式创建DataFrame对象
S1 = {
    '名称':['小太阳','鼠标','小刀'],
    '价格':[233.2,167.6,150],
    '数量':[180,89,35],
}
print('通过字典方式创建DataFrame对象')
df = pd.DataFrame(S1)
print(df)
print('\n')

# DataFrame的重要属性
# 查看所有元素的值
print('查看所有元素的值：')
print(df.values)
print('\n')

# 查看所有元素的类型
print('查看所有元素的类型：')
print(df.dtypes)
print('\n')

# 查看所有元素的行名称
print('查看所有元素的行名称：')
print(df.index)
print('\n')

# 查看具体名称
print('查看具体列名称索引：')
print(list(df.index))
print('\n')

# 修改元素的行索引
print('修改元素的行索引：')
df.index=[1,2,3]
print(df)
print('\n')

# 查看所有元素的列索引
print('查看所有元素的行名称：')
print(df.columns)
print('\n')

# 查看具体行名称
print('查看具体行名称索引：')
print(list(df.columns))
print('\n')

# 修改元素的列索引
print('修改元素的列索引：')
df.columns=['商品名称','商品价格','商品数量']
print(df)
print('\n')

# 规则格式
pd.set_option('display.unicode.east_asian_width',True)
# 行列数据的转换
print('行列数据的转换：')
print(df.T)
print('\n')

# 查看前N条数据，默认前5条：
# ()不传参，默认展示5条
print('查看前N条数据，默认前5条：')
print(df.head(1))
print('\n')

# 查看前N条数据，默认后5条：
# ()不传参，默认展示5条
print('查看前N条数据，默认后5条：')
print(df.tail(1))
print('\n')

# 查看多少行，多少列
print('查看多少行，多少列：')
print('行',df.shape[0],'列',df.shape[1])
print('\n')

# 查看索引、数据类型和内存信息
print('查看索引、数据类型和内存信息:\n',df.info)
print('\n')


# DataFrame的重要函数
print('查看每列的统计汇总信息:')
print(df.describe())
print('\n')

# 返回每一列的非空值的个数
print('返回每一列的非空值的个数:')
print(df.count())
print('\n')

# 返回每一列的和，无法统计反馈空值
print('反馈每一列的和：')
print(df.sum())
print('\n')

# 返回每列最大值
print('返回每列最大值：')
print(df.max())
print('\n')

# 返回每一列最小值
print('返回每列最小值：')
print(df.min())
print('\n')
