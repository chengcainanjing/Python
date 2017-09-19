#coding=utf-8

import os
import json


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

























