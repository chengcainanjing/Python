#coding=utf-8                                  
 
#====================
#File: io_input.py
#Author: Cheng Cai
#Date: 2017-09-05
#====================

#python2版本
def reverse(text):
    return text[::-1]
#text[a:b]代表从位置 a 开始到位置 b 结束来对序列进行切片
#第三个参数是确定切片的步长，默认步长是1
#这里的-1代表将返回翻转过的文本

def is_palindrome(text):
    return text == reverse(text)

something = raw_input ("Enter text: ")
#关于 python2与 python3中 print 与 input 的区别
#请看笔记：Python2与Python3中 print 的不同点

if is_palindrome(something):
    print "Yes, it is a palindrome"

else:
    print "No, it is not a palindrome"


