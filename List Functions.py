     

      #---------------LIST----------------#



l1 = [ "hi" , "hello" , ]
l2 = [ 'captian','america',]
print(l1)
print(l1+l2)





#accesing the index position


txt = ["they", "call" ,"him","ogas", "gambherra"]
print(txt[3][1])
print(txt[1][2])





#updating the element in the list

txt[4] = 'rishi'
txt[1] =  'sai'
txt[2] =  'siddhu'
txt[3] = 'kalayani'
print(txt)





#deleting the element from the list 

del txt[0]
del txt[1]
del txt[2]

print(txt)




      # using sliceing 
      
txt = ['hi', 'my', 'name','is','sai',]
txt[4] = 'ramu'
del txt[4]

print(txt[ : : -1])  #sliceing in list 
print(txt[1: 4: 1])



    #append 

print(txt.append("rishi"))
print(txt.append("ravi"))
print(txt)


txt = ["ultracore"]
print(txt.append('procasaser'))
print(txt)

 

    #extend


company = ['blue star']
print(company.extend('company'))
print(company)


movie = ['spider']
movie.extend('man')
print(movie)



    #insert


lovely = ['boysai' , 'sai']
lovely.insert(1 , 's')
print(lovely)



facebook = ['instagram','twitter','whatsapp']
facebook.insert(1 , 'arrati')
print(facebook)


   #count


laptop = ['h', 'f'  , 1, 1, 2, 3 ]
print(laptop.count(2))


output = ['blue star', 'c', 'o', 'm', 'p', 'a', 'n', 'y','spider', 'm', 'a', 'n']
print(output.count('c'))
print(output.count('o'))
print(output.count('m'))



    #index 


social = ['instagram', 'arrati', 'twitter', 'whatsapp']
print(social.index('instagram'))
print(social.index('whatsapp'))



txt = ['hi', 'hello', 'captian', 'america']
print(txt.index("america"))

     

         #pop

print(txt.pop(0))
print(txt.pop(1))
print(txt.pop(0))
print(txt.pop(0))
print(txt)



string = ['type', 'count', 'index','reverse']
print(string.pop(0))
print(string.pop(1))
print(string.pop(0))
print(string.pop(0))
print(string)


    #remove 


l1 = ['they', 'sai', 'siddhu', 'kalayani', 'rishi']
print(l1.remove('sai'))
print(l1.remove('siddhu'))
print(l1)



l2 = [ 1 , 1 , 5 , 5 , 6, 9 , 10 , 11 ,]
print(l2.remove(1))
print(l2.remove(5))

print(l2)




   #reverse



l2.reverse()
print(l2)

l1.reverse()
print(l1)


   #sort



no = [ 1, 5, 10, 11, 12, 45, 100 , 4 , 3,]
print(no.sort())
print(no)


print(no.sort(reverse=True))
print(no)


    #clear


no.clear()
print(no)



happy = ['sad']
print(happy.clear())
print(happy)



     #copy

l5 = ['kfkfmkmkfmkwsdcmnkdm']
print(l5.copy())
print(l5)


    #count

