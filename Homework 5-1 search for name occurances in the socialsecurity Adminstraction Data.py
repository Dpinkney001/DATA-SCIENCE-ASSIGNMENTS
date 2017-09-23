# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:00:08 2017

@author: Duvall Pinkney

Use regular expressions (regex) to search for name occurrences in the Social 
Security Administration data. Choose a name that can be spelled 3 or more ways
 (for example, "Megan" has alternative spellings of "Meaghan", "Megyn", "Meghan",
 etc.). Use regex to combine the totals from different spellings and graph for the
 21 years of state data. 

#1: Submit your Python program as a .py file.
#2: Submit a screen shot of the graphics window containing the plot.





"""
import re 




def fileShooter():
    year = 1990
    for year in range(1990, 2011):
        
        fName = "nystate/yob"+str(year)+".txt"
       
        return fName
        year += 1


def readfile1():
    with open("nystate/yob"+str(1990)+".txt", 'r') as f:
        
        for line in f:
            nameObj1 = re.search("megan", line)
            nameObj2 = re.search("Meaghan", line)
            nameObj3 = re.search("Megyn", line)
            nameObj4 = re.search("Meghan", line)
            nameObj5 = re.search("\Ame\w{3}an\Z", line)
            
            if nameObj1 == True:
                print(f[line])
            elif nameObj2 == True:
                print(f[line])
            elif nameObj3 == True:
                print(f[line])
            elif nameObj4 == True:
                print(f[line])
            elif nameObj5 == True:
                print(f[line])
        
def readfile2():
   with open("nystate/yob"+str(1991)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)

def readfile3():
    with open("nystate/yob"+str(1992)+".txt", 'r') as f:
        
       for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)

def readfile4():
    with open("nystate/yob"+str(1993)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)

def readfile5():
    with open("nystate/yob"+str(1994)+".txt", 'r') as f:
        
       for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
            

def readfile6():
    with open("nystate/yob"+str(1995)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
            
def readfile7():
    with open("nystate/yob"+str(1996)+".txt", 'r') as f:
        
       for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
   

def readfile8():
   with open("nystate/yob"+str(1997)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
        
        
def readfile9():
   with open("nystate/yob"+str(1998)+".txt", 'r') as f:
        
       for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
        
        
def readfile10():
    with open("nystate/yob"+str(1999)+".txt", 'r') as f:
        
       for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
        
def readfile11():
   with open("nystate/yob"+str(2000)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
def readfile12():
    with open("nystate/yob"+str(2001)+".txt", 'r') as f:
        
       for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
        
def readfile13():
    with open("nystate/yob"+str(2002)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)


def readfile14():
    with open("nystate/yob"+str(2003)+".txt", 'r') as f:
        
        for line in f:
            nameObj1 = re.search("megan", line)
            nameObj2 = re.search("Meaghan", line)
            nameObj3 = re.search("Megyn", line)
            nameObj4 = re.search("Meghan", line)
            nameObj5 = re.search("\Ame\w{3}an\Z", line)
            
            if nameObj1 == True:
                print(f[line])
            elif nameObj2 == True:
                print(f[line])
            elif nameObj3 == True:
                print(f[line])
            elif nameObj4 == True:
                print(f[line])
            elif nameObj5 == True:
                print(f[line])
                
def readfile15():
    with open("nystate/yob"+str(2004)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
               
def readfile16():
    with open("nystate/yob"+str(2005)+".txt", 'r') as f:
        
       for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
        
def readfile17():
    with open("nystate/yob"+str(2006)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)    
        
def readfile18():
    with open("nystate/yob"+str(2007)+".txt", 'r') as f:
        
       for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)       
        
def readfile19():
    with open("nystate/yob"+str(2008)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)

def readfile20():
   with open("nystate/yob"+str(2009)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
            
def readfile21():
   with open("nystate/yob"+str(2010)+".txt", 'r') as f:
        
        for line in f:
            re.search("megan", line)
            re.search("Meaghan", line)
            re.search("Megyn", line)
            re.search("Meghan", line)
            re.search("\Ame\w{3}an\Z", line)
        


        
def main():
    #readfile(fileShooter())
    readfile1()
    readfile2()
    readfile3()
    readfile4() 
    readfile5()
    readfile6()
    readfile7()
    readfile8()
    readfile9()
    readfile10()
    readfile11()
    readfile12() 
    readfile13()
    readfile14()
    readfile15()
    readfile16()
    readfile17()
    readfile18()
    readfile19()
    readfile20()
    readfile21()

main()    