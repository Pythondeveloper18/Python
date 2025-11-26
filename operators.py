

    #------------------------OPERATORS------------------------#


#ARTHEMITCAL OPERATORS------> 1



a = 10
b = 20


print(a+b)  #------>add
print(a-b)  #------->sub
print(a*b)  #------->muliti
print(a/b)  #------->divide
print(a%b)  #------->m divide
print(a**b) #------power/exponention
print(a//b) #------>floor division




#boolean operators---------> 2

         
         #isalpha

c = ('hyderabad')
print(c.isalpha()) 

d = ("4vizag")
print(d.isalpha())

        #isdigit

e = ('200km')
print(e.isdigit())


#comparison operators-------> 3


f = 50
f1 = 100

print(f>f1)  #False
print(f<f1)   #true
print(f<=f1)   #true
print(f>=f1) #false
print(f==f1) #false
print(f!=f1) #true



#logical operators------------> 4


print(a<b and a>b)  #1 , 0  == flase
print(a<b or a>b)   #1 , 0  == true
print( not a<b , a>b) #0 , 0 ---flase 
print(not a<b or a>b and a==b) #false



#identity operators-------------->5


a = 10
b = 20
print(id(a) , id(b))
print(a is b )
print(a is not b )


c = 50
d = 50
print(c is d)
print(c is not d)



      #mutable 

e = [100 , 1111]
f = [1111, 15]
print(e is not f)




#---------------------MEMBERSHIP OPERATORS------------------#

g = ("hello")
print("e" in g)  #true
print("e"  not in g)  #false



#------------------assignment operators-------------------#


a = 10
a+=50
print(a)  #-------addition


b = 50
b-=60
print(b) #----------subtraction 


c = 100
c*=10
print(c)  #-------------multiple



d = 5
d/=10
print(d)  #--------------divident
























