#coding=utf-8                                  
 
#====================
#File: oop_subclass.py
#Author: Cheng Cai
#Date: 2017-09-04
#====================

#这是 python2版本
class SchoolMember:                                                 #基类
    '''代表任何学校里的成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: {})'.format(self.name)

    def tell(self):
        '''告诉我所有细节'''
        print 'Name:"{}" Age: "{}"'.format(self.name, self.age)




class Teacher(SchoolMember):                                        #派生类,定义一个老师类来继承父类
    '''代表一位老师'''
    def __init__(self, name, age, salary):                          #继承父类并且重构
        SchoolMember.__init__(self, name, age)                      #继承基类方法
        self.salary = salary                                        #在方法前面加上基类名作为前缀
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"{:d}"'.format(self.salary)


class Student(SchoolMember):                                        #派生类，定义一个学生类来继承父类
    '''代表一位学生'''
    def __init__(self, name, age, marks):                           #继承父类并且重构
        SchoolMember.__init__(self, name, age)                      #继承父类方法
        self.marks = marks
        print '(Initialized Student: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks:"{:d}"'.format(self.marks)

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('ChengCai', 25, 100)

# 打印一行空白行
print 
members = [t, s]
for member in members:
    #对全体师生工作
    member.tell()


