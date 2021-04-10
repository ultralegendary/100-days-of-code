"""Day 19

"""

#https://leetcode.com/problems/range-sum-of-bst
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        s=0
        stack=[root]
        while stack:
            a=stack.pop()
            if a.val>=low and a.val<=high:
                s+=a.val
            if a.right:
                stack.append(a.right)
            if a.left:
                stack.append(a.left)
        return s

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
