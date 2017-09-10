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


