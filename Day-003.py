#https://practice.geeksforgeeks.org/tracks/python-module-3/?batchId=119
#day 3


string="hello"
print(id(string))
print(id("hello"))
string+=" "
print(id(string))
#different id because string is unmutable

string="""hellos this's" is a string"""
print(string)

#string slicing
print(string[5])
print(string[5:10])
print(string[5:])
print(string[5::2])


#string reverse
print(string[::-1])


#string functions

print(string.find("i",10))
print(string.rfind("i"))
print(string.startswith('e',1))
print(string.endswith(('g')))
print(string.islower())

len(string)
string.count("i",4)
string.center(40,'|')
"JoIn".join(["string","is","joined"])

string="---string---"
string.strip('-')
string.lstrip('-')
string.rstrip('-')
min(string)
max(string)

string.replace('-', '_')
string.expandtabs()


#string to list
string="this is a string"
list=string.split()

l=[]
l[:0]=string


#regex program
#only one example here, visit https://www.geeksforgeeks.org/pattern-matching-python-regex/

import re

def Find(string):

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]

string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/'
print("Urls: ", Find(string))

#escape secquence : 
string="\"strin\n\t\a"

#string format
string="{} code {} between {}".format("this","has been","inserted")

#practice these links too:
#https://www.geeksforgeeks.org/pattern-matching-python-regex/
#https://www.geeksforgeeks.org/python-format-function/
