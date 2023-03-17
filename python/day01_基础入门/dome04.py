'''
    ·1、什么是元组
    ·2、元组的创建方式
    ·3、元组的遍历
    
    ·4、什么是集合
    ·5、集合的创建
    ·6、集合的增、删、改、查操作
    ·7、集合生成式
    
    可变序列    序列、字典
    不可边序列 元组、字符串

'''

# 元组的创建方式 ()
s = ('python','Java','PHP','mysql','R语言')
print(s)

# 使用内置函数tuple()创建元组
s = tuple(('python','Java','PHP','mysql','R语言','C++'))
print(s)

# 只包含一个元素的元组需要用逗号,隔开，否则是字符串类型
s1 = ('C#')
print(type(s1))  #返回 class 'str'

s1 = ('C#',)
print(type(s1))

# 创建空元组
s2 = ()
print(s2)

# 创建空序列
d1 = []
print(d1)

d1 = list([])
print(d1)

# 创建空字典
d2 = {}
print(d2)
print(d2,type(d2))

d2 = dict({})
print(d2)

# 创建空元组
d3 = ()
print(d3)

d3 = tuple(())
print(d3)

# 获取元组
print(s[0])
print(s[1])
print(s[2])
print(s[3])

# 遍历元组
for item in s:
    print(item)
    
    

# 创建集合 集合是值不能重复
ite = {2,4,5,6,7,2,4,6,4,8}
print(ite)

# 通过内存函数set() 创建
ite = set(range(8))
print(type(ite))

s3 = set((1,2,4,4,5,65)) #集合的元素是无序的
# s3 = set((7,5,3,2,1,5,87))
print(s3,type(s3))

# 定义空集合
s4 = set({})
print(s4)


'''
    集合的相关操作
    ·集合元素的判断操作：in或not in
        
    ·集合元素的新增操作：
        ·调用add()方法，一次添中一个元素
        ·调用update()方法至少添中一个元素·集合元素的删除操作
        ·调用remove()方法，一次删除一个指定元素，如果指定的元素不存在抛出KeyError
        ·调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不抛异常
        ·调用pop()方法，一次只删除一个任意元素
        ·调用clear()方法，清空集合

'''
t1 = {10,20,20,40,50,41}
print(t1,type(t1))

# 集合判断的操作
print(10 in t1)
print(70 in t1)
print(70 not in t1)
print(40 not in t1)

# 集合元素新增操作
t1.add(80)
print(t1)

# 通过updata添加至少一个集合元素
t1.update({87,91,67})
print(t1)

# 通过remove()指定删除某个元素
t1.remove(91)
print(t1)

# 通过discard()删除指定元素
t1.discard(67)
print(t1)

# 注意：remove与discard的区别，后者若未查询到指定元素不会抛异常

# 通过pop随机删除一个，不能添加参数
t1.pop()
print(t1)

# 清空集合
t1.clear()
print(t1)


# 判断两个集合是否相等
t2 = {10,20,30,50,60,90}
t3 = {20,10,50,30,60,90}

print(id(t2),t2 == t1)
print(id(t3),t2 != t1)

# 一个集合是否是另一个集合的子集
t4 = {10,20,30,50,60,90}
t5 = {10,20,30}
t6 = {10,20,30,70,88}
t7 = {100,200,300}

print(t5.issubset(t4))
print(t6.issubset(t4))

# 一个集合是否是另一个集合的超集
print(t4.issuperset(t5))
print(t4.issuperset(t6))

# 一个集合是否是另一个集合的交集 有交集返回FALSE
print(t5.isdisjoint(t6))
print(t6.isdisjoint(t7))

# 交集 交集的写法：通过intersection()方法，或者是 & 
print(t4.intersection(t5))
print(t4 & t5)

# 并集 写法:union()方法 或者是 |
print(t4.union(t5))
print(t4 | t5)

# 计算差集 写法：difference() 或是是  -
print(t4.difference(t5))
print(t4 - t5)

# 计算对称交集  写法：symmetric_difference() 或者是 ^
print(t4.symmetric_difference(t5))
print(t4 ^ t5)
