"""binary tree


"""

#https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
#recrusive: 
def preOrder(root):
    print(root.info,end=' ')
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
#itrative:
def preOrder(root):
    stack=[root]
    while(stack):
        a=stack.pop()
        print(a.info,end=' ')
        if(a.right):
            stack.append(a.right)
        if a.left:
            stack.append(a.left)

#https://www.hackerrank.com/challenges/tree-postorder-traversal/problem
#recursice:
def postOrder(root):
    if(root.left):
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(root.info,end=' ')
#itreative:
def postOrder(root):
    queue=[]
    stack=[root]
    while stack:
        a=stack.pop()
        queue.append(a.info)
        if a.left:
            stack.append(a.left)
        if a.right:
            stack.append(a.right)
    for i in range(len(queue)):
        print(queue[-i-1],end=' ')

#https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
def inOrder(root):
    if root.left:
        inOrder(root.left)
    print(root.info,end=' ')
    if root.right:
        inOrder(root.right)
#itreative:
def inOrder(root):
    cur=root
    stack=[]
    q=[]
    while True:
        while cur:
            stack.append(cur)
            cur=cur.left
        cur=stack.pop()
        print(cur.info,end=' ')
        cur=cur.right
        if not (cur or stack):
            break
"""
today leet code challenge
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3702/
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d,l={},[]
        for i in range(len(order)):
            d[order[i]]=i
        print(d)
        for i in words:
            l.append([d[j]for j in i])
        for i in range(1,len(l)):
            if l[i-1]>l[i]:
                return False
        
        return True
        
#https://leetcode.com/problems/binary-tree-inorder-traversal/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l=[]
        ans=[]
        a=root
        while True:
            if not(a or l):
                break
            
            while a:
                l.append(a)
                a=a.left
            a=l.pop()
            ans.append(a.val)
            a=a.right
            
        return ans