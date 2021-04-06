#Day -15

#stack

#https://www.hackerrank.com/challenges/maximum-element/problem
def getMax(operations):
    ma=lambda b,a:a if a>b else b
    l=[]
    for i in operations:
        if i[0]=='1':
            if(not l):
                l.append(int(i.split()[1]))
            else:
                l.append(ma(int(i.split()[1]),l[-1]))
        elif i[0]=='2':
            l.pop()
        else:
            yield l[-1]

#https://www.hackerrank.com/challenges/balanced-brackets/problem
def isBalanced(s):
    ss=[]
    for i in s:
        if i in '{[(':
            ss.append(i)
        else:
            if not ss:
                return 'NO'
            if i==']'and ss[-1]=='[':
                ss.pop()
            elif i=='}'and ss[-1]=='{':
                ss.pop()
            elif i==')'and ss[-1]=='(':
                ss.pop()
            else:
                return 'NO'
    if ss:
        return 'NO'
    return 'YES'

#https://www.hackerrank.com/challenges/equal-stacks/problem
def equalStacks(h1, h2, h3):
    a1,a2,a3=[0],[0],[0]
    h1.reverse()
    h2.reverse()
    h3.reverse()
    for i in h1:
        a1.append(i+a1[-1])
    for i in h2:
        a2.append(a2[-1]+i)
    for i in h3:
        a3.append(a3[-1]+i)
    i1,i2,i3=-1,-1,-1
    while not (a2[i2]==a3[i3]==a1[i1] and a2[i2]==a1[i1]):
        if(a1[i1]>a2[i2]and a1[i1]>a3[i3]):
            i1-=1
        elif a2[i2]>a1[i1]and a2[i2]>a3[i3]:
            i2-=1
        elif a3[i3]>a1[i1]and a3[i3]>a2[i2]:
            i3-=1
        elif(a1[i1]>a2[i2]or a1[i1]>a3[i3]):
            i1-=1
        elif a2[i2]>a1[i1]or a2[i2]>a3[i3]:
            i2-=1
        elif a3[i3]>a1[i1]or a3[i3]>a2[i2]:
            i3-=1
        
    return a2[i2]

#https://www.hackerrank.com/challenges/game-of-two-stacks/problem
def twoStacks(maxSum, a, b):
    
    sumsa,sumsb=0,0
    ini=0
    for i in a:
        if not(sumsa+i<=maxSum):
            break
        sumsa+=i
        
        ini+=1
    res=ini
    j,lb=0,len(b)
    while ini>=0 and j<lb:
        sumsa+=b[j]
        j+=1
        while maxSum<sumsa and ini>0:
            ini-=1
            sumsa-=a[ini]
            
        if sumsa<=maxSum and ini+j>res:
                res=j+ini
        
    return res

#https://www.hackerrank.com/challenges/largest-rectangle/problem
#histogram problem
def largestRectangle(h):
    s=[]
    i,l=0,len(h)
    maxarea=-1
    
    index=0
    while(i<l):
        if not s or h[s[-1]]<=h[i]:
            s.append(i)
            i+=1
        else:
            a=s.pop()
            if s:
                area=h[a]*(i-1-s[-1])
            else:
                area=h[a]*i
            maxarea=max(area,maxarea)
    while s:
        a=s.pop()
        if s:
            area=h[a]*(i-1-s[-1])
        else:
            area=h[a]*i
        maxarea=max(area,maxarea)
    return maxarea

    