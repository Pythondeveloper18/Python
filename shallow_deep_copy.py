#-------------------SHALLOW AND DEEP COPY----------------------#


#SHALLOW COPY ON MUTABLE OBJECTS
'--------------------------------'



l1 = [1,2,23]

l2 = l1
print(id(l1),id(l2))
print(l1,l2)
l1[1] = 100
print(l1)
print(l2)



a1 = {10:50,50:80,60:90}

a2 = a1
a3 = a2
a4 = a3
a5 = a4ip
print(id(a1),id(a2),id(a3),id(a4
                              ),id(a5))
print(a1,a2,a3,a4,a5)
a1[50] = 500
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)


#SHALLOW COPY ON INMUTABLE OBJECTS
'----------------------------------'
 

c1 = 'GOAT SHIP'

c2 = c1
print(id(c1),id(c2))
print(c1)
print(c2)

#c1[3]='a' #TypeError: 'str' object does not support item assignment



#deepcopy on mutable objects
'-------------------------------'

h1 = [100]

h2 = h1.copy()
print(id(h1),id(h2))
h1[0] = 400
print(h1) #400
print(h2)  # 100


z1 = {'hi':'hello','bye':78,45:700}
z2 = z1.copy()
print(id(z1),id(z2))
print(z1)
print(z2)
z1["hi"] = 'hello'
print(z1)
print(z2)


#deepcopy on inmutabale objects
'-------------------------------'

'''k1 = ("amozon","filpkart")
k4 = k1.copy()
id(k1)
id(k4)
print(id(k1),id(k4))'''  #AttributeError: 'tuple' object has no attribute 'copy







