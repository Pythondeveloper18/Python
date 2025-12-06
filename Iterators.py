 


 #--------------------- Iteators -----------------------------#
print('-------------------iteators-------------------------------')

my = iter([1,2,3,4])

print(next(my))
print(next(my))
print("*" * 20)
for i in my:
	print(i)


name = iter(('sai','ramu','raju'))
print(next(name))
print(next(name))



if i in name:
	print(i)
