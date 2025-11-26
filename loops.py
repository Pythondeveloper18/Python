
#-----------------Loops----------------------#


# for ---------------------------

students = 'sai','ramu','raju','shyam','ganesh'

for i in students:
	print("student name >>>" , i)




#----------------------------------------

even = [1,2,3,4,5,6,7,8,9,10]

#looping over the all the elements
# checking if the number are divisble by 2
#and the print

for i in even:
  if i % 2 == 0:
  	print(i)


#-----------------------------------------
#-----------------------------------------

students = 'sai','ramu','raju','shyam','ganesh'

for i in students:
    if i == 'shyam':
        break
    else:
	    print(i)


for i in students:
	if i == "shyam":
		continue
	else:
		print(i)



city = ["vizag","anakapalli","etikoppaka","gajuwaka"]

#alogrithm---
'-------------'

#looping over all data in dictionary
#using condition for check & select the city
#using "continue" key to that skip the city
#and then print


for i in city:
	if i == "etikoppaka":
		continue
	else:
		print(i)
print("outside")


#--------------------------------------
#--------------------------------------


#multi variable assement---------------

 
remarks = [("sai0"),('raj0'),('ram0')]

for a,b,c,d in remarks:
	print(a,b,c,d)

#--------------------------------------
#--------------------------------------


#while loop-------------------------------

#i = 100
#while i < 101
	#print(i)





#---------------------------------------------


put = ('hello world')

#alogorthim

#LOOPING OVER THE STRING
#CHECKING IF THE " A E I O U " IN THE STRING
#IF YES CONTINUE WITH PRINT

for i in put:
	if i in "aeiou":
		print(i)


#-----------------------------


# WAP tp list all even numbers in one list and all odd numbers in one list
# Input : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# Output: [2, 4, 6, 8, 10] & [1, 3, 5, 7, 9]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#alogorthim

#firstly take an empty
#

even = []
odd = []

for i in a:
  if i % 2 == 0:
  	even.append(i)
  else:
  	odd.append(i)
print(even,odd)



#------------------------------------

two = (100,200,300,400,500)



even = []
odd = []

for i in two:
	if i % 2 == 0:
		even.append(i)
	else:
		odd.append(i)
		print(even,odd)




i =  100
while i < 10:
	print(i)

		
		

		
'''
row = 7

for i in range(row):
	for i in range(row -  1 - 1):
		print("     " , end="     ")
		for i in range(2*i + 1):
			print("*", end='         ')
'''


--

num = float(input('enter the number:'))


if num > 0:
    print('postive')
elif num < 0:
    print('negative')
else:
    property('zero')


















	
	

	






	











