

#--------------------DICTI0NARIES----------------------#




a = {10:20,"HELLO":5.0,50:50}
print(a)



#accessing data 


g = {'a':10,'b':20,'c':30,'d':40}
print(g['a'])
print(g['b'])
print(g['c'])



#updating



h = {'a':10,'b':20,'c':30,'d':40}
h['a'] = 'x'
h['b'] =  'y'
h['c'] = 'z'
print(h)


#deletind data

j  = {'a':10,'b':20,'c':30,'d':40}
del j['a']
del j['b']
del j['c']
print(j)


#inserting data


o =  {'a':10,'b':20,'c':30,'d':40}
o['k'] = 10
o['r'] = 100
o['v'] = 1000
o['l'] = 10000


print(o)




#-----------------DICTIONARY FUNCTIONS-----------------#



#KEY----------


aa =  {'a':10,'b':20,'c':30,'d':40}
print(aa.keys())




#values------
print(aa.values())



#items--------
print(aa.items())



#get----------
print(aa.get('a'))
print(aa.get('m', 100))



#setdefault--------
print(aa.setdefault('x'))
print(aa)


#pop-------------
aa.pop('a')
aa.pop('b')
print(aa)


#popitem----------
aa.popitem()
aa.popitem()
print(aa)


#update------------
c = {'c':10,'d':50,'v':400}
s  = {'q':70,'g':80,'f':800}
s.update(c)
c.update(s)
print(s)

#fromkeys------------
print({}.fromkeys('abcnddmdkmskdmskdm',45))


#clear-------
c.clear()
print(c)

s.clear()
print(s)



#copy---------
c.copy()
print(c)



dic = {10 : 20}
print(dic)























 



