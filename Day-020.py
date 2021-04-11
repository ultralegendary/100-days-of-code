#https://atcoder.jp/contests/abc198/tasks
#A-DIV:
print(int(input())-1)

#B- palindrome 0
a=input()
a=a[-1::-1]
for i in range(len(a)):
  if a[i]!='0':
    break
a=a[i:]
for i in range(int(len(a)/2)):
      if a[i]!=a[-i-1]:
        print("No")
        break
else:
    print("Yes")

#C- compas walking
s,x,y=list(map(int,input().split()))
dis=(x*x+y*y)**(1/2)
if dis<s:
  print(2)
elif dis==s:
  print(1)
elif dis%s:
  print(int(dis/s)+1)
else:
  print(int(dis/s))

#d