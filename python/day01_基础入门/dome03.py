'''
    1、什么是字典
    2、字典的原理
    3、字典的创建与删除
    4、字典的查询操作
    5、字典元素的增、删、改操作
    6、字典推导式

    ·字典的特点：
        ·字典中的所有元素都是一个key-value对， key不允许重复, value可以重复
        ·字典中的元素是无序的
        ·字典中的key必须是不可变对象·字典也可以根据需要动态地伸缩
        ·字典会浪费较大的内存，是一种使用空间换时间的数据结构

'''

# 使用{}创建字典
dataList = {
    'name': 'make',
    'age':'18',
    'sex':'girl',
    'text':'快乐girl,happy every day',
    'like':'100',
    'famaily':'Dad'
    }
print(dataList)

# 使用dict创建字典
dataList = dict(name='Jack',age=18)
print(dataList)

# 空字典
d = {}
print(d)

Scores = {
    'name': 'Jack',
    'age':'18',
    'sex':'girl',
    'text':'快乐girl,happy every day',
    'like':'100',
    'famaily':'Dad'
    }
# 获取字典元素
print('通过key获取字典元素：')
print(Scores['name'])


# 通过get获取字典元素
print('通过get方法获取字典元素：')
print(Scores.get('name'))   

# key与get获取字典元素的区别：
# print(Scores['names'])  # KeyError: 'names'
# print(Scores.get('names'))  # None

# 可设置默认值，做为当字典中未存在默认返回404
print(Scores.get('names',404))

# 判断key是否存在
print('name' in Scores)
print('name' not in Scores)

# 删除元素
del Scores['famaily']
print(Scores)

# 修改字典元素
Scores['age'] = 20
print(Scores)

# 获取字典所有的key值
print(Scores.keys())

# 获取字典所有的values值
print(Scores.values())

# 获取字典所有的type类型
print(type(Scores))

# 获取字典所有的键值对
print(Scores.items())       # 得到的是列表
# 列表转换为元组
print(list(Scores.items()))

# 遍历字典元素
for item in Scores:
    print(item+'\n',Scores[item],Scores.get(item))

# 字典中不允许key重复,而value是可以重复的，如下所示：
d = {'name':'Jack','name':'Make','names':'Jack'}
print(d)

items = ['Jack','Nico','STM']
prices = [97,38,64]

# 内置函数zip() 可将对象中的元素打包成一个元组，然后返回元组的值
# upper() 可将key转为大写
d = {item.upper():price   for item,price in zip(items,prices)}
print(d)