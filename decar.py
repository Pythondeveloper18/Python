
def change(convert):
	def wrapper (a,b):
		if id(a) == id(b):
			return convert(a,b)
		else:
			return 'error404'
	return wrapper
		
@change
def convert(a,b):
	return a * b


print(convert(10, 10))
#----------------------------------------------------------------




print("*" * 25)


def change(name):
	def wrapper (name):
		if isinstance(name, str):
			return (name.upper())
		else:
			return "sucess"
	return wrapper
					
	
@change
def conv(name):
	return name.upper()

print(conv('a1'))


def even(odd):
	def wrapper (a,b):
		print('iam inside the wrapper')
		if type(a) == type(b):
			return odd(a,b)
		else:
			return 'try with another number'
	return wrapper		

@even
def odd(c,d):
	return c * d

print(odd(2,'h'))















def password(number):
	return number.isalnum()


print(password(''))

	