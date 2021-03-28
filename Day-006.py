
#day 006
#https://practice.geeksforgeeks.org/tracks/python-module-6/?batchId=119

#dictionary

d={1:"apple",2:"orange"}
d={"name":"name",2:[1,2,3,4]}
d=dict([(1,("name",23)),(2,"std")])
d={1:"one",2:{1:"one-one",2:"two-two"}}
d["one"]="apple"
print(d["one"])
d.get("one")
del d["one"]
d.pop(1)
d.clear()
str(d)
d.items()
a=d.copy()
d.items()
a.update(d)

from collections import Counter
l=Counter([1,2,3,4,2,3,1,4,5,2,3])


l1,l2,l3=[1,2,3,4,5],[2,3,4,5,6,7],[3,4,5,6,7,8]
l1,l2,l3=Counter(l1),Counter(l2),Counter(l3)
dict(l1.items()&dict(l2.items())&dict(l3.items()))

list_1=[("Nakul",93), ("Shivansh",45), ("Samved",65),
           ("Yash",88), ("Vidit",70), ("Pradeep",52)]
dict_1=dict()

for student,score in list_1:
    dict_1.setdefault(student, []).append(score)