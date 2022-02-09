"""
Here is my solution to the Symmetric Tree Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# set level = 0
# recursion function w/ level indicator and incrementor
# append to dict a list with level as key and node value to list
# for each item in dict
# Check if item = item[::-1] (palindrome)





class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        level = 0
        global symmetryDict
        symmetryDict = {}
        buildDict(root, level)
        for key, value in symmetryDict.items():
            if value != value[::-1]:
                return False
        return True
        
        
        
def buildDict(root, level):
    level += 1
    if root:
        try:
            symmetryDict[level].append(root.val)
        except:
            symmetryDict[level] = [root.val]
        buildDict(root.left, level)
        buildDict(root.right, level)
    else:
        try:
            symmetryDict[level].append(float('inf'))
        except:
            symmetryDict[level] = [float('inf')]
            
            
        
        
        
        
        
        
        