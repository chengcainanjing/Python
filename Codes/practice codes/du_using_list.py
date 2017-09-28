#coding=utf-8                                  

 
#====================
#File: du_using_list.py
#Author: Cheng Cai
#Date: 2017-08-30
#====================
 
#下面两个代码唯一的区别就在于 print的运用上

'''
#这是 Python3 的代码
#This is my shopping list
#shoplist是一个变量，一张为即将前往市场的某人准备的购物清单
shoplist = ['apple', 'mango', 'carrot', 'banana'] 
#len是求列表的长度
print('I have', len(shoplist), 'items to purchase.')
#end表示不是换行，最后结束的是' ' 
print('These items are:', end=' ')
#遍历列表中的每一个项目
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')

shoplist.append('rice')
#打印列表[]
print('My shopping list is now', shoplist)

print('I will sort my list now')
#首字母排序
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
#删除首元素
del shoplist[0]
print('I bought the', olditem)
#打印剩下的列表
print('My shopping list is now', shoplist)
'''





#这是 Python2的代码
#This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist), 'items to purchase.'

print 'These items are:',
for item in shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist

print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is', shoplist

print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist








