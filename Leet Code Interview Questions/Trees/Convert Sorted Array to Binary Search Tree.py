"""
Here is my solution to the Convert Sorted Array to Binary Search Tree Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return
            
        return treeHouse(nums)
    
        
def treeHouse(nums):
    if len(nums) >= 3:
        halfNum = int(len(nums) / 2)
        root = TreeNode(nums[halfNum])
        root.left = treeHouse(nums[:halfNum])
        root.right = treeHouse(nums[halfNum + 1:])
        return root
    elif len(nums) == 2:
        root = TreeNode(nums[1])
        root.left = TreeNode(nums[0])
        return root
    elif len(nums) == 1:
        x = nums[0]
        root = TreeNode(x)
        return root
