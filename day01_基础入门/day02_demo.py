# 1、编写一个类，实现一个静态方法，该方法返回两个数的和。
class Parents_Sum:
    # 初始化函数
    def __init__(self,a,b):
        # 初始化赋值
        self.a = a
        self.b = b
        # print(a+b)
    
    # 定义静态方法
    # 注意：静态方法需要单独传递参数，因为声明了静态方法，就代表该方法垄断了类初始化传递的参数
    # @staticmethod
    # def Son_sum(self):
    #     print(self.a+self.b)
        
    # 正确代码如下：
    @staticmethod
    def Son_sum(a,b):
        print(a+b)

# 创建类对象
sum1 = Parents_Sum(10, 20)
print('\n')

# 用类对象调用方法
print('我是用创建的类对象调用的类方法，结果为：')
sum1.Son_sum(10, 2)
print('\n')

# 直接使用类名.方法调用
print('我是用类名.类方法调用传参获得的结果为：')
Parents_Sum.Son_sum(9,15)
print('\n')

# 2、编写一个类，实现一个类方法，该方法返回该类的类名。
class MyClass:
    @classmethod
    def getName(cls):
        # print(cls)    #   <class '__main__.MyClass'>
        return cls.__name__

print('我是用classmethod内置方法获得方法名，该方法不需要实例化传参数赋值：')
print(MyClass.getName())
print('\n')

# 3、编写一个类，实现一个实例方法，该方法接受一个参数并返回该参数的平方。
class getPow:
    def res_Pow(self):
        # 通过内置函数计算平方
        return pow(self, 2)

print('通过类方法调用计算出平方，结果为：')
print(getPow.res_Pow(12))

# 4、编写一个类，实现一个静态方法，该方法接受一个列表并返回该列表中的最大值。
class num_Max:
    def getMax(self):
        # 使用列表max求最大值，并返回
        return max(self)
    
numList = [10,30,20,21]
print('列表最大值为:',num_Max.getMax(numList))
    

# 5、编写一个类，实现一个类方法，该方法接受一个整数n并返回一个n行n列的乘法表。

class MultiplicationTable:
    def __init__(self, n):
        self.n = n
    
    def print_table(self):
        # 行
        for i in range(1, self.n+1):
            # 列
            for j in range(1, i+1):
                print(f"{j}*{i}={i * j}\t", end='')
            print()

table = MultiplicationTable(9)
table.print_table()

# 6、编写一个类，实现一个实例方法，该方法接受一个字符串并返回该字符串的反转字符串。
class Name_Str:
    def get_Str(self):
        return self[::-1]
    
print(Name_Str.get_Str('happy'))

# 7、编写一个类，实现一个静态方法，该方法接受一个列表并返回该列表中的所有偶数。
class myEven:
    @staticmethod
    def get_even(a):
        
        '''
        dataList = []
        for item in a:
            if item%2 ==0:
                dataList.append(item)
        '''
        
        # 优化代码如下：                
        dataList = [item for item in a if item%2 == 0]
            
        print(dataList)

Even_list = [10,20,30,5]
myEven.get_even(Even_list)

# 8、编写一个类，实现一个类方法，该方法接受一个整数n并返回一个长度为n的斐波那契数列。
class Fibonacci:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.a, self.b = 0, 1
        self.count = 0
        return self
    
    def __next__(self):
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        if self.count < self.n:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration
        
fib = Fibonacci(10)
for num in fib:
    print(num)

# 9、编写一个类，实现一个实例方法，该方法接受一个整数n并返回该整数的阶乘。
class Factorial:


    def compute(self, n):

        if n < 0:
            raise ValueError("The input must be a non-negative integer.")
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
    
    
#10、 编写一个类，实现一个静态方法，该方法接受两个列表并返回两个列表的交集。
class Intersection:
    @staticmethod
    def get_Intersection(list1,list2):
        return [item for item in list1 if item in list2]

list1 = [10,20,30,50]
list2 = [10,20,30]
# 调用类方法
Intersection.get_Intersection(list1,list2)

# 11、编写一个Python类，表示一个矩形，包括求面积和周长的方法。
class Rectangle:
    def __init__(self,high,width):
        self.high = high
        self.width = width

    # 求面积
    def area(self):
        # 面积公式：长 * 宽
        return self.high * self.width


    # 求周长
    def perimeter(self):
        return 2 * (self.high + self.width)
    
# 调用类求面积
rect = Rectangle(5,3)
print(rect.area())
print(rect.perimeter())

# 12、编写一个Python类，表示一个人，包括姓名、性别、年龄等属性以及一个打印个人信息的方法。
class perSon:
    
    def __init__(self,name,sex,age) -> '函数初始化' :
        self.name = name
        self.sex = sex
        self.age = age
    
    def print_info(self):
        print(f'他叫{self.name},性别{self.sex},今年{self.age}')

person = perSon('张三','男',18)
person.print_info()


# 13、编写一个Python类，表示一个汽车，包括品牌、型号、颜色等属性以及一个加速度的方法。
class car:
    def __init__(self,brand,model,color,seep):
        self.brand = brand
        self.model = model
        self.color = color
        self.seep = seep

    def accelerate(self,acceleration):
        self.seep += acceleration
        print(f'{self.color}{self.brand}{self.model}加速到了{self.seep}km/h')


car = car('白色','保时捷','帕拉梅拉xp',20)
car.accelerate(20)


# 14、编写一个Python类，表示一个学生，包括姓名、学号、成绩等属性以及一个求平均成绩的方法。
class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
    
    def average_grade(self):
        if len(self.grades) == 0:
            return None
        
        return sum(self.grades) / len(self.grades)

s = Student("John Doe", 12345, [90, 85, 95])
avg_grade = s.average_grade()
print(avg_grade)

'''
面向对象的知识点：
    类和对象的概念和区别
    属性和方法的概念和区别
    封装、继承、多态的概念和使用
    魔术方法和类方法、静态方法的概念和使用
    类的构造函数和析构函数的概念和使用
    元类和单例模式的概念和使用
    Python标准库中常用的面向对象模块，如pickle、shelve、copy、abc等。
    希望这些例题和知识点对您有所帮助。
'''