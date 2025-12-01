name = ('parbha bheemaraju')
#op = []
for i in name:
	if i in 'aeiou':
		print(i)
		#op.append(i)

#print(i)





def school(students):
	def warrper(a,b):
		print('iam inside the warrper')
		if type(a) == type(b):
			return students(a,b)
		else:
			return "low internet"
			print('iam outside the warrper')



	return warrper


print('iam in checkpoint')
@school
def students(a,b):
	return  a + b
print('iam in checkpoint')
print(students(10 , 'j'))
print('code run success......')
