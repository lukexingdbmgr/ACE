# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        cur = prev = next = lastRight = lastRight = None

        cur = root
        while (cur != None):
            next = cur.left  # save
            cur.left = prev  # change
            right = cur.right  # save
            cur.right = lastRight  # change

            ## state change
            prev = cur
            cur = next
            lastRight = right
