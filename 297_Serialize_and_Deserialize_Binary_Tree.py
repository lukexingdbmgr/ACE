# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize_help(self, root, ans):
        if root == None:
            ans.append('#')
            return
        ans.append(str(root->val))
        self.serialize_help(root.left, ans)
        self.serialize_help(root.right, ans)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        self.serialize_help(root, ans)
        return ','.join(ans)  ## array to string

    def des_helper(self, d_i)
        v = next(d_i)
        if v == '#':
            return None
        nnd = TreeNode(int(v))
        nnd.left = self.des_helper(self, d_i)
        nnd.right = self.des_helper(self, d_i)

        return nnd

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        d = data.split(',')
        d_i = iter(d)
        return self.des_helper(d_i)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))




class Codec_answer:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        self.preOrder(root, ans)
        ## make ans to a string
        return ','.join(ans)

    def preOrder(self, root, ans):
        if root is None:
            ans.append("#")
            return

        ans.append(str(root.val))
        self.preOrder(root.left, ans)
        self.preOrder(root.right, ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = iter(data.split(','))
        return self.build(nodes)

    def build(self, nodes):
        # val = nodes.pop(0)
        val = next(nodes)
        if val == "#":
            return None

        node = TreeNode(val)
        node.left = self.build(nodes)
        node.right = self.build(nodes)
        return node


if __name__ == "__main__":
    rt = TreeNode(0)
    left = TreeNode(100)
    right = TreeNode(10)

    rt.left = left
    left.right = right

    d = Codec()
    d.serialize(rt)
    root = d.deserialize()

'''
>>> f = [1,2,3,44]
>>> ','.join(f)
TypeError: sequence item 0: expected str instance, int found
>>> f = ['12', '12', '34']
>>> ','.join(f)
'12,12,34'
>>> q = ','.join(f)
>>> q
'12,12,34'
>>> a = q.split(',')
>>> a
['12', '12', '34']
>>> c = iter(a)
>>> next(c)
'12'
'''
