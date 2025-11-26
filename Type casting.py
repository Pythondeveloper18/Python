

#--------------------TYPE CASTING-------------------#



#INTEGER---------->

print(10+20) #30.3------>  #int+int
print(10+20.3)  #30.3----->  #int+float
#print(10 +"10")      #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(10+'20.3')     #TYpeError: unsupported operand type(s) for +: 'int' and 'str' 
#print(10 + [20 , 3]) #TypeError: unsupported operand type(s) for +: 'int' and 'list'
#print(10+(20,3))     #TypeError: unsupported operand type(s) for +: 'int' and 'tuple'  

#FLOAT-------------->

print(10.3+50.5) #60.8--------->float+float
print(10.3+10)   #20.3--------->float+int
#print(10.3+'10')     #TypeError: unsupported operand type(s) for +: 'float' and 'str'
#print(10.5+[50,50])  #TypeError: unsupported operand type(s) for +: 'float' and 'list'
#print(10.3+(100,7))  #TypeError: unsupported operand type(s) for +: 'float' and 'tuple'


#STRING------------->

#print('10'+10)      #TypeError: can only concatenate str (not "int") to str
#print('10'+10.3)    #TypeError: can only concatenate str (not "float") to str 
#print('10'+[10,10]) #TypeError: can only concatenate str (not "list") to str
print('10'+('10')) #1010------>STRING+STRING
#print('10'+(10,10)) #TypeError: can only concatenate str (not "tuple") to str


#LIST-------------->


#print([10]+10)       #TypeError: can only concatenate list (not "int") to liST
#print([10]+10.3)     #TypeError: can only concatenate list (not "float") to list
#print([10]+'10')     #TypeError: can only concatenate list (not "str") to list
print([10]+[10]) #[10, 10]-------------> list+list
#print([10]+(10,3))   #TypeError: can only concatenate list (not "tuple") to list



#TUPLES--------------->
#print((10,3)+10)    #TypeError: can only concatenate tuple (not "int") to tuple
#print((10,3)+10.3)  #TypeError: can only concatenate tuple (not "float") to tuple 
#print((10,3)+"10")  #TypeError: can only concatenate tuple (not "str") to tuple
#print((10,3)+[10])  #TypeError: can only concatenate tuple (not "list") to tuple
print((10,3)+(10,4)) #(10, 3, 10, 4)------------->TUPLE+TUPLE




#---------------------Data MANIPUTLATIONS----------------------#
#----------------------------------------------------------------#


#ADDING-------------------->




print(10+20) #30.3------>  #int+int
print(10+20.3)  #30.3----->  #int+float
#print(10 +"10")      #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(10+'20.3')     #TYpeError: unsupported operand type(s) for +: 'int' and 'str' 
#print(10 + [20 , 3]) #TypeError: unsupported operand type(s) for +: 'int' and 'list'
#print(10+(20,3))     #TypeError: unsupported operand type(s) for +: 'int' and 'tuple'  




#SUBTRACTION---------------->




print(10-20) #-10------>  #int-int
print(10-20.3)  #-10.3----->  #int-float
#print(10 -"10")      #TypeError: unsupported operand type(s) for -: 'int' and 'str'
#print(10-'20.3')     #TYpeError: unsupported operand type(s) for -: 'int' and 'str' 
#print(10 - [20 , 3]) #TypeError: unsupported operand type(s) for -: 'int' and 'list'
#print(10-(20,3))     #TypeError: unsupported operand type(s) for -: 'int' and 'tuple' 



#MULTIPULICATION-------------------->


print(10*20) #200------>  #int*int
print(10*20.3)  #203.0----->  #int*float
#print(10 *"10")      #TypeError: unsupported operand type(s) for *: 'int' and 'str'
#print(10*'20.3')     #TYpeError: unsupported operand type(s) for *: 'int' and 'str' 
#print(10 * [20 , 3]) #TypeError: unsupported operand type(s) for *: 'int' and 'list'
#print(10*(20,3))     #TypeError: unsupported operand type(s) for *: 'int' and 'tuple' 



#DIVISON-------------------->



print(10/20) #0.5------>  #int/int
print(10/20.3)  #0.49----->  #int/float
#print(10 /"10")      #TypeError: unsupported operand type(s) for /: 'int' and 'str'
#print(10/'20.3')     #TYpeError: unsupported operand type(s) for /: 'int' and 'str' 
#print(10 / [20 , 3]) #TypeError: unsupported operand type(s) for /: 'int' and 'list'
#print(10/(20,3))     #TypeError: unsupported operand type(s) for /: 'int' and 'tuple' 



















