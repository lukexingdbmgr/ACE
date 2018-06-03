# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# ACE #

class Solution(object):
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)

    def getSlop(self, x, y, x1, y1):
        if x == x1:
            return float('inf')
        y = y - y1
        x = x - x1
        g = self.gcd(x, y)
        return (x / g, y / g)
        # return float((y - y1) / (x - x1))

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        num_dict = {}

        for p in points:
            x, y = p.x, p.y
            key = (x, y)
            if key not in num_dict:
                num_dict[key] = 1
            else:
                num_dict[key] += 1

        # for k, v in num_dict.items():
        #    print("key = " , k)
        #    print("num = ", v)

        # print("-"*101)
        m = 0
        sub = 0
        lst = list(num_dict.keys())  ##TypeError: 'dict_keys' object does not support indexing
        if len(lst) == 1:
            return num_dict[lst[0]]

        ## lst = [(1,2), (4,5), (10,1)]
        for i in range(len(lst) - 1):
            dd = {}
            for j in range(i + 1, len(lst)):

                x, y = lst[i]
                x1, y1 = lst[j]

                s = self.getSlop(x, y, x1, y1)
                if s not in dd:
                    dd[s] = num_dict[lst[j]]
                else:
                    dd[s] += num_dict[lst[j]]

            vs = dd.values()
            if vs:
                mx = max(vs)
                m = max(m, mx + num_dict[lst[i]])
            else:
                m = max(m, num_dict[lst[i]])

        return m


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution9(object):

    def isSameTree(self, s, t):
        ## 0 0 case
        if s == None and t == None:
            return True
        ## 0 1 and 1 0 case
        if (s and not t) or (not s and t):
            return False
        if s.val != t.val:
            return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None:
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == "__main__":
    s = TreeNode(4)
    s.left = TreeNode(1)
    s.right = TreeNode(2)
    s.right.left = TreeNode(0)

    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)

    a = 1
    b = 1

    print(not a or not b)
    if (a != None) or (b != None):
        print("shock")

    s9 = Solution9()
    print(s9.isSubtree(s, t))

'''
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import numpy as np

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        mm = {}
        for p in points:
            mm[(p.x,p.y)] = mm.get((p.x,p.y), 0) + 1
        P = mm.keys()    
        if len(P) == 1:
            return mm[P[0]]
        maxP = 0
        for i in xrange(len(P)-1):
            slopes,repCnt = {},1
            for j in xrange(i+1,len(P)):
                dx,dy = P[i][0]-P[j][0],P[i][1]-P[j][1]
                if dx == 0:
                    slope = "#"
                elif dy == 0:
                    slope = 0
                else:
                    slope = float(dy) / dx
                slopes[slope] = slopes.get(slope,0) + mm[P[j]]
                
            maxP = max(maxP, mm[P[i]] + max(slopes.values()))
        return maxP
                
'''