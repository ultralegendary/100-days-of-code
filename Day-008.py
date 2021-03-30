"""day 8
https://www.hackerrank.com/domains/python?badge_type=python
"""

#https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def print_rangoli(si):
    for i in range(si-1,-1,-1):
        print('-'*i*2,end='')
        q=si
        while(q!=i):
            print(end=chr(96+q))
            if(i!=si-1):
                print(end='-')
            q-=1
        q+=1
        while(q!=si):
            print(end=chr(97+q))
            if(q+1!=si):
                print(end='-')
            q+=1
        print('-'*i*2)

    for i in range(1,si):
        print('-'*i*2,end='')
        q=si
        while(q!=i):
            print(end=chr(96+q))
            if(i!=si-1):
                print(end='-')
            q-=1
        q+=1
        while(q!=si):
            print(end=chr(97+q))
            if(q+1!=si):
                print(end='-')
            q+=1
        print('-'*i*2)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
#https://www.hackerrank.com/challenges/capitalize/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def solve(s):
    
    ss=''
    if s[0]!=' ':
        ss+=s[0].upper()
    for i in range(1,len(s)):
        if(s[i-1]==' 'and s[i]!=' '):
            ss+=s[i].upper()
        else:
            ss+=s[i]
    
    return ss

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(s)

    #fptr.write(result + '\n')

    #fptr.close()
#simple function: return s.title()
