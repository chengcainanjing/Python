#coding=utf-8

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

'''		
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
'''