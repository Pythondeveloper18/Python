
def change(name):
	def wrapper (name):
		if name:
			return (name.upper())
		else:
			return 'code error 404'
	return wrapper		
	
             
				
@change
def convert(name):
	return name.upper()

print(convert('hi'))
print(convert('100'))














def change(func):
    def wrapper(name):
        if name:  # checks if name is not empty
            return func(name.upper())  # call the original function
        else:
            return 'code error 404'
    return wrapper

@change
def conv(name):
    return name  # name is already converted by decorator

print(conv('hi'))   # Output: HI
print(conv(''))     # Output: code error 404

