"""
Day 11
https://www.hackerrank.com/domains/data-structures

"""

#array rotation:
arr=map(int,input().split())
d=int(input())
d%=len(arr)
arr=arr[d:]+arr[:d]

#