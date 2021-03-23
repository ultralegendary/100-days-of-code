#Comment line 
"""multi
line
comment """
print("Hello world")


#variable declaration

a=4     
print(a,type(a))
a="python"
print(a,type(a))


#list
nums=[]
nums.append(10)
nums.append([10])
nums.append("helo")
print(nums)


#input 
name=input("Enter your name : ")
print("Hellow ",name)

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=num1*num2
print("Product =",num3)


#selection statements
n=20
if n<10:
    print("number is less than 10")
elif n<30:
    print("number is less than 30")
else :
    print("number is greater than 30")



#functions in python
def getInteger():
    return int(input("Enter a intiger : "))

def Main():
    print("Entered main() ")
    print(getInteger())

if(__name__=='__main__'):
    Main()


#iteration(looping)
for i in range(10):
    print(i,end=' ')


#importing modules
import math
print(math.fabs(float(input("Enter a number: "))))



#Arithimetic operators

a=20
b=30
a+b
a-b
a*b
a/b#division
a//b#floor division
a%b#modulo
a**b#power


#Relational operators
a>b
a>=b
a<b
a<=b
a==b
a!=b

#Logical operators
a=True
b=False
(a and b)
(a or b)
(not a)


#Bitwise operators
x=3
y=8

x|y
x&y
x^y
~x
x>>2
x<<2

#special operators
a=2
b=2

a is b #true

a=[1,2,3]
b=[1,2,3]
a is b # false
a=b
a is b #true


1 in a#true
4 not in a#true


#ternary operator

print("true")if 1>5 else print("false")


print((1,2)[1>2])
print({True: 1, False: 2} [1 < 2])
print((lambda :1,lambda:2)[1<2])

print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")

min=1<2 and 1 or 2


type(1000**1000)



#end,sep parameter
print("hi","thie","is","python",sep='-',end='|')

#type conversion 

#explicit:
#int(a,base)
int("a",16)
float(23)
ord('A')
oct(20)
hex(30)
set([1,2])
tuple([1,2])
list([1,2])
dict(('a',1),('b',2))
str(23032)
complex(2,3)
chr(97)
print("%c"%3001)

#use of __name__

print ("File1 __name__ = %s" %__name__) 

if __name__ == "__main__": 
    print ("File1 is being run directly")
else: 
    print ("File1 is being imported")


#multiply input in one line
x,y=input().split()

X,Y=[int(a)for a in input().split()]
x,y=map(int,input().split())



#END of DAY 1
