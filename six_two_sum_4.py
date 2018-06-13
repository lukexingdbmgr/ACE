# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.d = {}

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        if (k - root.val) in self.d:
            return True
        self.d[root.val] = 1

        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
