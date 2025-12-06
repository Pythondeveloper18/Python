'''

class Sudents: 
	a = 10
	b = 100
	c = 1000

my_instance = Sudents()
print(my_instance.a)
print(Sudents)
print(my_instance)
my_instance.a = 100
print(my_instance.a)
my_instance.d = 1000
print(my_instance.d)
print(my_instance)
print(my_instance.a)


class a:
	def students(a,b):
		return a + b



obj = students()
print(obj.students(10,10))

'''
'''

class a:
	x = 100
	y = 200

obj = a()
print(obj.x)



class Animal:
    def sound(self):
        print("Makes a sound")

class Dog(Animal):
    def sound(self):
        print("Barks")



obj = Dog()
print(obj.sound())



class Parent:
    def show(self):
        print("I am Parent")

class Child(Parent):
    pass

obj = Child()
obj.show()   # Output: I am Parent





class password:       #-------->taking class
	def show(self):   #-------->writing a function
		print(1477)   #---------->print the function

class login(password): #----------> creating a class and taking the function from from 
	pass

obj = login()
obj.show()
'''


class A:
	def __init__(self):
		self.z = 100
		self.y = 500

	def add(self):
		return self.z + self.y
	def mul(self):
		return self.z / self.y
	def div(self):
		return self.z * self.y
	def even(self):
		return self.z * self.y

obj = A()
print(obj.even())


class Person:
    def __init__(self, name):
        self.name = name

'''

try:
    # Code that may cause an error
    x = 10 / 0
except:
    # Code that runs if an error happens
    print("An error occurred")

'''
try:
	x = 100
	y = 200
	print(xy)


except:
	print('babu neku coding vacha aslu')

try:

   with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

except:
	print('no file is given')








