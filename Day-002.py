#Loops in python  
c=0
while c<=3:
    print(c,end=' ')
    c+=1

while(c<=6):
    print(c,end=' ')
    c+=1
else:
    print("End of loop")

#from 0 to n-1
for i in range(3):
    print(i)
    
#ittreation over list
print("list itteration")
l=["a","b","c"]
for i in l:
    print(i,end='|')

print("Dict itteration")
d = dict() 
d['a'] = 1
d['b'] = 2
for i in d :
    print("%s  %d" %(i, d[i]))
    
print("String itteration")
for i in "string":
    print(i,end="|")
    
#nested loops :
for i in range(10):
    for j in range(i):
        print(i,end=' ')
    print()


#continue statement
for i in "apple":
    if i=='p':
        continue
    print(i,end='|')


#error handling and iter
a=iter([1,2,3,4,5])
while True:
    try:
        print(next(a))
    except StopIteration:
        break

#enumerate
a=["apple","banna","orange"]
for i,x in enumerate(a):
    print(i,x)

for i in enumerate(a,start=2):
    print(i)
    
#zip
b=[1,2,3]
for i,j in zip(a,b):
    print(i,j)
    

#unzip
l1,l2 = zip(*[('Aston', 'GPS'), 
              ('Audi', 'Car Repair'), 
              ('McLaren', 'Dolby sound kit') 
           ])
print(l1)
print(l2)


import sys

a = range(1,10000)
print ("The size allotted using range() is : ")
print (sys.getsizeof(a))
a[2:5]

#replacement for switch 

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

    # get() method of dictionary data type returns 
    # value of passed argument if it is present 
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")
if __name__ == "__main__":
    argument=0
    print (numbers_to_strings(argument))

#difference betweeen is and ==
#is checks if id() of objects are same
list1 = []
list2 = []
list3=list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:    
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:    
    print("False")

#end of day 2
#practice more 