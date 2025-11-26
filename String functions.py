         #captalize

s1 = "mahindara singh dhoni"
print(s1.capitalize())

s2 = "      "
print(s1.capitalize())


        #title

s1 = "my name is sai"
print(s1.title())

you = "ya iam fine"
print(you.title())

       #lower

powershell = "PYTHON"
print(powershell.lower())

aws = "AMozAn WeB sErvICes"
print(aws.lower())


      #upper

testing = "run and debug"
print(testing.upper())


continuo  =  "StopAsyncIteration"
print(continuo.upper())

      #swap

source = "ConTroL"
print(source.swapcase())

Ellipsis = "HIGHend"
print(Ellipsis.swapcase())


     #Isalpha

Except = "member"
print(Except.isalpha())

frontend = "html.index"
print(frontend.isalpha())

     #isdigit

output = "010110"
print(output.isdigit())

Import = "codecs0123"
print(Import.isdigit())


      #Isalnum

ports = "terminal block"
print(ports.isalnum())

stfunctions = "32count"
print(stfunctions.isalnum())


     #startswith

dubugging = "testing"
print(dubugging.startswith("st",1 , 5))

output = "KeyboardInterrupt"
print(output.startswith("up", 10 ,1))


       #endswith 


frontend = "backend"
print(frontend.endswith("ac" , 1 , 5))


frontend = "backend"
print(frontend.endswith("ck" , 6  , ))


      #count

name = "ronalodo"
print(name.count("n"))    #1
print(name.count('o' , 0 , 8))  #3
print(name.count('lo' , 0  ,8 ))   #1


    # INDEX

vscode = 'SUBLIME BETTER THEN VSCODE'
print(vscode.index('I')) #4
print(vscode.index('E' , vscode.index('E')+1))
print(vscode.index('E'))
print(vscode.index('B' , vscode.index('B')+1)+1)

     #FIND

print(vscode.find('x'))
print(vscode.find('E' , vscode.index('E')+1))


     #rindex

txt = ("sai bheemaraju")
print(txt.rindex("a", 0 , 10))


txt = ("rohit virat")
print(txt.rindex("i", 0 , 10))


    #rfind

txt = ("lion king")
print(txt.rfind("n" , 0 , 10))


txt = ("ogas gambheera")
print(txt.rfind("g", 0 , 13))



    #strip


txt = ("rishi1kumar")
print(txt.strip("rr"))


txt = ("bhbhhbfv nfv nfv nfv nfv nfv fn c")
print(txt.strip())


        #split


txt = ("hi hello  world my name is sai")
print(txt.split())


txt =''' (Date,Country,Production(barrels/day),Price(USD/barrel
2025-01-01,USA,11800000,78.2
2025-01-01,Saudi Arabia,10300000,80.1
2025-01-01,Russia,9500000,77.8
2025-01-01,Canada,4600000,75.5
2025-01-01,Iraq,4300000,79.3
2025-02-01,USA,11950000,79.6
2025-02-01,Saudi Arabia,10200000,81.2
2025-02-01,Russia,9400000,78.1
2025-02-01,Canada,4650000,76.4
2025-02-01,Iraq,4350000,80.0)'''


print(txt.splitlines())



     #replace


txt = ("sai")
print(txt.replace("sai" , "Russia" , 1))





txt = ("jjdkodkodkofjdnjdnkdlod")
print(txt.replace("jj" , "sai" , 10))



     #istrip


txt = ("IRON MAN")
print(txt.lstrip("")[6: 7: 1 ])



     #rstrip

txt=("captian america")
print(txt.rstrip("cap"))


     #rjust

txt = "sai"
btxt =" bheemaraju "
print(txt.rjust(1) , "bheemaraju")  


   #zfill
   

txt = " superman"
print(txt.zfill(100))



    #splitlines

txt = ("hihelloworld")
print(txt.splitlines("\n"))



    #centre

txt = ("lovelyboy")
print(txt.center(10 ,'s',))
     















 