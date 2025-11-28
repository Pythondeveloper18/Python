

            #-------------------List Camphersion-----------------------#




# Lc with 2 sections------>


from requests import get


input_list = [1,2,3,4]

output_list = []

for i in input_list:
	if i ** 2 :
		 print(i ** 2)
	else:
		print(i)


print([ i ** 2   for i in input_list])

#-------------------------------------------------------------------------------------

hyberabad = ["telagana","andhrapradesh",'india']
empty = []

for i in hyberabad:
	empty.append(i.count("t" , 0 ,6))
else:
	print(empty)


print([i.count("t" , 0 ,6) for i in hyberabad ])



#===================================================================


#LC WITH 3 SECTIONS---------------------------->


a = [1,2,3,4,5]
output = []

for i in a:
	if i % 2:
		output.append(i ** 2)
	else:
		output.append(i ** 3)
print(output)



print([i ** 2 for i in a  if i % 2])




b = [10,5,6,8]
                                      
print("#" * 50 )              
for i in b:
	if i ** 2:          #------------------------------> Lc with 2 sections
		print(i ** 2)
print("-" * 50 )
print([ i ** 2  for i in b])


#------------------------------------------------                                                        
print("#" * 50 )

for i in b:
	if i % 2:
		print(i ** 2)    #------------------------------> Lc with 3 sections
print("-" * 50 )

print([ i ** 2  for i in b  if i % 2])

print("#" * 50 )
#--------------------------------------------------

for i in b:
	if i % 2:
		print(i ** 2)
	else:
		print(i ** 3)#---------------------------------->Lc with 4 sections

print(i)


print("-" * 50 )

print([ i ** 2  if i % 2 else i ** 3 for i in b])

print("#" * 50 )


#-------------------------d


# Task-1: WAP to list the elements whose length is greater than 5
# input_list = ['hyderabad', 'chennai', 'goa', 'vizag', 'ladak']
# output_list => ['hyderabad', 'chennai']

input_list = ['hyderabad', 'chennai', 'goa', 'vizag', 'ladak']

uput = []


for i in input_list:
	if len(i) > 4:
		uput.append(i)

    
print(uput)

print([i for i in input_list if len(i) > 5])

print('=' * 50)



x = [1,1,2,34]

print([i % 2 == 0  for i in x])

print([i ** 2  for i in x  if i % 2 == 0])

print([i ** 2 if i % 2  else i ** 3 for i  in x ])


lst = [1,2,4,5,6,7,8,9,10]
op = []
  
for i in lst:
	if i % 2 == 0:
		print(i)



#task 2 : write a  progamm to create a dicitonary with rhe keys from the given data structure and value as length of the elements .


citys = ['hyderabd' , 'chennai' , 'goa' , 'vizag' , 'ladak']

op = {}





print({i:  len(i) for i in citys })