1. 在python2.x中raw_input( )和input( )，两个函数都存在，其中区别为

raw_input( )---将所有输入作为字符串看待，返回字符串类型

input( )-----只能接收“数字”的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）



2. 在python3.x中raw_input( )和input( )进行了整合，去除了raw_input( )，仅保留了input( )函数，
其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。

**Python2**
```
Python 2.3.4 (#1, Feb  2 2005, 11:44:13)   
[GCC 3.4.3 20041212 (Red Hat 3.4.3-9.EL4)] on linux2  
Type "help", "copyright", "credits" or "license" for more information.  
>>> user=raw_input("please input:")         
please input:wei                          #  raw_input 输入  字符串  成功  
>>> user  
'wei'  
>>> user=input("please input:")            
please input:123                          #  input 输入  数字  成功（返回的是数字）  
>>> user  
123  
>>> user=raw_input("please input:")  
please input:111 <span style="white-space:pre">         </span>  #  raw_input 输入  数字  成功（返回的还是当成字符串）  
>>> user  
'111'  
>>> user=input("please input:")  
please input:wei                          #  input  输入字符串   失败  
Traceback (most recent call last):  
  File "<stdin>", line 1, in ?  
  File "<string>", line 0, in ?  
NameError: name 'wei' is not defined  
```

**Python3**
```
Python 3.2.3 (default, Apr 11 2012, 07:15:24) [MSC v.1500 32 bit (Intel)] on win  
32  
Type "help", "copyright", "credits" or "license" for more information.  
>>> user=raw_input("please input:")                 #没有了raw_input  
Traceback (most recent call last):  
  File "<stdin>", line 1, in <module>  
NameError: name 'raw_input' is not defined  
>>> user=input("please input:")  
please input:wei  
>>> user  
'wei'  
>>> user=input("please input:")                     #input的输出结果都是作为字符串  
please input:123  
>>> user  
'123'  
```
