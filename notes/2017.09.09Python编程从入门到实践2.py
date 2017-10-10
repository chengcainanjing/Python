#coding=utf-8

#import os
#import json

#继承
#编写的类似从另一个现成类的特殊版本，可使用继承
#一个类继承另一个类
#他将自动获得另一个类的所有属性和方法
#原有的类称为父类
#新类称为子类
#子类继承父类的所有属性和方法
#同时还可以定义自己的属性和方法

#子类的方法__init__()
#创建子类的实例时，python首先需要完成任务是
#给父类的所有属性赋值
#因此，子类的方法__init__()需要父类施以援手

#父类也称为超类
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

#(2)子类			
class ElectricCar(Car):
	def __init__(self, make, model,year):
		#(4)
		super(ElectricCar, self).__init__(make,model,year)

#(5)		
my_tesla = ElectricCar('tesla', 'model s', 2016)
name = my_tesla.get_descriptive_name()
print name			
'''

'''
	首先是Car类的代码。创建子类时，父类必须包含在当前文件中，且位于子类前面。
	
	在2处，我们定义了子类ElectricCar。定义子类时，必须在括号内指定父类的名称。
方法__init__()接受创建Car实例所需的信息。
	
	4处的super()是一个特殊函数，帮助Python将父类和子类关联起来，
这行代码让Python调用ElectricCar的父类的方法__init__()，让ElectricCar实例
包含父类的所有属性。
父类也称为超类(supercalss),名称super因此而得名。
    
	为测试继承是否能够正确地发挥作用，我们尝试创建一辆电动汽车，
但提供的信息与创建普通汽车时相同。
在5处，我们创建ElectricCar类的一个实例，
并将其存储在变量my_tesla中。
这行代码调用ElectricCar类中定义的方法__init__()，
后者让Python调用父类Car中定义的方法__init__()。
我们提供了实参'tesla','model s'和2016.
    
	除方法__init__()外，电动汽车没有其他特有的属性和方法。
当前，我们只想确认电动汽车具备普通汽车的行为：
2016 Tesla Model S
    ElectricCar实例的行为与Car实例一样，
现在可以开始定义电动汽车特有的属性和方法了。
'''

'''
在Python2.7中，继承语法稍有不同，ElectricCar类的定义类似与下面这样：
class Car(obiect):
　　def __init__(self,make,model,year):
class ElectricCar(Car):
　　def __init__(self,make,model,year):
　　　　super(ElectricCar,self).__init__(make,model,year)
super()函数需要两个实参：子类名和对象self。
为帮助Python将父类和子类关联起来，这些实参必不可少。
另外，在Python2.7中使用继承时，务必在父类时在括号内指定object。
'''

#给子类定义属性和方法
'''
class Car(object):
	"""定义一大类-车"""
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

#(2)子类			
class ElectricCar(Car):
	"""定义一个子类-电动车，继承父类-车"""
	def __init__(self, make, model,year):
		#(4)
		super(ElectricCar, self).__init__(make,model,year)
		#添加子类的新属性，并设置其初始值（70）
		#根据ElectricCar类创建的所有实例都将包含这个属性
		#但所有Car实例都不包含它
		self.battery = 70
	
	def describe_battery(self):
		print "This car has a " + str(self.battery) + "-kwh battery."
		
#(5)		
my_tesla = ElectricCar('tesla', 'model s', 2016)
name = my_tesla.get_descriptive_name()
print name			

my_tesla.describe_battery()
'''

#重写父类的方法
#对于父类的方法，只要不符合子类模拟的实物的行为，都可以对其进行重写
#因此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名
#这样，python将不会考虑这个父类的方法，而知关注你在子类中定义的相应方法
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

	def fill_gas_tank(self):
		print  self.make.title() + " needs a gas."
		
	
#(2)子类			
class ElectricCar(Car):
	def __init__(self, make, model,year):
		#(4)
		super(ElectricCar, self).__init__(make,model,year)
		#添加子类的新属性，并设置其初始值（70）
		#根据ElectricCar类创建的所有实例都将包含这个属性
		#但所有Car实例都不包含它
		self.battery = 70
	
	def describe_battery(self):
		print "This car has a " + str(self.battery) + "-kwh battery."
	
	def fill_gas_tank(self):
		#电动车没有油箱,重写父类的方法
		print  self.make.title() + " doesn't need a gas."

#(5)	
my_new_car = Car('audi', 'a4', 2014)	
print my_new_car.get_descriptive_name()
my_new_car.fill_gas_tank()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print my_tesla.get_descriptive_name()		
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
'''

#将实例用作属性
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

	def fill_gas_tank(self):
		print  self.make.title() + " needs a gas."
		
#将一个类作为属性
#定义一个名为Battery的新类
#没有继承任何类
class Battery():
	#方法__init__()除了self外，还有一个形参battery_size,设定了默认值
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
	
	def describe_battery(self):
		print "This car has a " + str(self.battery_size) + "-kwh battery."
						
class ElectricCar(Car):
	def __init__(self, make, model,year):
		super(ElectricCar, self).__init__(make,model,year)
		#在ElectricCar类中，添加一个self.battery属性
		#这行代码让python创建一个新的Battery实例，
		#并将该实例存储在属性self.battery中，
		#每当方法__init__()被调用时，都将执行该操作
		#因此现在每个ElectricCar实例都包含一个自动创建的Battery实例
		self.battery = Battery()
		
	def fill_gas_tank(self):
		#电动车没有油箱,重写父类的方法
		print  self.make.title() + " doesn't need a gas."

my_tesla = ElectricCar('tesla', 'model s', 2016)

print my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
#上面这行代码让python在实例my_tesla中查找属性battery
#并对存储在该属性下的battery实例调用方法describe_battery()
'''

#下面给Battery类添加一个方法，根据电瓶容量报告汽车的续航里程
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

	def fill_gas_tank(self):
		print  self.make.title() + " needs a gas."
		
#将一个类作为属性
#定义一个名为Battery的新类
#没有继承任何类
class Battery(object):
	#方法__init__()除了self外，还有一个形参battery_size,设定了默认值
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
	
	def describe_battery(self):
		print "This car has a " + str(self.battery_size) + "-kwh battery."

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print message
		
class ElectricCar(Car):
	def __init__(self, make, model,year):
		super(ElectricCar, self).__init__(make,model,year)
		#在ElectricCar类中，添加一个self.battery属性
		#这行代码让python创建一个新的Battery实例，
		#并将该实例存储在属性self.battery中，
		#每当方法__init__()被调用时，都将执行该操作
		#因此现在每个ElectricCar实例都包含一个自动创建的Battery实例
		self.battery = Battery()
		
	def fill_gas_tank(self):
		#电动车没有油箱,重写父类的方法
		print  self.make.title() + " doesn't need a gas."

my_tesla = ElectricCar('tesla', 'model s', 2016)

my_tesla.battery.battery_size = 85
print my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()
'''

#多继承
#MixIn
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
#但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

#为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
#类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：
'''
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
	pass
'''
#MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
#Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
#而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
#比如，编写一个多进程模式的TCP服务，定义如下：
'''
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
'''
#编写一个多线程模式的UDP服务，定义如下：
'''
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
'''
#如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
'''
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
'''
#这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
#小结
#由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
#只允许单一继承的语言（如Java）不能使用MixIn的设计。




#导入单个类
#关联的文件名是module_car
#from module_car import Car
'''
my_new_car = Car('audi', 'a4', 2016)
print my_new_car.get_descriptive_name()

my_new_car.update_odometer(25)
my_new_car.read_odometer()
'''

#在一个模块中存储多个类
#关联文件名是module_car
#from module_car import ElectricCar
'''
my_tesla = ElectricCar('tesla', 'model s', 2016)

print my_tesla.get_descriptive_name()
my_tesla.battery.battery_size = 85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
'''

#从一个模块中导入多个类
#from module_car import Car,ElectricCar实例的行为与Car实例一样
'''
my_beetle = Car('volkswagen', 'beetle', 2016)
print my_beetle.get_descriptive_name()

my_tesla = ElectricCar('tesla', 'medel s', 2016)
print my_tesla.get_descriptive_name()
'''

#导入整个模块
#import module_car
'''
my_beetle = module_car.Car('volkswagen', 'beetle', 2016)
print my_beetle.get_descriptive_name()

my_tesla = module_car.ElectricCar('tesla', 'medel s', 2016)
print my_tesla.get_descriptive_name()
'''

#导入模块中的所有类
#from module_name import *
#不推荐这种导入方式
#这里之所以介绍这种导入方式，是因为虽然不推荐这种方式，
#但我们可能会在别人编写的代码中见到它。
#需要从一个模块中导入很多类时，最好导入整个模块，
#并使用module_name.class_name语法来访问类。
#这样做时，虽然文件开头并没有列出用到的所有类
#但我们清楚地知道在程序的哪些地方使用了导入的模块；
#我们还避免了导入模块中的每个类可能引发的名称冲突。

#在一个模块中导入另一个模块
#在文件名为：module_ElectricCar.py中，
#from module_car import Car
#在此文件中头部加入
#from module_car import Car
#from module_ElectricCar import ElectricCar
'''
my_beetle = Car('volkswagen', 'beetle', 2016)
print my_beetle.get_descriptive_name()

my_tesla = ElectricCar('tesla', 'medel s', 2016)
print my_tesla.get_descriptive_name()
'''

#自定义工作流程

 #Python标准库
#   Python标准库是一组模块，安装Python都包含它。
#我们现在对类的工作原理已有大致的了解，可以开始使用其他程序员编写好的模块了。
#可使用标准库中的任何函数和类，为此只需在程序开头包含一条简单的import语句。
#下面来看模块collections中的一个类——OrderedDict。
#文件头部添加:
#from collections import OrderedDict
'''
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'C'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
	print name.title() + "'s favorite language is " + language.title() + '.'
	
print favorite_languages
'''

#test
#9-14
#from random import randint
'''
class Die(object):
	#模拟随机在掷骰子
	def __init__(self, sides=6):
		#初始化骰子基本属性
		self.sides = sides
		
	def roll_die(self, number):
		#打印位于1和骰子面之间的随机数，并掷10次
		random_numbers = []
		for i in range(number):
			random_number = randint(1, self.sides)
			print random_number
			random_numbers.append(random_number)
		print random_numbers
		print '\n'

dice_number = Die(6)
dice_number.roll_die(10)

dice_number = Die(10)
dice_number.roll_die(10)

dice_number = Die(20)
dice_number.roll_die(10)			
'''
	
#类编码风格

#	类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。
#实例名和模块名都采用小写风格，并在单词之间加上下划线。
#实例名和模块名都采用小写格式，并在单词之间加上下划线。
#   对于每个类，都应紧跟在类定义后面包含一个文档字符串。
#这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。
#每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
#   可使用空行来组织代码，但不要滥用。
#在类中，可使用一个空行来来分隔方法；而在模块中，可使用两个空行来分隔类。
#   需要同时导入标准库的模块和我们编写的模块时，
#先编写导入标准库模块的import语句的程序中，再添加一个空行，
#然后编写导入我们自己编写的模块的import语句。
#在包含多条import语句的程序中，
#这种做法让人更容易明白程序使用的各个模块都来自何方。			

#文件与异常
'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print contents.rstrip()
'''

#文件路径
'''
with open('/Users/chengcai/Documents/GitHub/Python/pi_digits.txt') as file_object:
    contents = file_object.read()
    #使用方法read()读取这个文件的全部内容,并将其作为一个长长的字符串存储在变量contents中
    print contents.rstrip()
    #方法rstrip()删除字符串末尾的空白
'''

#逐行读取
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in lines:
    print line
'''

#创建一个包含文件各行内容的列表
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    #readlines()方法从文件中读取每一行，并将其存储在一个列表中，
    #接下来，该列表被存储到变量lines中
    
for line in lines:
    print line.rstrip()
'''

#使用文件内容
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print pi_string
print len(pi_string)
'''

#包含一个百万位的大型文件
#2017.09.19

#print os.getcwd() #显示当前工作目录
#在notepad++中，打开文件后显示的是notepad++所在的程序目录
#在python2.7IDLE中显示的是此文件所在的文件夹目录
#对于类的导入，可在此文件所在的文件夹中搜索对应的模块，
#而在下面代码中,open()不可以搜索对应的文件夹
#具体的细节不了解，存在疑问？？？
#下面代码，报错：
#IOError:[Errno 2] No such file or directory: 'digit.txt'
'''
#import os
print os.getcwd()	#显示当前工作目录
with open('pi_digits.txt','r') as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()
	
print pi_string[:52] + '...'
print len(pi_string)
'''	


#对上面代码进行改进
#引入import os模块
#引入os.path.dirname(__file__)
'''
#import os
print '当前所在工作目录：' + os.getcwd()	#显示当前工作目录

path = os.path.dirname(__file__)	#显示此文件所在目录
print '当前文件所在目录：' + path
#对于print输出中文的讨论：
#在windows，用notepad++时，如果使用utf-8编码，执行时，会显示乱码
#如果转码为ANSI时，再执行，就显示正常为中文

filename = path + '\pi_million_digits.txt'

with open(filename, 'r') as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()
	
print pi_string[:52] + '...'
print len(pi_string)
'''

#圆周率值中包含你的生日吗
'''
#import os
print '当前所在工作目录：' + os.getcwd()	#显示当前工作目录

path = os.path.dirname(__file__)	#显示此文件所在目录
print '当前文件所在目录：' + path
#对于print输出中文的讨论：
#在windows，用notepad++时，如果使用utf-8编码，执行时，会显示乱码
#如果转码为ANSI时，再执行，就显示正常为中文

filename = path + '\pi_million_digits.txt'

with open(filename, 'r') as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()
	
birthday = raw_input('Enter your birthday, in the from mmddyy: ')
if birthday in pi_string:
	print 'Your birthday appears in the first million digits of pi!'
else:
	print 'Your birthday does not appear in the first million digits of pi!'
'''
	
	
#test
#10-1	
'''
#import os
path = os.path.dirname(__file__)
print '当前文件所在目录：' + path

filename = 	path + '\pi_digits.txt'

#打印整个文件
with open(filename) as file_object:
	contents = file_object.read()
	print contents.rstrip()
	
#打印时遍历文件对象
with open(filename) as file_object:
	for line in file_object:
		print line.strip()

#打印时将各行存储在一个列表中
with open(filename) as file_object:
	lines = file_object.readlines()
	#lines是一个列表，打印出来的每个元素后面带有\n
	print lines
	
	pi_string = ''
	
	for line in lines:
		print line.strip()
		#这是打印列表中的每一行
		pi_string += line.strip()
		#这是将每一行合并起来变成一行
	print pi_string
'''

#10-2
'''
path = os.path.dirname(__file__)
print '当前文件所在目录：' + path

filename = 	path + '\pi_digits.txt'
	
#打印时遍历文件对象
lines = []
with open(filename) as file_object:
	
	print '原来的数据： '
	for line in file_object:
		print line.rstrip()
		string = line.replace('1', '2')
		lines.append(string)

print '替换后的数据：'
for line in lines:
	print line.rstrip()
'''

#写入文件
'''
#import os
path = os.path.dirname(__file__)
print '当前文件所在目录：' + path

filename = path + '\write_message.py'
with open(filename, 'w') as file_object:
	file_object.write('I love programming.\n')
	file_object.write('I love creating new game.\n')
'''

	
#附加到文件
'''	
#import os
path = os.path.dirname(__file__)
print '当前文件所在目录：' + path

filename = path + '\write_message.py'
with open(filename, 'a') as file_object:
	file_object.write('I also like playing pingpang.\n')
	file_object.write('I like creating apps that can run in a browser.\n')
'''
	
#test 
#10-3
'''
#import os
path = os.path.dirname(__file__)
print '当前文件所在目录：' + path

filename = path + '\write_message.py'
with open(filename, 'a') as file_object:
	message = '如果输入为：quit，则退出！\n'
	message += '请输入名字：'
	
	while True:
		add_string = raw_input(message) 
		if add_string == 'quit':
			break
		else:
			file_object.write(add_string+'\n')
'''

#10-4
'''
#import os
path = os.path.dirname(__file__)
print '当前文件所在目录：' + path

filename = path + '\write_message.py'
with open(filename, 'a') as file_object:
	message = '如果输入为：quit，则退出！\n'
	message += '请输入名字：'
	
	while True:
		add_string = raw_input(message) 
		if add_string == 'quit':
			break
		else:
			guest = 'Hello, ' + add_string.title() + '.\n'
			file_object.write(guest)
'''

#异常
#python		

#存储数据
#用户关闭程序时，我们几乎总是要保存他们提供的信息：
#一种简单的方式是使用模块json来存储数据


#使用json.dump()和json.load()
#import os
#import json
#使用函数json.dump()将数字列表存储到文件numbers.json中
'''
numbers = [1, 2, 4, 6, 9, 11, 15]

path = os.path.dirname(__file__)
print path
filename = path + '/test.txt'

with open(filename, 'r') as f_obj:
	contents = f_obj.readlines()
	print contents

filename = path + '/numbers.json'

with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)
'''

#使用json.load()将上面代码创建的number.json文件的这个列表读取到内存中
#import os
#import json
'''
path = os.path.dirname(__file__)
print path

filename = path + '/numbers.json'

with open(filename, 'r') as f_obj:
	numbers = json.load(f_obj)

print numbers
'''

#保存和读取用户生成的数据
#import os
#import json
'''
numbers = [1, 2, 4, 6, 9, 11, 15]

path = os.path.dirname(__file__)
print path
#filename = path + '/test.txt'

filename = 'test.txt'

with open(filename, 'r') as f_obj:
	contents = f_obj.readlines()
	print contents

#filename = path + '/numbers.json'
filename= 'numbers.json'

with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)	
	
path = os.path.dirname(__file__)
print path

filename = path + '/numbers.json'

with open(filename, 'r') as f_obj:
	numbers = json.load(f_obj)

print numbers
'''
	


#保存和读取用户生成的数据
#import os
#import json
'''
filename = 'username.json'               #这是 mac 中的用法

with open(filename, 'r') as f_obj:
	username = json.load(f_obj)
        print 'Welcome back, ' + username + '!'

username = raw_input('What is your name? ')


path = os.path.dirname(__file__)
print path
#filename = path + '/username.json'     #这是 windows 中 notepad 里用法
                                        #在 notepad 里运行的目录不是此文件的目录
                                        #而是 notepad 的程序目录

filename = 'username.json'              #这是 mac 中的用法
                                        #macvim 执行此行代码时，运行的目录是
                                        #此文件所在目录，因此可以用相对目录
                                        #但建议用绝对目录，这样就不怕移植所带来
                                        #不必要的麻烦

with open(filename, 'w') as f_obj:
	json.dump(username, f_obj)	
	print "We'll remember you when you come back, " + username + '!'


#filename = path + '/numbers.json'       #这是 windows 中 notepad 里用法
filename = 'username.json'               #这是 mac 中的用法

with open(filename, 'r') as f_obj:
	username = json.load(f_obj)
        print 'Welcome back, ' + username + '!'
'''


#from json
'''
filename = 'username.json'
try:
    with open(filename, 'r') as f_obj:
        username = json.load(f_obj)

except IOError:
    username = raw_input('What is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print "We'll remember you when you come back, " + username + '!'

else:
    print 'Welcome back, ' + username + '!'
'''

#重构

#import json
'''
def greet_user():
    #问候用户，并指出起名字
    filename = 'username.json'
    try:
        with open(filename, 'r') as f_obj:
            username = json.load(f_obj)

    except IOError:
        username = raw_input('What is your name? ')
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print "We'll remember you when you come back, " + username + '!'

    else:
        print 'Welcome back, '+ username + '!'

greet_user()
'''

#进一步细化，每个函数功能更加单一，具体
#import json
'''
def get_stored_username():
    # 如果存储了用户名，就获取它
    filename = 'username.json'
    try:
        with open(filename, 'r') as f_obj:
            username = json.load(f_obj)

    except IOError:
        return None

    else:
        return username

def get_new_username():
    # 提示用户输入用户名
    username = raw_input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    # 问候用户，并指出其名字
    username = get_stored_username()
    if username:
        print 'Welcome back, ' + username + '!'

    else:
        username = get_new_name()
        print "We'll remember you when you come back, " + username + '!'

greet_user()
'''
























