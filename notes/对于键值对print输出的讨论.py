#使用用户输入来填充字典
responses = {}
polling_active = True

while polling_active:
	name = raw_input('\nWhat is your name?')
	response = raw_input('Which mountain would you like to climb someday?')

	#注意下一步是将字典中的键与值一一对应的
	responses[name] = response
	
	repeat = raw_input('Would you like to let another person respond? (yes/no)')
	if repeat == 'no' or repeat == 'n':
		polling_active = False

print '\n---Poll Results---'
#注意：对于字典，print输出时，不能使用是sorted()函数，
#使用后字典仅显示键，不显示值
#print sorted(responses)	#这个显示的是键，对键排序，不显示值
#下面一行代码显示键-值对
print responses
#在for循环中，针对键-值对的循环，可以使用sorted()
for name,response in sorted(responses.items()):
	print name + 'would like to climb '+ response + '.'
