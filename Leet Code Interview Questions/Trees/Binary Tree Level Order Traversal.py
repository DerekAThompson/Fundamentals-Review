"""
This is my solution to the Binary Tree Level Order Traversal Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        global trackDict
        global maxLevel
        trackDict = {}
        maxLevel = 0

        level = 0
        if root == None:
            return []
        traverse(root, level)
        returnList = [0] * maxLevel
        for key, value in trackDict.items():
            returnList[int(key - 1)] = value
        return returnList
        
    
def traverse(root, level):
    global trackDict
    global maxLevel
    level += 1
    if level > maxLevel:
        maxLevel = level
    if not root:
        return None
    else:
        try:
            trackDict[level].append(root.val)
        except:
            trackDict[level] = [root.val]
    if root.left:
        traverse(root.left, level)
    if root.right:
        traverse(root.right, level)
    pass