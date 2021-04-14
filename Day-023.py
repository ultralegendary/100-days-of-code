"""
Day 23
Hashing
https://leetcode.com/tag/hash-table/
https://www.geeksforgeeks.org/hashing-data-structure/
"""

#https://leetcode.com/problems/two-sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a={}
        for i,n in enumerate(nums):
            if target-n in a:
                return [i,a[target-n]]
            else:
                a[n]=i

#https://leetcode.com/problems/sum-of-unique-elements/
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        s=0
        for i in nums:
            if i not in a:
                a[i]=1
                s+=i
            elif a[i]==1:
                a[i]+=1
                s-=i
        return s

#https://leetcode.com/problems/word-pattern/submissions/
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ss=s.split()
        if len(ss)!=len(pattern):
            return False
        dic={}
        dic2={}
        for i,j in zip(*[ss,pattern]):
            if j in dic:
                if i!=dic[j]:
                    return False
                
            else:
                if i in dic2:
                    return False
                dic[j]=i
                dic2[i]=j
                
        return True

#https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            d=set()
            for j in i:
                if j.isdigit() and j in d:
                    return False
                elif j.isdigit():
                    d.add(j)
        print(1)
        for i in range(9):
            d=set()
            for j in range(9):
                if board[j][i].isdigit() and board[j][i]in d:
                    return False
                elif board[j][i].isdigit():
                    d.add(board[j][i])
        print(2)
        for i in range(3):
            for j in range(3):
                d=set()
                for k in range(3):
                    
                    for l in range(3):
                        t=board[i*3+k][j*3+l]
                        if t.isdigit()and t in d:
                            return False
                        elif t.isdigit():
                            d.add(t)
        
        return True

#https://leetcode.com/problems/count-primes/
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        
        b=[True]*(n)
        b[0]=b[1]=False
        
        p = 2
        while (p * p <= n):
          
        # If prime[p] is not changed, then it is a prime
            if (b[p]):
              
            
                for i in range(p * 2, n  , p):
                    b[i] = False
            p += 1
        
        return b.count(True)