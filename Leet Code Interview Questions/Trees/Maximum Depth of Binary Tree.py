"""
Here is my solution to the Maximum Depth of Binary Tree Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global maxLevel
        level = 0
        maxLevel = 0
        
        
        traverse(root, level)
        return maxLevel

def traverse(root, level):
    global maxLevel
    level += 1
    if root:
        if level > maxLevel:
            maxLevel = level
        if root.left:
            traverse(root.left, level)
        if root.right:
            traverse(root.right, level)
    pass
        