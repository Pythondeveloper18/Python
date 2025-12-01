

                            #-----------------FUNCTIONS------------------#





#=============================================================================================================

def sai(x,y,z):
	op = x + y + z  #--------->called function
	return  op

print(sai(10,10,10)) #----------->calling functin

#==============================================================================================================

def students(shyam,prasad,ravi):
	ranks = shyam + prasad + ravi  #------------->called function
	return ranks

print(students(50,40,60)) #------------>calling function

#==============================================================================================================


# writing a programm  to decrease the mulit athresne upto 6 , 
#if the number is above 6 it returns false
#if it is below the 6 it will return numbers
#if it is the same number it will return same number....

#function_name = data
#parameters = numbers/num
#ouput = 6

def data(num):  #------------>called function
	if num  >= 6:
		return num == 6 
	else:

		return num

print(data(1)) #--------you can return any number #------------------->calling function


#====================================================================================================

#Default parameters---------->

def sai(a,b,c=0,d=0):
	return a + b + c + d

print(sai(1,2))
print(sai(1,2,3))
print(sai(1,2,3,4))


#====================================================================================================


#*Args----------------------->

def args(*a):
	return a

print(args(1,2,3,4,5))  # you can add number of parameters in *args

      #-----cambo-----#

def aggi(a,b,c,d=0,e=0,*f):
	print(a,b,c,d,e,f)

aggi(1,2,3,4,5,6,6,8,5,9,2,5)


#======================================================================================

#**kwargs

def myfun(**k):
	return k

print(myfun(d=1))


         #-----cambo------->

def aggi(a,b,c,d=0,e=0,*f,**g):
	print(a,b,c,d,e,f,g)

aggi(1,2,3,4,5,6,6,8,5,9,y=2,X=5)

































