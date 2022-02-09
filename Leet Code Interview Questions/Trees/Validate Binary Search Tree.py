"""
Here is my solution to the Validate Binary Search Tree Problem
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        global treeList
        treeList = []
        if not root.left and not root.right:
            return True
        rootCompare(root)
        sortList = sorted(treeList)
        if treeList != sortList or float('-inf') in treeList:
            return False

        if len(treeList) != len(set(treeList)):
            return False
        return True

def rootCompare(root):
    global treeList
    if root:
        if root.left and root.left.val >= root.val:
            treeList.append(float('-inf'))
        elif root.right and root.right.val <= root.val:
            treeList.append(float('-inf'))
        rootCompare(root.left)
        treeList.append(root.val)
        rootCompare(root.right)
    pass
