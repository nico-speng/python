
'''
    try...except...else结构：
    如果try块中没有抛出异常，则执行else，如果try中抛出异常，则执行except
    
    try...except...else...finally结果:
    finally快无论是否发生异常都会被执行，能常用来释放try块中申请的资源
    
    
'''

try:
  a = int(input('请输入一个除数数字：\t'))
  b = int(input('请输入一个被除数数字：\t'))
  result = a/b
except BaseException() as e:
  print('出错了')
  print(e)

else:
    print('结果为：',result)
    
finally:
    print('感谢您的使用')