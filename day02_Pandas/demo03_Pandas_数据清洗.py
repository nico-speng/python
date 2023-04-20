import pandas as pd


pd.set_option('display.unicode.east_asian.width',True)

df = pd.read_excel('msb课程记录.xlsx')
print(df)

print('-------------------')

print(df.info()) # 查看缺失值

print('-------------------')

# 判断缺失值

print(df.isnull())  # 结果为True或FALSE  不为NaN时为False

print(df.notnull())  # 结果为True或FALSE  不为NaN时为True

print('-------------------')

# df = df.dropna()    # 需要重新赋值给新的变量  会删除所有NaN的所在行数据
# print(df)


print(df[df['课程总数'].notnull()]) # 提前课程总数不为NaN的数据



# 缺失值的处理填充

df['课程总数'] = df['课程总数'].fillna(0)
print(df)


# 重复值的处理

# 判断是否具有重复值

print(df.duplicated())

# 去除全部的重复数据

df = df.drop_duplicates()
print(df)



# 去除指定列的重复数据,保留重复行中的最后一行
jls_extract_var = 'last'
df = df.drop_duplicates(['买家实际支付金额'],keep=jls_extract_var)
print(df)

# 直接删除，保留一个副本 需要赋值新变量
df1 = df.drop_duplicates(['买家实际支付金额'],inplace=False)
print(df1)
print(df)