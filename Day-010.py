"""Day 010
problem solving
"""

#https://www.hackerrank.com/challenges/python-sort-sort/problem
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    s=sorted(arr,key=lambda x:x[k])
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=' ')
        print()
#editorial:
n,m = map(int,input().split())
lst = []
for i in range(n):
    lst.append(map(int,input().split()))
k = int(input())
print("\n".join(map(lambda x: " ".join(map(str, x)), sorted(lst, key = lambda x: x[k]))))

#https://www.hackerrank.com/challenges/any-or-all/problem
n=int(input())
s=input().split()
print(all([int(i)>0 for i in s]+[any(i==i[::-1] for i in s)]))

#https://www.hackerrank.com/challenges/ginorts/problem
import string
s=input()
even,odd,big,small=[''for i in range(4)]
for i in s:
    if i in string.ascii_lowercase:
        small+=i
    elif i in string.ascii_uppercase:
        big+=i
    else:
        if int(i)&1:
            odd+=i
        else:
            even+=i
s=[]
s+=sorted(small)
s+=sorted(big)
s+=sorted(odd)
s+=sorted(even)
for i in s:
    print(end=i)

#https://www.hackerrank.com/challenges/calendar-module/problem
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
import calendar
m,d,y=map(int,input().split())
print(days[calendar.weekday(y,m,d)])
