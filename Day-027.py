"""
Day 27
BIT MANIPULATION
theory:
https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/
https://www.geeksforgeeks.org/bits-manipulation-important-tactics/
problems:
https://leetcode.com/tag/bit-manipulation/


"""

#https://practice.geeksforgeeks.org/problems/equal-sum-and-xor/1
"""n+i=n^i+2(n&i)
-> n&i=0
-> all the possible combinations os unset bits [1<<res(2**res)]
"""
def countValues(n):
    res=0
    while n:
        res+=not n&1
        n>>=1
    return 1<<res

#https://leetcode.com/problems/subsets/
class Solution(object):
    def subsets(self, nums):
        ans=[]
        a=0
        le=len(nums)
        for i in range(1<<le):
            r=[]
            for i in range(le):
                if a&1<<i:
                    r.append(nums[i])
            a+=1
            ans.append(r)
        return ans
#better solution :
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if not nums:
            return ret
        else:
            ret.append([])
            
        # print(ret[0])
        for n in nums:
            length = len(ret)
            print(ret)
            for i in range(length):
                # new = 
                # print(new)
                ret.append(ret[i] + [n])
        return ret


#https://leetcode.com/problems/reverse-bits/
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        ans=0
        for i in range(32):
            ans+=(((n>>i)&1)<<32-i-1)
        return ans
#simple solution
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        newnum = 0
        for i in range(32):
            newnum = (newnum << 1) | (n&1)
            n = n >> 1
            
        return newnum
