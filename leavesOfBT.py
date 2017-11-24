# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves_help(self, root, res):
        if root == None:
            ## for empty ; h = 0
            return 0

        h = max(self.findLeaves_help(root.left, res), self.findLeaves_help(root.right, res))
        if len(res) == h:
            res.append([root.val])
        else:
            res[h].append(root.val)
        return h + 1

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.findLeaves_help(root, res)
        return res
