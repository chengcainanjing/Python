#coding=utf-8                                  
 
#====================
#File: oop_simplestclass.py
#Author: Cheng Cai
#Date: 2017-09-01
#====================
'''
#这是 python2版本
class Person:   #使用 class 语句来创建一个新类
    pass        #缩进语句块代表这个类的主体

p = Person()
print p
'''
'''
#这是python3版本
class Person:
    pass

p = Person()
print (p)
'''



'''
#oop_methon.py
#这是 python2版本
class Person:
    def say_hi(self):
        print 'Hello, how are you?'

p = Person()
p.say_hi()
#上面两行等于
#Person().say_hi()
'''
'''
#这是 python3版本
class Person:           #定义了个类
    def say_hi(self):   
    #这是类的方法 self 这种特殊的变量引用对象本身
    #使用 self 来引用同意对象的变量和方法，
    #这被称作属性引用attribnute reference
        print ('Hello, how are you?')

p = Person()            #Person 类下创建的实例 p
p.say_hi()
#上面两行等于
#Person().say_hi()
'''



'''
#oop_init.py
#这是 pyth0n2版本
class Person:
    def __init__(self, newPersonName):       #定义__init__方法来接受 newPersonName 参数
        self.name = newPersonName            #self.name 中的 name 是一个字段，后面的 newPersonName 是一个局部变量

    def say_hi(self):
        print 'Hello, my name is', self.name

p = Person('Chengcai')
p.say_hi()
#上面这两行可以写作
#Person('Swaroop').say_hi()
'''
'''
#这是 python3版本
class Person:
    def __init__(self, name):       #定义__init__方法来接受 name 参数
        self.name = name            #self.name 中的 name 是一个字段，后面的 name 是一个局部变量

    def say_hi(self):
        print ('Hello, my name is', self.name)

p = Person('Chengcai')
p.say_hi()
#上面这两行可以写作
#Person('Swaroop').say_hi()
'''




#oop_objvar.py
class Robot:
    population = 0
    #这是一个类变量，而不是对象变量
    #这个类变量在每个对象执行__init__方法时都会执行一遍，
    #而且是共用一个副本，它的值是累积的

    def __init__(self, newpersonname):
        self.name = newpersonname                #__init__函数中，正确的初始化实例变量
        print "(Initializing {})".format(self.name)

        Robot.population += 1
        #上面一行中的Robor.population
        #可以用self.__class__.poppulation来代替
        #每个对象都通过 self.__class__ 属性来引用他的类

    def die(self):
        print "{} is being destroyed!".format(self.name)

        Robot.population -= 1

        if Robot.population == 0:
            print "{} was the last one.".format(self.name)
        else:
            print "There are still {:d} robots working.".format(Robot.population)

    def say_hi(self):

        print "Greetings, my masters call me {}.".format(self.name)

    @classmethod
    def how_many(cls):
    #how_many  是类方法，不是对象方法
    #为它定义一个类方法（classmethod）
    #或是 staticmethod 静态方法
    #通常使用Decorator（装饰器）来将 how_many方法标记为类方法

        print "We have {:d} robots.".format(cls.population)

droid1 = Robot("R2-D2") 
#droid1是 Robot 类的一个实例
droid1.say_hi()
#实例后面加点后面的是方法，即是其他语言中的函数调用，
#方法的参数是 self，即是它本身，

Robot.how_many()
#从这里可以看出 how_many前面的是类本身而不是一个具体的对象，
#说明 how_many 对应的是类，不是对象

droid2 = Robot("C=3PO")
droid2.say_hi()
Robot.how_many()

print "\nRobots can do some work here.\n"

print "Robots have finished their work. So let's destroy them."
droid1.die()
droid2.die()

Robot.how_many()






































