#https://www.hackerrank.com/domains/python?badge_type=python&filters%5Bstatus%5D%5B%5D=unsolved&filters%5Bdifficulty%5D%5B%5D=medium
#Day 007
"""each probelm link and its solution are given"""
#https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(s):
    
    
    c,v=0,0
    le=len(s)
    for i in range(len(s)):
        if(s[i] in 'AEIOU'):
            v+=le-i
        elif(s[i]not in 'AEIUO'):
            c+=le-i
    if(c>v):
        print("Stuart ",c)
    elif(c<v):
        print("Kevin ",v)
    else:
        print("Draw")
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)

#https://www.hackerrank.com/challenges/list-comprehensions/problem
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k] for i in range(x+1)for j in range(y+1)for k in range(z+1)if (x+y+z)!=n])

#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a,min=arr[0],arr[0]
    for i in arr:
        if(a<i):
            a=i
        if(min>i):
            min=i
    a1=min
    for i in arr:
        if(i>min and a!=i):
            min=i;
            a1=i
    print(a1)

#https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    s,n=[],[]
    from collections import Counter
    for _ in range(int(input())):
        n.append(input())
        s.append(float(input()))
    rank=Counter(s)
    rank.pop(min(rank))
    hi=min(rank)
    a=[]
    for _ in range(len(s)):
        if(s[_]==hi):
            a.append(n[_])
    a.sort()
    for j in a:
        print(j)

#https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format((student_marks[query_name][0]+student_marks[query_name][1]+student_marks[query_name][2])/3))

#https://www.hackerrank.com/challenges/python-string-formatting/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def print_formatted(number):
    [print("{o:>{q:}} {o:>{q:}o} {o:>{q:}X} {o:>{q:}b}".format(o=i,q=len(bin(number))-2))for i in range(1,1+number)]
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)