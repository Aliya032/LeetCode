# 00:11 03-06-2024
# https://leetcode.com/problems/symmetric-tree/submissions/1275604714/
# video solution: https://www.youtube.com/watch?v=Mao9uzxwvmc


from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

class Solution: 
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val and 
                    dfs(left.left, right.right) and 
                    dfs(left.right, right.left))

        return dfs(root.left, root.right)
    

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(4, TreeNode(4), TreeNode(3))

s1solution = Solution()
print(s1solution.isSymmetric(root))