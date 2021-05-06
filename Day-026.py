"""
day-26
"""



#https://leetcode.com/problems/flood-fill/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack=[[sr,sc]]
        r,c=len(image),len(image[0])
        visited=[[True for i in range(c)]for j in range(r)]
        old=image[sr][sc]
        visited[sr][sc]=0
        while stack:
            sr,sc=stack.pop()
            image[sr][sc]=newColor
            if sr-1>=0 and visited[sr-1][sc]and image[sr-1][sc]==old:
                stack.append([sr-1,sc])
                visited[sr-1][sc]=0
            if sc-1>=0 and visited[sr][sc-1]and image[sr][sc-1]==old:
                stack.append([sr,sc-1])
                visited[sr][sc-1]=0
            if sr+1<r and visited[sr+1][sc]and image[sr+1][sc]==old:
                stack.append([sr+1,sc])
                visited[sr+1][sc]=0
            if sc+1<c and visited[sr][sc+1]and image[sr][sc+1]==old:
                stack.append([sr,sc+1])
                visited[sr][sc+1]=0
        return image


#https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        visi=[0]*V
        
        app=[0]
        res=[0]
        while app:
            a=app.pop(0)
            visi[a]=1
            for i in adj[a]:
                if not visi[i]:
                    visi[i]=1
                    res.append(i)
                    app.append(i)
        
        
        return res


#https://leetcode.com/problems/minimum-distance-between-bst-nodes/
class Solution(object):
    def __init__(self):
        self.diff=10**5
        self.a=[]
        self.len=0
    def minDiffInBST(self, root):
        
        if(self.len>=2):
            self.diff=min(self.diff,self.a[-1]-self.a[-2])
        
        if root.left:
            self.minDiffInBST(root.left)
            
        self.a.append(root.val)
        self.len+=1
        if root.right:
            self.minDiffInBST(root.right)
        if(self.len>=2):
            self.diff=min(self.diff,self.a[-1]-self.a[-2])
        return self.diff
        