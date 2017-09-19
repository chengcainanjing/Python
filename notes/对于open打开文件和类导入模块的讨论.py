#coding=utf-8

import os

#print os.getcwd() #显示当前工作目录
#在notepad++中,打开文件后显示的是notepad++所在的程序目录
#在python2.7IDLE中显示的是此文件所在的文件夹目录
#对于类的导入，可在此文件所在的文件夹中搜索对应的模块，
#而在下面代码中,open()不可以搜索对应的文件夹
#具体的细节不了解，存在疑问???
#下面代码，报错：
#IOError:[Errno 2] No such file or directory: 'digit.txt'
'''
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
