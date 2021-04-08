"""Day 17
QUEUE
"""
#https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
q=[]
for i in range(int(input())):
    l=input().split()
    if(l[0]=='1'):
        q.append(int(l[1]))
    elif l[0]=='2':
        q.pop(0)
    else:
        print(q[0])

#https://www.hackerrank.com/challenges/truck-tour/problem
def truckTour(petrolpumps):
    litre,dis=[],[]
    res,index=0,0
    
    for i in petrolpumps:
        if not litre:
            res=index
            litre.append(i[0])
            dis.append(i[1])
        else:
            litre.append(litre[-1]+i[0])
            dis.append(dis[-1]+i[1])
        if litre[-1]<dis[-1]:
            litre,dis=[],[]
        index+=1
    return res