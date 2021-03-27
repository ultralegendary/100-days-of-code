#day 4
#https://practice.geeksforgeeks.org/tracks/python-module-4/?batchId=119

#functions

def divisible_by_2(n):
    return not n%2
eval("""print("{n} is divisile by 2" if divisible_by_2({n}) else "{n} is not divisible by 2")""".format(n=int(input("Enter a number "))))


#pass
a=True
if a==True:
    pass
else:
    print("false")

#yeild sample
#yeild returns iterator
def fun():
    yield 1 
    print("1pass")
    yield 2
    print("2pass")
    
    yield 43
    print("3pass")
print(fun())
print("End of first")
print(list(fun()))

def square():
    i=0
    while True:
        yield i*i
        i+=1
for num in square():
    if(num>=100):
        break
    print(num,end='|')

#skipped programs on modules

from math import *#imports all functions
print(sqrt(2))


#classes and objects
#inheritance

class person(object):
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemployee(self):
        return False
class employee(person):
    def isemployee(self):
        return True
a=person("person_1")
b=employee("person_2")
print(a.getname(),a.isemployee())
print(b.getname(),b.isemployee())

issubclass(employee,person)
issubclass(person,employee)
isinstance(b, employee)
isinstance(a,employee)

#multiple inheritance
class a():
    def __init__(self):
        self.a=10
class b():
    def __init__(self):
        
        a.a=20
        self.a=20
class c(a,b):
    def __init__(self):
        super().__init__()
        a.a=30
        b.a=30
        self.a=30

#data hiding
class a():
    __hidden=10 #hidden variable uses double underscore
    def __init__(self,a):
        self.__hidden=a
obj=a()
obj._a__hidden #ascessing object illegally

#static member
class a():
    total=0 #static variable

#lambda functions:
square=lambda x:x*x
square(2)

print(list(filter(lambda x: x>18,[4,8,33,23,768,18,9])))

list(map(lambda x:x*x,[2,3,4,5,6,7]))

from functools import reduce
reduce(lambda a,b:a*b,[i for i in range(1,10)])

reduce(lambda a,b:a if a>b else b,[1,34,54,-34,2,43,3])


#end of day 3, practice more