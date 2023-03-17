'''
    1、列表的创建与删除
    2、列表的查询操作
    3、列表元素的增、删、改操作
    4、列表元素的排序
    5、列表推导式
'''

# 列表的创建 使用[]或者list() 可创建
print('通过[]创建列表：')
dataList = ['唐僧','孙悟空','猪八戒','沙悟净','白龙马']
print(dataList)
print('\n')


print('通过list()创建列表：')
dataList = list(['唐僧','孙悟空','猪八戒','沙悟净','白龙马','唐僧'])
print(dataList)
print('\n')

# 列表的查询操作
# 当列表中有重复的值，只反馈第一个的索引
print('列表的查询操作:')
print(dataList.index('唐僧'))
# 通过索引查询具体值
print(dataList[3])
# 切片查询
lis = [10,20,30,40,50,60,70,80,90]
print(lis[1:6:1])
print(lis[1:6:2])

# 列表元素的增
print('append把元素添加至列表末尾:')
dataList.append('太上老君')
print(dataList)
print('\n')

print('extend在列表元素至少添加一个元素至列表末尾:')
lis2 = [10,20]
dataList.extend(lis2)
print(dataList)
print('\n')

# 在任意一个位置添加N个元素
lis3 = [1,3,41,41]
dataList[2:] = lis3
print(dataList)
print('\n')


# 列表元素删除操作 若有重复元素，只会删除第一个
dataList.remove(41)
print(dataList)

# 通过索引删除列表中的索引
dataList.pop(2)
print(dataList)

# 通过切片操作删除至少一个元素
lis4 = dataList[1:2]
print(dataList)
print(lis4)

# 清空所有元素
dataList.clear()
print(dataList)

dataList = ['肯德基','麦当劳','良品铺子','百香果','好丽友','华莱士','绝味鸭脖']

# 修改列表元素
dataList[4] = '猪脚饭'
print(dataList)

# 将列表元素降序排序 通过sort(reverse=TRUE或FALSE)进行升序降序排序
lis5 = [10,20,44,6,13,45,67,42]
lis5.sort(reverse=True)
print(lis5)

# 将列表元素降序排序 sorted(参数,reverse=TRUE或FALSE)进行升序降序排序
# TRUE代表降序，FALSE代表升序，并且原列表不能变动
new_lis = sorted(lis5,reverse=False)
print(new_lis)

