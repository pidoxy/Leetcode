# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# create a stack
# check if it continues
class Solution:
    def __init__(self):
        self.min = 100000

    def findDepth(self, root, depth):
        if root:
            if root.left or root.right: 
                self.findDepth(root.left, depth+1)
                self.findDepth(root.right, depth+1)
            else:
                self.min = min(self.min, depth)
    def minDepth(self, root: Optional[TreeNode]) -> int: 
        if not root: return 0
        
        self.findDepth(root, depth = 1)
        return self.min 
        # if not root: return 0

        # left, right = 1,1

        # if root.left:
        #     left = 1 + self.minDepth(root.left)
        # if root.right:
        #     right = 1 + self.minDepth(root.right)
        # print(left, right)
        # return min(left, right)


        


        
