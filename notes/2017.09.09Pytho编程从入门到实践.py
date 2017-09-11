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
























