#coding=utf-8
 
#====================
#File: Python编程从入门到实践.py
#Author: Cheng Cai
#Date: 2017-09-19
#====================
#import module_name

#from module_name import make_pizza as mp

#from module_car import Car

#from module_car import ElectricCar

#from module_car import Car,ElectricCar

#import module_car

#from module_car import Car
#from module_ElectricCar import ElectricCar

#from collections import OrderedDict

#from random import randint

#import os
#import json

'''
#字符串
string = 'This is a string'
print string

string = 'This is also a string'
print string

# 字符串中可以包含引号和撇号
string = 'I told my friend, "Python is my favourite language"'
print string

string = 'The language "Python" is named after Monty Python, not the snake'
print string

string = "One of Python's strengths is its diverse and supportive community."
print string

字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。
请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。
如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。

如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：

#'I\'m \"OK\"!'
表示的字符串内容是：

#I'm "OK"!
转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，
可以在Python的交互式命令行用print()打印字符串看看：

'''
>>> print('I\'m ok.')
I'm ok.
>>> print('I\'m learning\nPython.')
I'm learning
Python.
>>> print('\\\n\\')
\
\
'''

#你可能猜到了，%运算符就是用来格式化字符串的。
#在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
#如果只有一个%?，括号可以省略。

#常见的占位符有：

#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数
#其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

'''
>>> '%2d-%02d' % (3, 1)
' 3-01'
>>> '%.2f' % 3.1415926
'3.14'
'''
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

'''
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
'''

'''
>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
'''

#使用方法修改字符串大小写
name = "add lovelace"
print name.title()
#title() 方法以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写

print name.upper()
#upper()方法将字符串改为全部大写

print name.lower()
#lower()方法将字符串改为全部小写

#合并/拼接 字符串
first_name = "cheng"
last_name = "cai"
full_name = first_name + " " + last_name
print "Hello, " + full_name.title() + "!"
 
message =  "Hello, " + full_name.title() + "!"
print message

 
#制表符或者换行符来添加空白
print "Languages:\n\tPython\n\tC\n\tJavaScript"

#删除空白
favourite_language = 'python '
print favourite_language

print favourite_language.rstrip()
#rstrip方法表示删除字符串末尾空白，这种删除是暂时的，再次访问这个值时仍然有空白
#如果想要永久删除这个空白，需要将删除操作的结果存回到变量中
favourite_language = favourite_language.rstrip()
print favourite_language

#剔除开头的空白用 lstrip 方法，
#剔除字符串两边的空白用strip 方法
first_language = ' Python '
print first_language.lstrip()
print first_language.strip()

#数字
#整数
2 + 3
2 - 3

#注意在 python2中整数相除，
#只保留整数部分的数，而不是四舍五入
#所以，结果如果想有小数，则最少有一个操作数是浮点数
print 2 / 3
print 3 / 2
print 3.0 / 2
2 * 3

#两个*代表乘方运算
2 ** 3 
2 + 3*4 
(2 + 3) * 4

#浮点数
0.1 + 0.1   #0.2
2 * 0.1 #0.2

# 结果包含的小数位数可能是不确定的
print 0.2 + 0.1
print 2 * 0.1
 
#使用函数 str（）避免类型错误
#将整数用作字符串
age = 27
message = "Happy " + str(age) + "rd Brithday!"
print message

#变量引用
#一次赋多值
'''
v=('a', 'b', 'c')
(x, y, z) = v
#一一对应， x = 'a', y = 'b', z = 'c'
'''

#空值
#用None表示
#空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。






#列表(list)
#有一系列特定顺序排列的元素组成
#用方括号[] 表示列表，并用逗号来分隔其中的元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print bicycles

#访问列表元素
print bicycles[0]
print bicycles[1].title()
# 索引从0开始
#方括号中的数字：-1表示最后一个元素
print bicycles[-1].title()

names = ['chengcai', 'daiyumu', 'luwangpeng', 'wuyufei']
n = 0
while n <= 3:
    print 'Hello, {}! How are you?'.format(names[n]).title()
    n =n + 1
    print n

#修改列表元素
names[0] = 'caiyuntao'
print names

#在列表中添加元素
#在列表末尾添加元素
names.append('chengcai')
print names

#在列表中插入元素
#insert 方法可以在列表的任何位置插入元素
names.insert(1, 'panqiaoxu')
print names

# extend (扩展) 与 append (追加) 的差别
'''
>>> li = ['a', 'b', 'c']
>>> li.extend(['d', 'e', 'f']) 1
>>> li
['a', 'b', 'c', 'd', 'e', 'f']
>>> len(li)                    2
6
>>> li[-1]
'f'
>>> li = ['a', 'b', 'c']
>>> li.append(['d', 'e', 'f']) 3
>>> li
['a', 'b', 'c', ['d', 'e', 'f']]
>>> len(li)                    4
4
>>> li[-1]
['d', 'e', 'f']

1Lists 的两个方法 extend 和 append 看起来类似，但实际上完全不同。
extend 接受一个参数，这个参数总是一个 list，
并且把这个 list 中的每个元素添加到原 list 中。
2在这里 list 中有 3 个元素 ('a'、'b' 和 'c')，
并且使用另一个有 3 个元素 ('d'、'e' 和 'f') 的 list 扩展之，
因此新的 list 中有 6 个元素。
3另一方面，append 接受一个参数，这个参数可以是任何数据类型，
并且简单地追加到 list 的尾部。
在这里使用一个含有 3 个元素的 list 参数调用 append 方法。
4原来包含 3 个元素的 list 现在包含 4 个元素。
为什么是 4 个元素呢？因为刚刚追加的最后一个元素本身是个 list。
List 可以包含任何类型的数据，也包括其他的 list。这或许是您所要的结果，或许不是。
如果您的意图是 extend，请不要使用 append。
'''

#在列表中链接列表
names.extend(['two', 'one'])

'''
>>>names
['chengcai', 'daiyumu', 'luwangpeng', 'wuyufei', 'two', 'one']
'''

#从列表中删除元素
#使用 del 语句来删除元素
del names[5]
print names

#使用 pop 方法删除元素
#pop方法可以删除列表末尾的元素,并且可以接着使用这个被删除的元素
#被删除的元素之后，原来的列表中就不包含被删除的元素了
del_name = names.pop()
print del_name
print names

#对于 del 语句和pop 方式删除元素的区别
#删除后，不在使用被删除的元素，建议使用 del 语句
#如果使用被删除的元素，使用 pop 方法

#根据值删除元素
#使用 remove 方法
names.remove('caiyuntao')
print names
#注意，该方法只能删除第一个指定的值，如果需要删除的值，多次出现，需要多次删除

#运算符
'''
>>> li = ['a', 'b', 'mpilgrim']
>>> li = li + ['example', 'new'] 1
>>> li
['a', 'b', 'mpilgrim', 'example', 'new']
>>> li += ['two']                2
>>> li
['a', 'b', 'mpilgrim', 'example', 'new', 'two']
>>> li = [1, 2] * 3              3
>>> li
[1, 2, 1, 2, 1, 2]
1 Lists 也可以用 + 运算符连接起来。
list = list + otherlist 相当于 list.extend(otherlist)。
但 + 运算符把一个新 (连接后) 的 list 作为值返回，而 extend 只修改存在的 list。
也就是说，对于大型 list 来说，extend 的执行速度要快一些。
2 Python 支持 += 运算符。li += ['two'] 等同于 li.extend(['two'])。
+= 运算符可用于 list、字符串和整数，并且它也可以被重载用于用户自定义的类中 。
3 * 运算符可以作为一个重复器作用于 list。
li = [1, 2] * 3 等同于 li = [1, 2] + [1, 2] + [1, 2]，即将三个 list 连接成一个。
'''

# 组织列表
# 使用方法 sort（）对列表进行永久性排序,且是按照字母顺序排列
cars = ['bmw', 'audi', 'toyota', 'subaru']
print "\nHere is the original list: "
print cars

cars.sort()
print "\nHere is the sort list: "
print cars

#排列按字母表顺序相反的顺序排列
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print "\nHere is the sort and reversed list: "
print cars
 
#使用 sorted() 对列表进行临时排序
#sorted() 方法能够按特定的顺序显示列表元素，
#同时不影响他们在列表中的原始排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']

print "\nHere is the original list: "
print cars

print "\nHere is the sorted list: "
print sorted(cars)

#倒着导引列表
#如果想要按与字母顺序相反的顺序显示列表，
#可向函数sorted()传递参数reverse=True
print "\nHere is the reverse=True list: "
print sorted(cars, reverse = True)

# 反列表元素排列顺序，使用方法 reverse（）
#但 reverse（）不是指按与字母顺序相反的顺序排列列表元素
#只是反转列表元素的排列顺序
#方法 reverse（）永久性地修改列表元素的排列顺序
#但可随时恢复到原来的品牌列顺序
#只需要对列表再次调用 reverse（）即可
print "\nHere is the reverse list: "
cars.reverse()
print cars
print "\nHere is the original lise: "
print "\nLook the list which is original or not: "
cars.reverse()
print cars

#确定列表的长度
#使用函数len()
print "\nthe length of the list: "
print len(cars)

#遍历列表
#for循环,注意缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print magician

for magician in magicians:
    print magician.title()+", that was a great trick!"
    print "I can't wait to see your next trick, " + magician.title() + ".\n"
	
print "Thank you, everyone. That was a great magic show!"
	
#创建数值列表
#range()函数生成一系列数字,从第一个数开始，到达第二个数值时停止，但不输出第二个数
for value in range(1, 5):
	print value

#list()函数将range()函数作为参数
#list()函数将数字转换为一个列表
numbers = list(range(1, 5))
print numbers

#range()函数还可以指定步长
numbers = list(range(2, 11, 2))
print numbers

#创建一个列表，遍历1到10的平方
#方法1
squares = []
for value in range(1, 11):
	square = value**2
	squares.append(square)

print squares

#方法2
squares = []
for value in range(1, 11):
	squares.append(value**2)
	
print squares

#对数字列表执行简单的统计计算
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print min(digits)
print max(digits)
print sum(digits)

#列表解析
squares = [value**2 for value in range(1, 11)]
print squares

#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print "\n前三个元素是：{}".format(players[0:3])
print "\n第二个元素到第四个元素是：{}".format(players[1:4])
#不指定第一个索引，Python 自动从列表开头开始
print "\n前四个元素是：{}".format(players[:4])    
#不指定第二个索引，Python 自动索引到最后一个元素，并且输出最后一个元素
print "\n第二个元素到最后一个元素是：{}".format(players[1:])
#第一个索引从倒数第三个元素开始
print "\n倒数第三个元素到最后一个元素是：{}".format(players[-3:])

#遍历切片

print "\nHere is all people in my team:"

for player in players[:]:
    print player.title()


#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
#这一步是切片，复制整个列表给另一个新列表，原列表不变
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print '\nMy favourite foods are:'
print my_foods

#新列表添加新的元素，与原列表不影响，无冲突
print '\nMy friend favourite foods are:'
print friend_foods
 
#下面这一步不同于上面的切片方法，这是直接将原列表赋给新列表，
#而不是把 my_foods 的副本 存储到 friend_foods
#这种语法实际上是让python将新变量 friend_foods 关联到包含在my_foods 中的列表
#因此这两个变量指向同一个列表
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print '\nMy favourite foods are:'
print my_foods

#新列表添加新的元素，与原列表不影响，无冲突
print '\nMy friend favourite foods are:'
print friend_foods
 
#元组(tuple)
#不可以修改元素，列表可以修改元素
# 元组是用圆括号来定义
dimensions = (200, 50)
print dimensions[0]
print dimensions[1]

#修改元组内的某个元素是不可能的，会显示报错
#dimensions[0] = 50
#print dimensions[0]
#遍历元组内所有元素
for dimension in dimensions:
    print dimension

#虽然元组的元素不可以改变，
#但是存储元组的变量是可以被修改的
print '\nOriginal dimensions:'
for dimension in dimensions:
    print dimension

dimensions = (410, 100)
print '\nModified dimensions:'
for dimension in dimensions:
    print dimension

#字典（dictionary）
#字典是一系列建--值对
#每个键都与一个值相关联
#字典用花括号将一系列的键--值对表示
alien_0 = {'color':'green','points':5}
print alien_0['color']
print alien_0['points']

#赋值给新的变量
new_points = alien_0['points']
print "\nYou just earned" + str(new_points) + "points.\n"

#添加键-值对
#字典是一种动态结构
#可随时在其中添加键-值对
print alien_0

#如何添加键-值
alien_0['x_position'] = 0
alien_0['y_position'] = 50
print alien_0




#遇事冷静，礼让三分
#情绪稳定，思维清晰时，做判断；相反时，不要做任何决定
#做事别冲动，退一步海阔天空
#对人对事，有耐心，要细心，持爱心
#每天起来笑一笑，想一件快乐、开心的事
#不开心的事总会过去，开心的事都会留下美好回忆
#常挂笑容在嘴边，对人多笑笑



#字典
#字典是一系列建--值对
#每个键都与一个值相关联
#字典用花括号将一系列的键--值对表示
alien_0 = {'color':'green','points':5}
print alien_0['color']
print alien_0['points']

#赋值给新的变量
new_points = alien_0['points']
print "\nYou just earned" + str(new_points) + "points.\n"

#添加键-值对
#字典是一种动态结构
#可随时在其中添加键-值对
print alien_0

#如何添加键-值
alien_0['x_position'] = 0
alien_0['y_position'] = 50
print alien_0

#创建一个空字典
alien_1 = {}
alien_1['color'] = "blue"
alien_1['points'] = 10
print alien_1

#修改字典中的值
alien_1['color'] = 'yellow'
print "\nThe alien is now " + alien_1["color"] + "."

alien_1 = {'x_position':0,'y_position':50,'speed':'medium'}
print "\nOriginal x_position: " + str(alien_1['x_position'])

if alien_1['speed'] == 'slow':
	x_increment = 1
elif alien_1['speed'] == 'medium':
	x_increment = 2
elif alien_1['speed'] == 'fast':
	x_increment = 3

#新位置等于老位置加上增量
alien_1['x_position'] = alien_1['x_position'] + x_increment
print "\nNew x_position: " + str(alien_1['x_position'])

'''
#要避免key不存在的错误，有两种办法，
#一是通过in判断key是否存在：

>>> 'Thomas' in d
False
二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：

>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
注意：返回None的时候Python的交互式命令行不显示结果。
'''

#删除键-值对
#可使用del语句
#使用时必须指定字典名和要删除的键
alien_0 = {'color':'green','points':5}
print alien_0

#单独删除一个键值对
del alien_0['points']
print alien_0

#删除一个key也可使用pop(key)，对应的value也会被删除
alien_0['color']
print alien_0

#删除所有键值对
'''
alien_0.clear()
>>>alien_0
{}
'''

#由类似对象组成的字典
favorite_languages = {'jen':'python',
					'sarah':'C',
					'edward':'ruby',
					'phil':'python'					
					}

print "Sarah's favorite language is " + favorite_languages['sarah'].title() + '.'

#存储一个熟人
my_girlfriend = {}
my_girlfriend['first_name'] = 'Jin'
my_girlfriend['last_name'] = 'Lei'
my_girlfriend['age'] = 27
my_girlfriend['city'] = 'nanjing'
print my_girlfriend

#遍历字典
user_0 = {'username':'zhanzhi',
		'first_name':'jin',
		'last_name':'lei'
		}

for key,value in user_0.items():
	print '\nkey: ' + key
	print 'value: ' + value
	
#注意即使遍历整个字典时，键-值对的返回顺序也与存储顺序不同，python不关心键-值对的存储顺序，
#而只跟踪键和值之间的关联关系
favorite_languages = {'jen':'python',
					'sarah':'C',
					'edward':'ruby',
					'phil':'python'					
					}

#方法 item（）返回一个键-值对列表
for name,language in favorite_languages.items():
	print name.title() + "'s favorite language is " + language.title() + "."

#遍历所有的键
for name in favorite_languages.keys():
	print name.title()
	
#遍历字典时，默认遍历所有的键，因此上面的for循环可以等于
friends = ['phil', 'sarah']
for name in favorite_languages:
	print name.title()
	
	if name in friends:
	    print "Hi, " + name.title() +\
                        ", I see your favorite language is " +\
                        favorite_languages[name].title() + "!"

        if 'erin' not in favorite_languages.keys():
            print '\nErin, please take our poll!\n'
            
#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print name.title() + ", thank you for taking the poll.\n"

# 遍历字典中所有值
print 'The following languages have been mentioned:'
for language in favorite_languages.values():
    print language.title()

#为了剔除重复项，可用集合set()
print '\nThe following languages have been mentioned:'
for language in set(favorite_languages.values()):
    print language.title()

'''
和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
'''



# 嵌套
#将一系列字典存储在列表中，或
#将一系列列表存储在字典中
#等等

#字典列表
alien_0 = {'color':'yellow', 'speed':'low', 'points':'5'}
alien_1 = {'color':'blue', 'speed':'low', 'points':'5'}
alien_2 = {'color':'red', 'speed':'low', 'points':'5'}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print alien

#自动生成外星人
#使用range()
#先创建一个空列表
aliens= []

#使用随机函数range（）来创建三十个外星人
for alien_number in range(30):
    new_alien = {'color':'blue', 'speed':'low', 'points':5}
    aliens.append(new_alien)

# 将前三个外星人颜色修改为黄色，速度为中等，值为10
for alien in aliens[:3]:
    if alien['color'] == 'blue':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print '\nThe first fifth aliens of all:'
for alien in aliens[:5]:
    print alien
print '...'

print 'Total number of aliens: ' + str(len(aliens))

#在字典中存储列表
pizza = {
		'crust':'thick',
		'toppings':['mushroom','extra cheese'],
		}

print "You ordered a " + pizza['crust'] + "-crust pizza " + \
	"with the following toppings: "

for topping in pizza['toppings']:
	print '\t' + topping

#2017.09.13	
#每当需要在字典中将一个键关联到多个值时，
#可以在字典中嵌套一个列表
favorite_languages = {
					'jen':['python','ruby'],
					'sarah':['c','python'],
					'edward':['ruby','c'],
					'phil':['python','c'],
					}
	
for names,languages in favorite_languages.items():
	print  '\n' + name.title() + "'s favorite languages are: "
	for language in languages:
		print '\t' + language.title()
		
#字典中嵌套字典
users = {'aeinsten':{'first':'albert', 'last':'einstein', 'location':'princeton'},
		'mcurie':{'first':'marie', 'last':'curie', 'location':'paris'},
		}

#输出一系列键-值对
for username,user_info in users.items():
	print '\nUsername:' + username
	full_name = user_info['first'] + ' ' +user_info['last']
	location = user_info['location']
	
	print '\tFull name: ' + full_name.title()
	print '\tLocation: ' + location.title()

#分开输出键与值
for username in users.keys():
	print 'Username: ' + username
	
for user_info in users.values():
	print '\tFull_name: ' + user_info['first'].title() + ' ' \
				+ user_info['last'].title()
	print '\tLocation :' + user_info['location'].title()
	
#6-7
person_0 = {'first_name':'zeng', 'last_name':'xiaoxian', 'age':18, 'location':'shanghai'}
person_1 = {'first_name':'hu', 'last_name':'yifei', 'age':18, 'location':'shanghai'}
person_2 = {'first_name':'lv', 'last_name':'ziqiao', 'age':18, 'location':'shanghai'}

people = [person_0, person_1, person_2]

for person in people:
	#简单方法打印所有人员信息
	#print '\n'+ str(person)
	
	#详细方法打印所有人员信息
	full_name = person['first_name'] + ' ' + person['last_name']
	print full_name.title() + ' is ' + str(person['age']) + ' old, and lives in '\
			+ person['location'].title() + '.'
	
#6-8
pet_0 = {'dog':{'age':3, 'master':'zengxiaoxian'}}
pet_1 = {'cat':{'age':2, 'master':'songmeijia'}}
pet_2 = {'monkey':{'age':4, 'master':'zhangwei'}}

pets = [pet_0, pet_1, pet_2]
#第一个for循环针对的是列表
#第二个for循环针对的是字典，需要for循环是因为字典内嵌套字典
for pet in pets:
	for pet_name,pet_info in pet.items():
	
		print '\n' + pet_info['master'].title() + "'s pet is " + pet_name \
					+ ' and the age is ' + str(pet_info['age'])
	
#如果pet_0等三个字典中不嵌套时，代码如下
pet_0 = {'age':3, 'master':'zengxiaoxian'}
pet_1 = {'age':2, 'master':'songmeijia'}
pet_2 = {'age':4, 'master':'zhangwei'}

pets = [pet_0, pet_1, pet_2]
for pet in pets:
	print pet['master'].title() + "'s pet is " + str(pet['age']) \
			+ ' years old.'

#6-9
#列表字典
favorite_places = {
				'zengxiaoxian':['shanghai', 'beijing', 'beihaidao'],
				'huyifei':['beijing', 'xian', 'nanjing'],
				'lvziqiao':['nanjing', 'suzhou', 'dalian'],
				}

for name,places in sorted(favorite_places.items()):
	print name.title() + "'s favorite palces are : "
	for place in sorted(places):
		print '\t' + place.title()

#6-10
#字典列表
person_0 = {'name':'zengxiaoxian', 'number':[2,5,8]}
person_1 = {'name':'lvziqiao', 'number':[10,50,18]}
person_2 = {'name':'zhangwei', 'number':[21,52,84]}

people = [person_0, person_1, person_2]

for person in people:
	print '\nName :' + person['name'].title() + '\nFavorite number: ' 
	for number in person['number']:
			print '\t' + str(number)
'''
#个人感悟
#列表、字典、字典列表、列表字典、字典字典
#无论在如何复杂，字典必包含一系列键-值对，键都是一个值
#但是值可以是任何形式，可以是单个字符串、单个数字、列表、字典
#我们在使用的时候，本质是调用的属性，例如：列表的属性、字典的属性
#在操作时，仅仅是将这些属性综合起来运用而已
#在调用列表所有属性对值进行操作，
#从字典中提取值一定要注意它的形式
		

#用户输入
'''
message = raw_input("Tell me something, and I'll repeat it back to you: ")
print message

name = raw_input("Please inter your name:")
print "Hello, " + name.title() + "!"

prompt = "If you tell us who are you, we can personalize the message you see."
prompt = "\nWhat is your first name?"

name = raw_input(prompt)
print '\nHello, ' + name.title()
'''

#raw_input输入的字符，系统将它看作字符串，
#如果想要与整数做比较，需要进行数据类型转换int()
'''
height = raw_input("How tall are you, in inches?")
height = int(height)

if height >= 36:
	print "\nYou're tall enough to ride!"	
else:
	print("\nYou'll be able to ride when you're a little older.")
'''

#求模运算符
#求模运算符不会指出一个数是另一个数的多少倍，而只指出余数是多少
#4%3 >>>1
#5%3 >>>1
#6%3 >>>0
'''
number = raw_input("Enter a number, and I will tell you if it's even or odd:")
number_0 = int(number)

if number_0 % 2 == 0:
	print "\nThe number " + number + ' is even.'
else:
	print "\nThe number " + number + ' is odd.'
'''

#while循环
#使用标志，判断整个程序是否处于活动状态
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
active =True
#while 语句可以如下局判断，也可以用active 来做判断
#while message != 'quit':
while active:
    message = raw_input(prompt)

    if message == 'quit':
        active = False
    else:
        print message
'''

'''
#使用 break 退出循环
prompt = '\nPlease enter the name of a city you have visited:'
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = raw_input(prompt)

    if city == 'quit':
        break
    else:
        print "I'd love to go to " + city.title() + "!"

#在循环中使用 continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print current_number
'''

#2017.09.14
#使用while循环来处理列表和字典
'''
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print 'Verifying user:' + current_user
	confirmed_users.insert(1, current_user)
	
print '\nThe following users have been confirmed: '
for confirmed_user in sorted(confirmed_users):
	print confirmed_user.title()
'''

#删除包含特定值得所有列表元素
'''
pets = ['cats', 'dogs', 'monkeys', 'goldlishes', 'rabbits', 'pigs']
while 'cats' in pets:
	pets.remove('cats')
	
print '\n' + str(pets)
'''

'''
#使用用户输入来填充字典
responses = {}
polling_active = True

while polling_active:
	name = raw_input('\nWhat is your name?')
	response = raw_input('Which mountain would you like to climb someday?')

	#注意下一步是将字典中的键与值一一对应的
	responses[name] = response
	
	repeat = raw_input('Would you like to let another person respond? (yes/no)')
	if repeat == 'no' or repeat == 'n':
		polling_active = False

print '\n---Poll Results---'
#注意：对于字典，print输出时，不能使用是sorted()函数，
#使用后字典仅显示键，不显示值
#print sorted(responses)	#这个显示的是键，对键排序，不显示值
#下面一行代码显示键-值对
print responses
#在for循环中，针对键-值对的循环，可以使用sorted()
for name,response in sorted(responses.items()):
	print name + 'would like to climb '+ response + '.'
'''

#函数 
#函数是带名字的代码块
'''
def greet_user():
	print ('Hello')
	
greet_user()
'''

#向函数体传递信息
#定义一个函数带参数
'''
def greet_user(username):
	print 'Hello, ' + username.title() + '.'

greet_user('zengxiaoxian')
'''

#实参与形参
#上面函数greet_user()中username是一个形参
#形参——函数完成其工作所需的一项信息
#在代码greet_user('zengxiaoxian')中，
#值'zengxiaoxian'是一个实参
#实参——调用函数时传递给函数的信息
#在greet_user('zengxiaoxian')中，
#将实参'zengxiaoxian'传递给了函数greet_user()
#这个值被存在形参username中

#位置实参
#调用函数时，将函数调用中的每一个实参都关联到函数定义中的一个形参
#为此，最简单的关联方式是基于实参的顺序
'''
def describe_pet(animal_type, pet_name):
	print '\nI have a ' + animal_type + '.'
	print 'My ' +animal_type + "'s name is " + pet_name.title() + '.'

describe_pet('hamster','harry')
describe_pet('dog','willie')
'''
'''
#实参传递时，调换前后顺序，查看形参是否按顺序输出
def describe_pet(animal_type, pet_name):
	print '\nI have a ' + animal_type + '.'
	print 'My ' +animal_type + "'s name is " + pet_name.title() + '.'

describe_pet('harry','hamster')
describe_pet('willie','dog')
#输出结果按实参传递给形参的顺序输出
'''

#关键字实参
#其是传递给函数的名称-值对
#在实参中将名称与值关联起来
#因此向函数传递实参时不会混淆（不会出现上面的情况）
#关键字实参让我们无需考虑函数调用中实参顺序
#还可以清楚的指出函数调用中的各个值的用途
'''
def describe_pet(animal_type, pet_name):
	print '\nI have a ' + animal_type + '.'
	print 'My ' +animal_type + "'s name is " + pet_name.title() + '.'

describe_pet(pet_name = 'harry', animal_type = 'hamster')
'''
	
#默认值
'''
def describe_pet(pet_name, animal_type = 'dog'):
	print '\nI have a ' + animal_type + '.'
	print 'My ' +animal_type + "'s name is " + pet_name.title() + '.'

describe_pet('harry')
'''
#注意： 在这个函数中，修改了形参的排列顺序
#由于给animal_type指定了默认值，无需通过实参来指定动物类型，
#因此在函数调用中只包含一个实参--pet_name
#但是，python仍然将这个实参视为位置实参，
#因此，如果函数调用中只包含宠物名字，
#这个实参将关联到函数定义的第一个形参
#这就需要将pet_name放到形参列表开头的原因所在

#如果显式的给naminal_type提供实参，
#python忽略这个形参的默认值
'''
def describe_pet(pet_name, animal_type = 'dog'):
	print '\nI have a ' + animal_type + '.'
	print 'My ' +animal_type + "'s name is " + pet_name.title() + '.'

describe_pet(pet_name = 'harry', animal_type = 'hamster')
'''

#返回值
#返回简单值
'''
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name('jimi', 'hendrix')
print musician
'''

#让实参变成可选的
'''
def get_formatted_name(first_name, last_name, middle_name = ''):
	#python将非空字符串解读为True
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name('jimi', 'hendrix')
print musician

musician = get_formatted_name('Geng', 'xue', 'chang')
print musician
'''

#返回字典
'''
def build_person(first_name, last_name, age = ''):
	person = {'first_name':first_name,'last_name':last_name}
	if age:
		person['age'] = age
	
	return person

musician = build_person('zeng', 'xiaoxian', '5')
print musician
'''

#结合使用函数和while循环
'''
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print '\nPlease tell me your name: '
	print "Enter 'q' at any time to quit"

	f_name = raw_input('First_name: ')
	if f_name == 'q':
		break
		
	l_name = raw_input('Last_name: ')
	if l_name == 'q':
		break
	
	formatted_name = get_formatted_name(f_name, l_name)
	
	print '\nHello, ' + formatted_name.title()
	
            quit = raw_input('\nDO you want to quit?(yes/no)')
            if quit == 'yes':
                    break
'''

#test
#8-6
'''
def city_country(city, country):
            full_format = city.title() + ', ' + country.title()
            return full_format
            
get_formatted_city_0 = city_country('chengdu', 'china')
get_formatted_city_1 = city_country('new_york', 'usa')
get_formatted_city_2 = city_country('yokoto', 'japan')
get_formatted_citys = [get_formatted_city_0, get_formatted_city_1, get_formatted_city_2]	
print get_formatted_citys
#方法2
def city_country(city, country):
        print city.title()+ ', ' + country.title()
            
city_country('chengdu', 'china')
city_country('newyork', 'usa')
city_country('toyoto', 'japan')
'''

#8-7
'''
def make_album(songer, album_name, album_number=''):
        song_info = {'songer': songer, 'album_name':album_name}
        if album_number:
                song_info['album_name'] = album_number
        print song_info

make_album('liuhuan', 'dahexiangdongliu', '8')
make_album('liudehua', 'benxiaohai', '12')
make_album('zhangxueyou', 'yiqie')
'''

#传递函数
'''
def greet_users(users_name):
    names = users_name[:]
    while names:
        current_user = names.pop()
        print 'Hello, ' + current_user + '!'

users_name = ['zengxiaoxian', 'huyifei', 'zhangwei']
greet_users(users_name)
print users_name

# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print 'Printing model: ' + current_design
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print '\nThe following models have been printed: '
    for completed_model in completed_models:
        print completed_model

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
'''

#禁止函数修改列表
#function_name(list_name[:])
#这实参表示将列表的副本传递给函数，而不是实参传递的本身
#保证了实参本身的原本性
#print_models(unprinted_models[:], completed_models)

#2017.09.15
#传递任意数量的实参
'''
def make_pizza(*toppings):
	print toppings
	
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''
#形参名×toppings中的星号让python创建一个名为toppings的空元组
#将收集来的所有值都封装在这个元组中

#将print语句替换为一个循环
'''
def make_pizza(*toppings):
	print '\nMaking a pizza with the following toppings: '
	for topping in toppings:
		print '-' + topping

make_pizza('pepperroni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''

#结合使用位置实参和任意数量实参
#让函数接受不同类型的实参
#必须在函数定义中将接纳任意数量实参的形参放在最后
#python先匹配位置实参和关键字实参，最后剩下来的都给最后一个形参
'''
def make_pizza(size, *toppings):
	print '\nMaking a ' + str(size) + '-inch pizza with following toppings:'
	for topping in toppings:
		print '- ' + topping
		
make_pizza(16, 'mushrooms')
make_pizza(32, 'pepperroni', 'green peppers', 'extra cheese')
'''

#使用任意数量的关键字实参
#事先不清楚传递给函数的会是什么样的信息
#这情况下，可以将函数编写成接受任意数量的键-值对
'''
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('zeng', 'xiaoxian', location = 'shanghai', field = 'star')
print user_profile
'''
#函数中形参**user_profile的两个星号代表
#让python创建一个名为user_info的空字典
	
#感悟
#在传递函数参数时，
#形参前面有一个*代表元组，实参是一系列的元素，传递给形参
#形参前面有两个**代表字典，实参是一系列的键值对，传递给形参

#test
#8-12
'''
def make_pizza(*toppings):
	print '\nMaking sangwich with the following toppings: '
	for topping in toppings:
		print '-' + topping
		
make_pizza('rice')
make_pizza('wirte', 'milk', 'pepperoni')
'''

#8-14
'''
def build_info(maker, type, **car_info):
	profile = {}
	profile['car_maker'] = maker
	profile['car_type'] = type
	for key, value in car_info.items():
		profile[key] = value
	
	return profile
	
car_profile = build_info('bmw', '310', location = 'germon', price = '350000')
print car_profile
'''
#注意**car_info中的键值对的使用，
#propile[key] = value 
#其中key是不需要加单引号的
#alue也不需要加单引号

#第二种表示
'''
def build_info(maker, type, **car_info):
	car_info['car_maker'] = maker
	car_info['car_type'] = type

	return car_info
	
car_profile = build_info('bmw', '310', location = 'germon', price = '350000')
print car_profile
'''
#第二种方式更为简洁，函数中没有创建新的字典，直接用**car_info

#将函数存储在模块中

#函数的优点之一：将主程序和代码分开
#通过函数指定描述性名称，可让主程序容易理解很多
#更进一步的话，将函数存储在被称为模块的独立文件中
#再将模块导入到主程序中
#import语句允许在当前运行的程序文件中使用模块的代码

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
		#初始化描述汽车的属性
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

		
		




