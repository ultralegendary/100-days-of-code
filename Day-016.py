"""Day-016
Stack
"""

#https://www.hackerrank.com/challenges/simple-text-editor/problem
n=int(input())
l=''
backtrack=[]
for i in range(n):
    s=input().split()
    if(s[0]=='1'):
        backtrack.append(l)
        l+=s[1]
    elif(s[0]=='2'):
        backtrack.append(l)
        l=l[:-int(s[1])]
    elif(s[0]=='3'):
        
        print(l[int(s[1])-1])
    else:
        
        l=backtrack.pop()

#https://www.hackerrank.com/challenges/poisonous-plants/problem
def poisonousPlants(p):
    l=[]
    for i in p:
        if not l or l[-1][-1]<i:
            l.append([i])
        else:
            l[-1].append(i)
    le=len(l)
    day=0
    while True:
        u=0
        if(le<2):
            return day
        
        day+=1
        i=1
        while i<le:
            l[i].pop(0)
            if not l[i]:
                l.pop(i)
                le-=1
                
            else:
                i+=1
        if(le<2):
            return day
        i=-1
        while i>-le:
            if l[i-1][-1]>=l[i][0]:
                l[i-1].extend(l[i])
                l.pop(i)
                le-=1
            else :
                i-=1
        if(le<2):
            return day


#https://www.hackerrank.com/challenges/and-xor-or/problem
def andXorOr(a):
    s=[]
    a1,b1=a[0],a[1]
    res=(((a1&b1)^(a1|b1))&(a1^b1))
    for i in a:
        while s:
            a1,b1=i,s[-1]
            res=max((((a1&b1)^(a1|b1))&(a1^b1)),res)
            if i<s[-1]:
                s.pop()
            else:
                break
        s.append(i)
    return res
