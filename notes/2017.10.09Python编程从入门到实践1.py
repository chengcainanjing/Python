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
#python 使用实参willie和6调用 Dog 类中的方法__init__()
#方法__init__()创建一个表示特定小狗的实例，
#并使用我们提供的值来设置属性 name 和 age
#我们将这个实例存储在变量my_dog 中
#在这里面，命名约定很重要：
#通常认为首字母大写的名称（如 Dog）指的是类，
#而小写的名称(my_dog)指的是根据类创建的实例
print "My dog's name is " + my_dog.name.title() + '.'
print "My dog's name is " + str(my_dog.age) + ' years old.'
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

#修改属性的值
#三种方法：
#直接通过实例进行修改；
#通过方法进行设置
#通过方法进行递增

#直接修改属性的值
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
