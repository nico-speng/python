'''
    面向对象
'''

class Student:
    native_name = '吉林'
    
    def __init__(self,name,age):
        self.name = name        #self.name 称为实例属性，进行了一个赋值操作，将局部变量的name赋值给实体属性
        self.age = age
    
    # 实例方法
    def eat(self):
        print('学生在吃饭')
    
    # 静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
        
    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')


# 在类之外定义的称为函数，在类之外定义的称为函数
def drink():
    print('喝水')
    
    
    
# 创建student类的对象
student = Student('张三', 18)
print(id(student))
print(type(student))
print(student)

# 调用类的方法
student.eat()


# 使用类属性
print(student.native_name)
student.native_name = '天津'
print(student.native_name)


''' 
    面向对象类的继承
'''

# 父类
class Parents:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f'姓名：{self.name}，年龄：{self.age}')
        

class SonClass(Parents):
    # 初始化 def __init__
    def __init__(self,name,age,career):
        # 重新继承父类
        super().__init__(name, age)      
        # 重新修改定义属性   
        self.son_career = career
        super().info()
        print(f'职业为:{self.son_career}')

class SonClass1(Parents):
    def __init__(self,name,age,sex):
        # 继承父类
        super().__init__(name, age)
        self.son_sex = sex
        
# 创建类
stu1 = SonClass('Jack',18,'老师')
stu2 = SonClass1('Mackie',38,'女')



person.info()
# 调用父类的方法
stu1.info()
stu2.info()

class Base(object):
    def greet(self):
        print('hi,I am Base')
 
class A(Base):
    def greet(self):
        Base.greet(self)  #通过父类Base直接调用greet方法，并把self作为参数
        print('hi,I am A')
 
 
a=A()

a.greet()

