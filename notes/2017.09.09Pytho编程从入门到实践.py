#coding=utf-8
 
#====================
#File: Python编程从入门到实践.py
#Author: Cheng Cai
#Date: 2017-09-09
#====================

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

#列表
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

# 组织列表
#使用方法 sort（）对列表进行永久性排序,且是按照字母顺序排列
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
 
#元组
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

#删除键-值对
#可使用del语句
#使用时必须指定字典名和要删除的键
alien_0 = {'color':'green','points':5}
print alien_0

del alien_0['points']
print alien_0

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

#个人感悟
#列表、字典、字典列表、列表字典、字典字典
#无论在如何复杂，字典必包含一系列键-值对，键都是一个值
#但是值可以是任何形式，可以是单个字符串、单个数字、列表、字典
#我们在使用的时候，本质是调用的属性，例如：列表的属性、字典的属性
#在操作时，仅仅是将这些属性综合起来运用而已
#在调用列表所有属性对值进行操作，
#从字典中提取值一定要注意它的形式
		

#用户输入
message = raw_input("Tell me something, and I'll repeat it back to you: ")
print message

name = raw_input("Please inter your name:")
print "Hello, " + name.title() + "!"

prompt = "If you tell us who are you, we can personalize the message you see."
prompt = "\nWhat is your first name?"

name = raw_input(prompt)
print '\nHello, ' + name.title()

#raw_input输入的字符，系统将它看作字符串，
#如果想要与整数做比较，需要进行数据类型转换int()
height = raw_input("How tall are you, in inches?")
height = int(height)

if height >= 36:
	print "\nYou're tall enough to ride!"	
else:
	print("\nYou'll be able to ride when you're a little older.")

#求模运算符
#求模运算符不会指出一个数是另一个数的多少倍，而只指出余数是多少
#4%3 >>>1
#5%3 >>>1
#6%3 >>>0
number = raw_input("Enter a number, and I will tell you if it's even or odd:")
number_0 = int(number)

if number_0 % 2 == 0:
	print "\nThe number " + number + ' is even.'
else:
	print "\nThe number " + number + ' is odd.'
	
#while循环
#使用标志，判断整个程序是否处于活动状态
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

#2017.09.14
#使用while循环来处理列表和字典
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print 'Verifying user:' + current_user
	confirmed_users.insert(1, current_user)
	
print '\nThe following users have been confirmed: '
for confirmed_user in sorted(confirmed_users):
	print confirmed_user.title()

#删除包含特定值得所有列表元素
pets = ['cats', 'dogs', 'monkeys', 'goldlishes', 'rabbits', 'pigs']
while 'cats' in pets:
	pets.remove('cats')
	
print '\n' + str(pets)

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
def greet_user():
	print ('Hello')
	
greet_user()

#向函数体传递信息
#定义一个函数带参数
def greet_user(username):
	print 'Hello, ' + username.title() + '.'

greet_user('zengxiaoxian')
	
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
def greet_user(users_name):
	while users_name:
		current_user  = users_name.pop()
		print 'Hello, ' + current_user + '!'

users_name = ['zengxiaoxian', 'huyifei', 'zhangwei']































