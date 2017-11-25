# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         similar to 206. Reverse Linked List

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        cur = prev = next = lastRight = None

        cur = root
        while (cur != None):
            next = cur.left  # save
            cur.left = lastRight  # change

            right = cur.right  # save
            cur.right = prev  # change

            ## state change
            prev = cur
            cur = next
            lastRight = right
        return prev


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#       TODO: replay this

class Solution2(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left and not root.right: return root
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return newRoot
