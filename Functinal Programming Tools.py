


#-------------------------Functional programming tools----------------------------#


print('Filters---------------->')
print('=' * 131)

#Filter---------------->

a = [100,200,3,400]


def even(a):
	if a % 2 == 0:
		return a


print(list(filter(even ,a)))

#----------------------------------------------------------------------
print('-' * 50)

b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]


def odd(b):
	if b % 3 == 0:
		return b


print(tuple(filter(odd,b)))

#--------------------------------------------------------------------------

d = ['ravi','raju','ramu','ravana']

def students(d):
	if len(d) > 1:
		return d


print(list(filter(students , d)))
print('-' * 50)

#-------------------------------------------------------------------------

e = [1,2,6,5,10,700,500]


def square(e):
	if e % 2:
		return e

print(list(filter(square , e)))
print('-' * 50)


#---------------------------------------------------------------------------

g = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

def siddhu(g):
	if g % 2 == 0:
		return g


print(list(filter(siddhu , g)))
print('=' * 131)


#======================================================================================


print('Map----------------->')
print('-' * 25)

ranking = [10,20,30,40,50,100]

def students(i):
	return i // 2

print(list(map(students , ranking)))
print('-' * 50)
#-----------------------------------------------------------------------------

Bhasyam = [100, 150,200,250,300]

def names(i):
	return str(i)



print(list(map(names , Bhasyam)))
print('=' * 131)

#======================================================================
print('reduce-------->')
print('-' * 25)


from functools import reduce

a = [100,2000,30000,400000,5000000,60000000]


def add(a,b):
	return a + b


print(reduce(add,a))
print('=' * 131)
#===========================================================================================
print('zip-------->')
print('-' * 25)

name = ['hello']
mama = ["hi"]
mame = ['world']

print(list(zip(name,mama,mame)))




























