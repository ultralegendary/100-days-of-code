""" Day 009

Same as yesterdays link
"""

#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(s, k):
    l=[s[i:i+k] for i in range(0,len(s),k)]
    ss=[]
    for i in range(len(l)):
        ss.append(l[i][0])
        for a in l[i]:
            if a not in ss[i]:
                ss[i]+=a
    for i in ss:
        print(i)
        
        
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int, input().split()))
a=int(input())
for i in range(a):
    l=input().split()
    if l[0]=='pop':
        s.pop()
    elif l[0]=='remove':
        s.remove(int(l[1]))
    elif l[0]=='discard':
        s.discard(int(l[1]))
sum=0
for i in s:
    sum+=i
print(sum)

#https://www.hackerrank.com/challenges/py-set-union/problem
a=int(input())
l1=set(map(int,input().split()))
a=int(input())
l1=l1|set(map(int,input().split()))
print(len(l1))

#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
a=int(input())
l1=set(map(int,input().split()))
a=int(input())
l1=l1&set(map(int,input().split()))
print(len(l1))

#https://www.hackerrank.com/challenges/py-set-difference-operation/problem
a=int(input())
l1=set(map(int,input().split()))
a=int(input())
l1=l1-set(map(int,input().split()))
print(len(l1))

#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
a=int(input())
l1=set(map(int,input().split()))
a=int(input())
l1=l1^set(map(int,input().split()))
print(len(l1))

#https://www.hackerrank.com/challenges/py-set-mutations/problem
int(input())
l1=set(map(int,input().split()))

for i in range(int(input())):
    a=input().split()
    if a[0]=='intersection_update':
        l1&=set(map(int,input().split()))
    elif a[0]=='update':
        l1|=set(map(int,input().split()))
    elif a[0]=='symmetric_difference_update':
        l1^=set(map(int,input().split()))
    else:
        l1-=set(map(int,input().split()))
print(sum(l1))

#https://www.hackerrank.com/challenges/py-the-captains-room/problem
s=int(input())
l=list(map(int,input().split()))
l1=[0 for i in range(len(l))]
for i in l:
    l1[i]+=1
for i in range(len(l1)):
    if l1[i]==1:
        print(i)
        break

#https://www.hackerrank.com/challenges/py-check-subset/problem
for i in range(int(input())):
    int(input())
    l1=set(map(int,input().split()))
    int(input())
    l2=set(map(int,input().split()))
    if(l1&l2==l1):
        print("True")
    else :
        print("False")
        
#https://www.hackerrank.com/challenges/py-check-strict-superset/problem
l=set(map(int,input().split()))
s=int(input())
l1=set([])
a=0
for i in range(s):
    l1=set(map(int,input().split()))
    if l&l1==l1 and len(l1)!=len(l):
        a+=1
    else:
        break
        
if(a==s):
    print("True")
else:
    print("False")
    
#https://www.hackerrank.com/challenges/zipped/problem
a,b=tuple(map(int,input().split()))
l=[]
for i in range(b):
    l.append(list(map(float,input().split())))
for i in zip(*l):
    s=0
    for j in range(b):
       s+=i[j] 
    print('{:.1f}'.format(s/b))

#https://www.hackerrank.com/challenges/input/problem
x,k=list(map(int,input().split()))
if(eval(input())==k):
    print("True")
else:
    print("False")
