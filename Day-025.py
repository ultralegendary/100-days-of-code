"""
Day 25
https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/
"""

#https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3710/
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        Stack=''
        for i in s:
            if not Stack:
                Stack=i
                v=1
                le=1
            else:
                
                Stack+=i
                le+=1
                
                while le>=k:
                    
                    if Stack[-k:]==Stack[-1]*k:
                        Stack=Stack[:-k]
                        le-=k
                    else:
                        break;
        return Stack
