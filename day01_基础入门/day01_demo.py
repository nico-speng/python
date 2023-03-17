# 编写一个程序，将两个数相加并输出结果。
'''print(10+12)'''

# 编写一个程序，从控制台输入一个字符串，反转它并输出结果。
'''
a = input('请输入一个字符串:\n')
b = a[::-1]
print(b)

'''

# 编写一个程序，从控制台输入一个数字，判断它是否是偶数。
'''
s1 = int(input('请输入数字：\n'))
print('偶数' if s1%2 == 0 else '奇数')
'''

# 编写一个程序，从控制台输入一个字符串，计算其中每个字母出现的次数并输出结果。
'''
a = input('请输入一个字符串:\n')
dataStr = {}
for i in a:

# isalpha()判断字符串是否全部由字母组成

  if i.isalpha():
    if i in dataStr:
      dataStr[i] += 1
    else:
      dataStr[i] = 1

for k,v in dataStr.items():
  print(f'字母{k}出现的次数为：{v}')
  
'''

# 编写一个程序，从控制台输入一个列表，将其中的所有元素反转并输出结果。
'''
a = input('请输入一个列表，以空格隔开：\n').split()
b = a[::-1]
print(b)

'''

# 编写一个程序，从控制台输入一个字符串，去除其中的空格并输出结果。
'''
# 使用replace()内置方法去掉空格
a = input('请输入一个字符串:\n').replace(' ', '')
print(a)

'''

# 编写一个程序，从控制台输入两个数字，计算它们的乘积并输出结果。
'''
a = int(input('请输入A的值:\n'))
b = int(input('请输入B的值:\n'))
print('A和B的乘积为:',a*b)

'''

# 编写一个程序，从控制台输入一个列表和一个元素，将该元素插入到列表的末尾并输出结果。
'''
a = input('请输入一个列表，以空格隔开：\n').split()
b = input('请输入一个元素:\n')
a.append(b)
a.extend(b)
print(a)

'''

# 编写一个程序，从控制台输入一个字符串和一个字符，统计该字符在字符串中出现的次数并输出结果。
'''
a = input('请输入一个字符串:\n')
b = input('请输入一个字符:\n')
count = 0

# 通过字典遍历去获得字符出现在字符串的次数
dataStr = {}

for ite in a:
  if ite in dataStr:
    dataStr[ite] += 1
  else:
    dataStr[ite] = 1

if b in dataStr:
  print(f'{b}字符在字符串中出现的次数为:{dataStr[b]}')

# 通过计时器，遍历值与字符对比，满足条件自加1
for i in a:
  if b == i:
    count += 1
print(f'{b}字符在字符串中出现的次数为:{count}')

'''

# 编写一个程序，从控制台输入一个列表和一个元素，将该元素插入到列表的指定位置并输出结果。
'''
a = input('请输入一个列表，以空格隔开:\n').split()
b = input('请输入一个元素:\n')
a.append(b)

for index,item in enumerate(a):
    if item != b:
      continue
    print(index)
    
# 优化代码如下：

print(a.index(b) if b in a else '元素不存在于列表中')
'''

# 编写一个程序，从控制台输入一个字符串，将其中的小写字母转换为大写字母并输出结果。
'''
a = input('请输入小写英文单纯：\n').swapcase()
print(a)

'''

# 编写一个程序，从控制台输入一个数字，判断它是否是质数。
'''
s2 = int(input('请输入数字：\n'))
print('奇数' if s2%2 != 0 else '偶数')

'''

# 编写一个程序，从控制台输入一个字符串，检查它是否是回文字符串。

'''
s = input("请输入一个字符串：")
if s == s[::-1]:
    print("是回文字符串")
else:
    print("不是回文字符串")
'''

# 编写一个程序，从控制台输入一个字符串，将其中的元音字母替换为指定的字符并输出结果。
'''
a = input('请输入一个字符串:\n')
b = input('请输入一个字符:\n')
vls = "aeiouAEIOU"

new_Str = ''
for ite in a:
  if ite in vls:
    new_Str += b;
  else:
    new_Str += ite
    
# 通过列表推导式进行优化：
new_Str = ''.join([b if i in vls else i for i in a])

print(f'{b}替换元音字符的结果为：{new_Str}')

'''


# 编写一个程序，从控制台输入一个列表和一个元素，删除列表中第一次出现的该元素并输出结果。
'''
a = input('请输入一个列表，以空格隔开：\n').split()
b = input('请输入一个元素：\n')

if b in a:
  a.remove(b)

print(a)
'''

# 编写一个程序，从控制台输入一个字符串，统计其中每个单词出现的次数并输出结果。
'''
a = input('请输入一个字符串:\n').split()
dataStr = {}
for item in a:
  if item in dataStr:
    dataStr[item] +=1
  else:
    dataStr[item] =1
    
print('dataStr的数据为：',dataStr)
print('dataStr.items()的数据为：',dataStr.items())

for key,value in dataStr.items():
  print(f'{key}单词出现的次数为{value}')
  '''
  
# 编写一个程序，从控制台输入一个数字，将其转换为二进制并输出结果。
'''
a = bin(int(input('请输入一个数字:\n')))
print(a)

'''

# 编写一个程序，从控制台输入一个列表和一个元素，删除列表中所有出现的该元素并输出结果。
'''
a = input('请输入一个列表，以空格隔开:\n').split()
b = input('请输入一个元素:\n')

while b in a:
    a.remove(b)
print(a)

# 使用列表推导式优化，代码如下：
a = [itme for itme in a if itme!=b]
print(a)
'''

# 编写一个程序，从控制台输入一个字符串，统计其中每个字符出现的次数并输出结果。
'''
a = input('请输入一个字符串:\n')
dataStr = {}
for chart in a:
  if chart in dataStr:
    dataStr[chart] += 1
  else:
    dataStr[chart] = 1

# 遍历字典                                
for item in dataStr:
  print(f'{item}出现次数为:{dataStr[item]}')

# 通过items()方法获取字典的key和value
for key,value in dataStr.items():
    print(f'{key}出现次数为:{value}')

# 以上两段遍历方法区别在于:普通遍历只能通过获取key值，然后通过字典字典key（键值）获取到value
# 而itmes()方法是直接获取到key和value值。
  
'''


# 编写一个程序，从控制台输入一个数字，将其转换为十六进制并输出结果。
'''
a = int(input('请输入一个数字:\n'))
num = hex(a)
print('该数字的十六进制输出结果为:',num)

'''
