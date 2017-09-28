
#coding=utf-8                                  
 
#====================
#File: backup_ver3.py
#Author: Cheng Cai
#Date: 2017-09-01
#====================
'''
#python3版本
import os
import time

#1需要备份的文件
source = ['/Users/chengcai/Documents/GitHub/notes']

#2备份文件在此目录下
target_dir = '/Users/chengcai/Documents/GitHub/backup'

#3备份文件打包压缩程 zip 文件
#4zip 压缩文件的文件名由当前日期与时间构成
#os.sep 变量的使用——将根据自己的操作系统给出相应的分隔符，
#在 GUN/Linux 与 Unix中它是‘/’，在 windows 中它是'\\'，
#在 mscos 中它会是':'，
#+号运算符来创建目标 zip 文件的文件名
#将两个字符串连接成一个新的字符串
today = target_dir + os.sep +time.strftime('%Y%m%d')
#将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')

#添加一条来自用户的注释以创建
#zip 文件的文件名
comment = input('Enter a comment -->')

#检验是否有评论键入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
            comment.replace(' ', '_') + '.zip'
            
#如果子目录尚不存在则创建一个
if not os.path.exists (today):
    os.mkdir(today)    
    print ('Successfully created directory', today)

#5使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target,
                                    ' '.join(source))
#运行备份
print ('Zip command is:')
print (zip_command)
print ('Running:')
if os.system(zip_command) == 0:
    print ('Successful backup to', target)
else:
    print ('Backup FAILED')
'''


#python2版本
import os
import time

#1需要备份的文件
source = ['/Users/chengcai/Documents/GitHub/notes']

#2备份文件在此目录下
target_dir = '/Users/chengcai/Documents/GitHub/backup'

#3备份文件打包压缩程 zip 文件
#4zip 压缩文件的文件名由当前日期与时间构成
#os.sep 变量的使用——将根据自己的操作系统给出相应的分隔符，
#在 GUN/Linux 与 Unix中它是‘/’，在 windows 中它是'\\'，
#在 mscos 中它会是':'，
#+号运算符来创建目标 zip 文件的文件名
#将两个字符串连接成一个新的字符串
today = target_dir + os.sep +time.strftime('%Y%m%d')
#将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')

#添加一条来自用户的注释以创建
#zip 文件的文件名
comment = raw_input('Enter a comment -->')
# 下面这行代码也可以运行，但是注意在输入字符串时要加上双引号或者单引号
#comment = input('Enter a comment -->')
#http://www.cnblogs.com/gengcx/p/6707024.html
# 这地址说明了 Python2中 input（）、raw_input()与 Python3中 input（）的区别


#检验是否有评论键入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
            comment.replace(' ', '_') + '.zip'
            
#如果子目录尚不存在则创建一个
if not os.path.exists (today):
    os.mkdir(today)    
    print 'Successfully created directory', today

#5使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target,
                                    ' '.join(source))
#运行备份
print 'Zip command is:'
print zip_command
print 'Running:'
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'


