"""Day 22
https://leetcode.com/tag/heap/
https://www.geeksforgeeks.org/heap-data-structure/
"""
#https://www.hackerrank.com/challenges/qheap1/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
def heapify(arr,i,le):
    l,r=2*i+1,2*i+2
    
    if l>=le:
        return arr
    if l<le and arr[l]<arr[i]:
        larg=l
    else:
        larg=i
    if r<le and arr[larg]>arr[r]:        
        larg=r
    if larg!=i:
        arr[i],arr[larg]=arr[larg],arr[i]
        return heapify(arr,larg,le)
    return arr
def heapins(arr,i):
    par=int(i/2-(i%2==0))
    
    if(par>=0 and arr[par]>arr[i]):
        arr[par],arr[i]=arr[i],arr[par]
        return heapins(arr,par)
    
    return arr
arr=[]
le=0
for i in range(int(input())):
    inp=input().split()
    if inp[0]=='1':
        arr.append(int(inp[1]))
        le+=1
        arr=heapins(arr,le-1)
    elif inp[0]=='2':
        
        for j in range(le):
            if arr[j]==int(inp[1]):
                le-=1
                if j<le:
                    arr[j]=arr.pop()
                    
                    arr=heapify(arr,j,le)
                else:
                    arr.pop()
                break
    else:
        print(arr[0])

#https://www.hackerrank.com/challenges/jesse-and-cookies/problem
import os
import sys

#
# Complete the cookies function below.
#
def heapify(arr,i,le):
    l=i*2+1
    r=i*2+2
    if i>=le:
        return arr
    if l<le and arr[l]<arr[i]:
        mini=l
    else:
        mini=i
    if r<le and arr[r]<arr[mini]:
        mini=r
    if mini!=i:
        arr[mini],arr[i]=arr[i],arr[mini]
        return heapify(arr,mini,le)
    return arr

def insheap(arr,i,le):
    par=int(i/2-(i%2==0))
    if par>=0 and arr[par]>arr[i]:
        arr[i],arr[par]=arr[par],arr[i]
        return insheap(arr,par,le)
    return arr

def cookies(k, A):
    
    le=len(A)
    ans=0
    mi1=0
    
    for i in range(le):
        A=heapify(A,le-1-i,le)
    while A and A[0]<k:
        if le==1:
            if A[0]>=k:
                return ans
            else:
                return -1
        elif le==2:
            mi2=1
            temp=A.pop()
            le-=1
            A[0]+=temp*2
            
        else:
            if A[1]>A[2]:
                temp=2
            else:
                temp=1
            A[0]+=A[temp]*2
            if le==3:
                if temp==2:
                    A[1]=(A[1] if A[1]<=A[2]else A[2])
                A.pop()#corner prolly
                le-=1
            else:
                
                A[temp]=A.pop()
                le-=1
                A=heapify(A,temp,le)
                A=heapify(A,0,le)
            
            
        ans+=1
        
    if not( A )or A[0]<k:
        return -1
    else:
        return ans
    
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()