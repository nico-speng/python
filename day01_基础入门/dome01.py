'''
    
    什么是转义字符呢?
    就是反斜杠+想要实现的转义功能首字母。
    
    为什么需要转义字符?
    当字符串中包含反斜杠、单引号和双引号等有特殊用途的字符时，必须使用反斜杠对这些字符进行转义（转换一个含义)
    换行：\n
    回车：\r
    水平制表符：\t
    退格：\b
    
    当字符串中包含换行、回车，水平制表符或退格等无法直接表示的特殊字符时，也可以使用转义字符当字符串中包含换行、回车，水平制表符或退格等无法直接表示的特殊字符时，也可以使用转义字符
    反斜杠：\\
    单引号：\'
    双引号：\"

'''

# 转义字符
print('hello\nworld')   #   +转义功能的首字母   n ——> newline的首字母表示换行
print('hello\tworld')
print('hello00\tworld')
print('hello\rworld')   #world将hello进行覆盖
print('hello\bworld')   #\b是退一个格，将o退没了

print('http:\\\\baidu.com')
print('老师说:\'大家好！\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r,或R
print(r'hello\nworld ')
# 注意事项：原字符，最后一个不能是反斜杠,例如：print(r'hello\nworld\')
print(r'hello\nworld\\')

''' 
    变量是什么？
    变量是一个标签的盒子
    id：标识    type：类型  name='m'
'''

'''
    以下对象的布尔值都未false
'''
print('\n以下对象的布尔值都未false:')
print(bool(0))          #为FALSE
print(bool(0.0))        #为FALSE
print(bool(''))         #为FALSE
print(bool(""))         #为FALSE
print(bool(None))       #为FALSE
print(bool([]))         #空序列
print(bool(list()))     #空序列
print(bool(()))         #空元组
print(bool(tuple()))    #空元组
print(bool({}))         #空字典
print(bool(dict()))     #空字典
print(bool(set()))      #空字典


# 使用for in 打印九九乘法表
for i in range(1,10):
    for item in range(1,i+1):
        print(item,'*',i,'=',item*i,end='\t')
    print('\n')


# 使用while 打印九九乘法表
i=0
while i<10:
    for item in range(1,i+1):
        print(item,'*',i,'=',item*i,end='\t')
    print('\n')
    i+=1

# 打印所有5的倍速 使用continue调出不符合条件的代码
for i in range(1,101):
    if i%5!=0:
        continue
    print(i)
        