# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMin(self, root, val):
        if root == None:
            return -1
        if root.val != val:
            return root.val
        left = self.findMin(root.left, root.val)
        right = self.findMin(root.right, root.val)

        if left == -1 or right == -1:
            return max(left, right)
        return min(left, right)

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return -1
        return self.findMin(root, root.val)