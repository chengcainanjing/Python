#coding=utf-8

#导入整个模块
'''
module_name.make_pizza(32, 'mushrooms')
module_name.make_pizza(12, 'pepperoni', 'mushrooms', 'green peppers')
'''

#这就是一种导入方法
#只需要编写一条import语句并在其中指定模块名，
#就可在程序中使用该模块中的所有函数

#导入特定的函数
#from module_name import function_name
#from module_name import function_name0, function_name1, function_name2
#上面的代码中，可以这样写
#from module_name import make_pizza

#使用as给函数指定别名

#如果要导入函数的名称，可能与程序中现在有的名称冲突
#或者函数名称太长
#可指定间断而独一无二的别名--函数的另一个名称，类似于外号
#这是模板：
#from module_name import function_name as fn
#给上面的函数make_pizza()指定别名mp()
#from module_name import make_pizza as mp

#mp(16, 'mushrooms')
#mp(32, 'mushrooms', 'green pepper', 'pepperoni')

#导入模块中的所有函数

#使用星号(*)运算符可以让python导入模块中的所有函数
#from module_name import *
#
#make_pizza(16, 'mushrooms')
#make_pizza(12, 'pepperoni', 'mushrooms', 'green peppers')
#星号让python将模块module_name中的每个函数都复制到这个程序文件中
#由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示
#最好不要这样做，因为，
#这样做有可能会导致模块中的函数名和项目中的函数名相同，
#导致意想不到的结果
#python可能遇到多个名称相同的函数或变量
#进而覆盖函数，
#而不是分别导入所有的函数
#最佳做法是
#要么导入我们需要使用的函数
#要么导入整个模块并使用句点表示法，
#这让代码更清晰、阅读和理解

#函数编写指南

# 每个函数都应包含简要地阐述其功能的注释，
#该注释应紧跟在函数定义后面，并采用文档字符串格式。

#给形参指定默认值时，等号两边不要有空格:
#def function_name(parameter_0,parameter_1='default value')

#对于函数调用中的关键字实参，也应遵循这种约定：
#function_name(value_0,parameter_1='value')

#类

#实例化
#根据类来创建对象被称为实例化，这可以使用类的实例

#创建和使用类
#类Dog，指的是任何小狗
#大多数小狗具有名字和年龄、两种动作（蹲下和打滚）
#类就是把一类具有共同属性的事物封装到一起，不用重复编写这些程序，
#编写好类后，需要的时候只需要调用相应的类即可

#创建Dog类
'''
class Dog(object):
#在python中，首字母大写的名称指的是类		
#这个类定义中括号是空的
#因为我们要从空白创建这个类
	#一次模拟小狗的简单尝试
	#这里是一个文档字符串，对这个类功能进行描述
	
	def __init__(self, name, age):
	#方法__init__（）是一个特殊的方法
        #每当我们根据 Dog 类创建新实例时，python 都会自动运行它
        #这个方法名称中，开头与末尾都有两个下划线，
        #这是一种约定，旨在避免 python 默认方法与普通方法发生名称冲突
        #该方法有三个形参，self,name,age,
        #形参self 是必不可少的，而且必须位于其他形参前面
        #python调用__init__()方法来创建 Dog 实例时，
        #将自动传入实参self
        #每个与类相关联的方法调用都自动传递实参self
        #它是一只指向实例本身的引用，让实例能够访问类中的属性和方法
        #我们创建 Dog 实例时，python 将调用 Dog 类的方法__init__()
        #我们将通过实参向 Dog（）传递名字和年龄，self 会自动传递
        #因此不需要传递它
                
		#初始化name和age
		self.name = name
		self.age = age
		#以 self为前缀的变量都可供类的所有方法使用，我们还可以通过类的
                #任何实例来方位这些变量
                #self.name=name 获取存储在形参 name 中的值 ，并将其
                #存储在变量name 中，然后该变量被关联到当前创建的实例
                #self.age=age 作用与此类似
                #像这样可通过实例访问的变量称为属性
	def sit(self):
		#模拟小狗被命令时蹲下
		print self.name.titel() + ' is now sitting.'
	
	def roll_over(self):
		#模拟小狗被命令打滚
		print self.name.title() + ' rolled over!'
'''

#根据类创建实例
'''
class Dog(object):
	"""一次模拟小狗的简单尝试"""
	
	def __init__(self, name, age):
            """初始化name和age"""
		self.name = name
		self.age = age
	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print self.name.title() + ' is now sitting.'
	
	def roll_over(self):
		"""模拟小狗被命令打滚"""
		print self.name.title() + ' rolled over!'
my_dog = Dog('willie', 6)
#这里创建一个名为 willie，年龄为6的小狗
#python使用实参willie和6调用 Dog 类中的方法__init__()
#方法__init__()创建一个表示特定小狗的实例，
#并使用我们提供的值来设置属性 name 和 age
#我们将这个实例存储在变量my_dog 中
#在这里面，命名约定很重要：
#通常认为首字母大写的名称（如 Dog）指的是类，
#而小写的名称(my_dog)指的是根据类创建的实例
print "My dog's name is " + my_dog.name.title() + '.'
print "My dog's age is " + str(my_dog.age) + ' years old.'
#访问属性 my_dog.name
#访问实例的属性，可使用句点表示法
#句点表示法在 python 中很常用
#调用方法
my_dog.sit()
my_dog.roll_over()
'''

#创建多个实例
'''
class Dog(object):
	#一次模拟小狗的简单尝试
	
	def __init__(self, name, age):
            #初始化name和age
		self.name = name
		self.age = age
	def sit(self):
		#模拟小狗被命令时蹲下
		print self.name.title() + ' is now sitting.'
	
	def roll_over(self):
		#模拟小狗被命令打滚
		print self.name.title() + ' rolled over!'
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print "My dog's name is " + my_dog.name.title() + '.'
print "My dog's name is " + str(my_dog.age) + ' years old.'
#调用方法
my_dog.sit()
my_dog.roll_over()

print "\nYour dog's name is " + your_dog.name.title() + '.'
print "Your dog's name is " + str(your_dog.age) + ' years old.'
#调用方法
your_dog.sit()
your_dog.roll_over()
'''

#test
#9-1
'''
class Restaurant(object):
    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type
    def describe(self):
        print "\nThe name of the restaurant is " + self.restaurant.title()
        print 'The type of the retaurant is ' + self.cuisine_type
    def open_restaurant(self):
        print "The restaurant is openning!"
my_restaurant = Restaurant('shicai', 'sichuan')
my_restaurant.describe()
my_restaurant.open_restaurant()
your_restaurant = Restaurant('jinlei', 'haiyang')
your_restaurant.describe()
your_restaurant.open_restaurant()
'''

#2017.09.18
#使用类和实例
#如何修改实例的属性
'''
class Car(object):
	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
			
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
'''

#添加一个随时间变化的属性
#它存储汽车的总里程

#给属性指定默认值
#类中每个属性都必须有初始值，哪怕这个值是0或空字符串
'''
class Car(object):
	def __init__(self, make, model, year):
		#初始化描述汽车的属性
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def read_odometer(self):
		print 'This car has ' + str(self.odometer_reading) + ' miles on it.'
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
'''

#类属性和实例属性
#由于Python是动态语言，根据类创建的实例可以任意绑定属性。
#给实例绑定属性的方法是通过实例变量，或者通过self变量：
'''
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
'''
#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
'''
class Student(object):
    name = 'Student'
'''
#当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
'''
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
'''
#从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
#但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

#修改属性的值
#三种方法：
#直接通过实例进行修改；
#通过方法进行设置
#通过方法进行递增

#直接修改属性的值
'''
class Car(object):
	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def read_odometer(self):
		print 'This car has ' + str(self.odometer_reading) + ' miles on it.'
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
#下面一行代码是直接修改实例属性的值
my_new_car.odometer_reading = 23 
my_new_car.read_odometer()
'''

#通过方法修改属性的值
'''
class Car(object):
	def __init__(self, make, model, year):
		#初始化描述汽车的属性
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def read_odometer(self):
		print 'This car has ' + str(self.odometer_reading) + ' miles on it.'
	
	#在class类中定义一个新方法，来接受一个里程值
	#并将其存储在self.odometer_reading中
	def update_odometer(self, mileage):
		self.odometer_reading = mileage
		
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(24)
my_new_car.read_odometer()
'''

#对其方法update_odometer()进行一些限制
#不可以回调
'''
class Car(object):
	def __init__(self, make, model, year):
		#初始化描述汽车的属性
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def read_odometer(self):
		print 'This car has ' + str(self.odometer_reading) + ' miles on it.'
	
	#在class类中定义一个新方法，来接受一个里程值
	#并将其存储在self.odometer_reading中
	def update_odometer(self, mileage):
		#在此处添加一个if条件语句，
		#判断mileage与self.odometer_reading大小
		#限制其回调
		if mileage > self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print "You can't roll back on odometer!"
			
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25)
my_new_car.read_odometer()
'''

#通过方法对属性的值进行递增
'''
class Car(object):
	def __init__(self, make, model, year):
		#初始化描述汽车的属性
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def read_odometer(self):
		print 'This car has ' + str(self.odometer_reading) + ' miles on it.'
	
	#在class类中定义一个新方法，来接受一个里程值
	#并将其存储在self.odometer_reading中
	def update_odometer(self, mileage):
		#在此处添加一个if条件语句，
		#判断mileage与self.odometer_reading大小
		#限制其回调
		if mileage > self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print "You can't roll back on odometer!"
	
	#在class类中定义一个新方法，来递增一个里程值
	#并将其加上原来的self.odometer_reading
	def increment_odometer(self, mileage):
		#禁止增加值为负值
		if mileage >= 0:
			self.odometer_reading += mileage
		else:
			print "You can't increment the odometer!"
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25)
my_new_car.read_odometer()
my_new_car.increment_odometer(1)
my_new_car.read_odometer()
'''

#限制访问
'''
#定义一个类
class Student(object):                                 

	#为类的所有属性绑定属性，并且属性为私有变量，外部不能够访问
    def __init__(self,name ,score):
        self.__name = name
        self.__score = score

	#通过内部访问内部数据（私有变量）
    def visit(self):
        print self.__name,self.__score

	#通过内部修改内部数据（私有变量）
    def update(self,score):
        self.__score = score                           

	#为实例定义一个方法
	
    def get_score(self):
        print self.__name,self.__score

#创建一个实例
Zhang = Student('Johnson', 100)                         

#对方法的调用
Zhang.get_score()     

#查看属性
print Zhang._Student__name, Zhang._Student__score
#尽量不要用这种方式访问私有变量，使用类里提供的方法来显示属性值
#如方法get_score(self)
'''

#需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
#特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
#有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
#但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
'''
>>> bart._Student__name
'Bart Simpson'
'''
#但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
#总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
#最后注意下面的这种错误写法：
'''
>>> bart = Student('Bart Simpson', 98)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
'''
#表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
#内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：
'''
>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
'''

#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
'''
class Student(object):
    pass
#然后，尝试给实例绑定一个属性：

>>> s = Student()
>>> s.name = 'Michael' # 动态给实例绑定一个属性
>>> print(s.name)
Michael
'''
#还可以尝试给实例绑定一个方法：
'''
>>> def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
>>> s.set_age(25) # 调用实例方法
>>> s.age # 测试结果
25
'''
#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
'''
>>> s2 = Student() # 创建新的实例
>>> s2.set_age(25) # 尝试调用方法
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'
'''
#为了给所有实例都绑定方法，可以给class绑定方法：
'''
>>> def set_score(self, score):
...     self.score = score
...
>>> Student.set_score = set_score
'''
#给class绑定方法后，所有实例均可调用：
'''
>>> s.set_score(100)
>>> s.score
100
>>> s2.set_score(99)
>>> s2.score
99
'''
#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

#使用__slots__
#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
'''
#然后，我们试试：
'''
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
'''
#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''
>>> class GraduateStudent(Student):
...     pass
...
>>> g = GraduateStudent()
>>> g.score = 9999
'''
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

#@property装饰器
#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
'''
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
'''
#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
#此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
'''
>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
'''
#注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
'''
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
'''
#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
#小结
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

'''
class Screen(object):
	"""使用@property装饰器将方法变为属性来调用"""
	@property
	def width(self):
		return self.__width
	
	@width.setter
	def width(self, width):
		self.__width = width
	
	@property
	def hight(self):
		return self.__hight
	
	@hight.setter
	def hight(self, hight):
		self.__hight = hight
		
	@property
	def resolution(self):
		return self.__width + self.__hight
		
if __name__ == '__main__':
	s = Screen()
	s.width = 1024
	s.hight = 112
	print s.resolution
	print s.width
	print s.hight
'''

