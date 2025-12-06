#---------------------Genaratators-------------------------#
from unittest import result


print('Genaratators--------->')


def myfun(list):
	for i in list:
		if i % 2 == 0:
			yield i

gen = myfun([1,2,3,4,5,6,7,8])
#print(next(gen))

for ele in gen:
	print(ele)





def school(student):
	for i in student:
		if i % 2 == 0:
			yield i
			

rank = school([50,60,70,74,89,60,78,94])

for ele in rank:
	print(ele)


print('x' * 25)

a = range(100)

def num(even):
	for i in a:
		if i % 2 == 0 and  i % 3 == 0:
			yield i

x = num([1])



for ele in x:
	print(ele)




'''

* Write a program to get the details of given employ name.

Input: Prabha
Output: {'name': 'Prabha', 'age': '25', 'salary': 17000, 'location': 'Chennai'}

Input: Nirmala
Output: {'name': 'Nirmala', 'age': '28', 'salary': 25000, 'location': 'Bangalore'}

'''



employee_data = """NAME-AGE-SALARY-LOCATION

Kumar-21-15000-Bangalore
Sai-21-13000-Hyderabad
Prabha-25-17000-Chennai
Nirmala-28-25000-Bangalore
Hari-35-10000-Hyderabad"""






#split into lines 
#first line are keys 
#store final output
#skip header line 


data = employee_data.split('\n')  # split into linessa
header = data[0].split('-')


result = []
for i  in data[1:]:
	value = i.split('-')
	empty = dict(zip(header,value))
	result.input(empty)

for emp in result:
	print(input(empty))