'''
    1、字符串的驻留机制
    2、字符串的常用操作
    3、字符串的比较
    4、字符串的切片操作
    5、格式化字符串
    6、字符串的编码转换
    
    查找字符串的操作方法
    index()查找子串substr第一次出现的位置,如果查找的子串不存在时，则抛出ValueError
    rindex()查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError
    find()查找子串substr第一次出现的位置,如果查找的子串不存在时，则返回-1
    rfind()查找子串substr最后一次出现的位置,如果查找的子串不存在时，则返回-1

    upper()把字符串中所有字符都转成大写字母
    lower()把字符串中所有字符都转成小写字母
    swapcase()把字符串中所有大写字母转成小写字母，把所有小写字母都转成大写字母
    capitalize()把第一个字符转换为大写，把其余字符转换为小写
    title()把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写

'''

# 字符串的驻留机制
a = 'python'
b = "python"
c = '''python'''

# 以下字符串ID是相同的，所以这就是字符串驻留机制
print(a,id(a))
print(b,id(b))
print(c,id(c))

s1 = 'abc%'
s2 = 'abc%'
print(s1 is s2)

a=-6
b=-6
print(a is b)


# 查找字符串的操作方法：
S1 = 'hello hello'
S2 = 'hEllo heLLo'
print(S1.index('o'))    # 正向索引查询
print(S1.rindex('o'))   # 逆向索引查询
print(S1.find('o'))     # 正向索引查询  若查询不到，则反馈-1
print(S1.rfind('o'))    # 逆向索引查询  若查询不到，则反馈-1

# 大小写转换操作
print(S1.upper())       #将所有字母转换成大写
print(S1.lower())       #将所有字母转换成小写
print(S2.swapcase())    #将字符串中小写转成大写，大写转成小写
print(S1.capitalize())  #将字符串首字母转为大写，其余小写
print(S2.capitalize())  #将字符串首字母转为大写，其余小写

'''
    center():居中对齐，第1个参数指定宽度，第2个参数指定填充符,第2个参数是可选的，默认是空格,如果设置宽度小于实际宽度则则返回原字符串
    
    ljust():左对齐，第1个参数指定宽度，第2个参数指定填充符,第2个参数是可选的，默认是空格如果设置宽度小于实际宽度则则返回原字符串
    
    rjust():右对齐,第1个参数指定宽度，第2个参数指定填充符,第2个参数是可选的，默认是空格如果设置宽度小于实际宽度则则返回原字符串
    
    zfill():右对齐，左边用O填充,该方法只接收一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度,返回字符串本身

'''

# 字符串对齐操作
print(S1.center(20,'*'))
print(S1.ljust(20,'*'))
print(S1.rjust(20,'*'))
print(S1.zfill(20))

'''
    字符串劈分操作的方法：
    split():从字符串的最左边开始劈分，默认的劈分字符是空格字符串，返回的是一个列表
    rsplit():从字符串的最右边开始劈分，默认的劈分字符是空格字符串，返回的是一个列表
    通过参数sep指定劈分字符串的是劈分符
    通过maxsplit指定最大劈分的次数
'''

# 字符串分隔
S3 = 'hello world python'
lis = S3.split()
print(lis)

# 通过参数sep指定劈分字符串的是劈分符
S3 = 'hello|world|python'
lis = S3.split('|',1)   # lis = S3.split(sep='|',maxsplit=1)
print(lis)

# 通过rsplit从右侧开始劈分
S3 = 'hello|world|python'
lis = S3.rsplit('|',1)   # lis = S3.rsplit(sep='|',maxsplit=1)
print(lis)

'''
    isidentifier():判断指定的字符串是不是合法的标识符
    isspace():判断指定的字符串是否全部由空白字符组成(回车、换行，水平制表符)
    isalpha():判断指定的字符串是否全部由字母组成
    isdecimal():判断指定字符串是否全部由十进制的数字组成
    isnumeric():判断指定的字符串是否全部由数字组成
    isalnum():判断指定字符串是否全部由字母和数字组成

'''
S4 = 'hello,python'
S5 = '14434543'
print(S4.isidentifier())    # 合法的字符串标识符是会包含数字和字母

# 判断字符串是否有空不字符组成
print(S4.isspace())

# 判断指定的字符串是否全部由字母组成
print(S4.isalpha())

# 判断指定字符串是否全部由十进制的数字组成
print(S4.isdecimal())

# 判断指定的字符串是否全部由数字组成
print(S5.isnumeric())

# 判断指定字符串是否全部由字母和数字组成
print('001Helle'.isalnum())


'''
    replace():第1个参数指定被替换的子串，第2个参数指定替换子串的字符串,该方法返回替换后得到的字符串，替换前的字符串不发生变化
    调用该方法时可以通过第3个参数指定最大替换次数
    join():将列表或元组中的字符串合并成一个字符串

'''

# 字符串替换
S6 = 'hello python'
print(S6.replace('python', 'java'))

S6 = 'hello,python,python,python'
print(S6.replace('python', 'java',2))

# 将列表和元组的字符串合并成一个字符串
lis1 = ['hello','python','java']
print(','.join(lis1))


lis1 = ('hello','python','java')
print(','.join(lis1))

print(','.join('python'))
