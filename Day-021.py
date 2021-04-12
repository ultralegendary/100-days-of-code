"""day 21

https://leetcode.com/problemset/all/?topicSlugs=binary-search-tree

"""

#https://leetcode.com/problems/convert-bst-to-greater-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        ans=TreeNode()
        change=ans
        stack=[root]
        s=0
        a=root
        while stack and a:
            
            
            while a.right:
                stack.append(a.right)
                a=a.right
            a=stack.pop()
            print(s,end='|')
            s+=a.val
            a.val=s
            
            if a.left:
                stack.append(a.left)
                a=a.left
            else:
                a=TreeNode()
        return root