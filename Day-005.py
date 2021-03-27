#Day 5
#https://practice.geeksforgeeks.org/tracks/python-module-5/?batchId=119

#list
l=[]
l=[1,2,3]
l=["one","two","three"]
l=[[1,2,3],["a","b","c"]]

print(len(l))
l=[]
for i in range(5):
    l.append(i)
l.append((1,2))
l.append(["a","b"])

l.insert(2,"0000")
l.extend([1,2,3])

l=[1,2,3,4]
print(l[0],l[-1],l[-2])

l.remove(2)#removes match

l.pop(2)#pops index

l=list("abcdefghijkl")

#list slicing
l[5:]
l[-1:-5:-1]

if'abc'in l:
    print('abc in list')
'a'not in l

l+=list("olidf")
l*3

l.index('d')

l.sort().reverse()
del l[1]

#sort by length of string
a=list("this is a sentence that is used to sort them in a order".split())
for i in range(len(a)):
    for j in range(i,len(a)):
        k=i
        if(len(a[j])<len(a[k])):
            k=j
        a[i],a[k]=a[k],a[i]

#union
l=list(set([1,2,3,4,5])|set([3,4,5,7,8,9]))
l=set().union([1,2,3,4],[6,4,5,1])
#intresction
l=list(set([1,2,3,4,5])&set([1,4,7,8,9,10]))
set([1,2,43,5]).intersection([1,3,5,6,7])
lst1=[1,2,3,4,5]
lst2=[3,5,6,7,9]
#lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]


#stack
l=["apple","bananna"]
l.append("orange")#push
l.append("graps")#push
l.pop()#pop
#queue
l.pop(0)#pop
l.append("grapes")#push

from collections import deque
a=deque([1,2,3,4,5])
a.pop()
a.append(1)
a.popleft()


#tuples:
t=(1,2,3,4,5)

#practiced some problems
