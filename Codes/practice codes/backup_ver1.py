#coding=utf-8                                  
 
#====================
#File: backup_ver1.py
#Author: Cheng Cai
#Date: 2017-08-31
#====================

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
target = target_dir + os.sep + \
        time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)    #

zip_command = 'zip -r {0} {1}'.format(target,
                                    ' '.join(source))

print 'Zip command is:'
print zip_command
print 'Running:'
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'


