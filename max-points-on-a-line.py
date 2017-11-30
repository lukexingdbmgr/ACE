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
        key_tuple = {}

        for p in points:
            x, y = p.x, p.y
            ##  key = hash((x, y)) % 90839 is not reliable
            key = str(x) + "#" + str(y)  ## use string to give the unique k
            key_tuple[key] = (x, y)
            ## de-dup
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
        for k, (x, y) in key_tuple.items():
            dd = {}
            for k1, (x1, y1) in key_tuple.items():
                if k == k1:
                    continue
                s = self.getSlop(x, y, x1, y1)
                if s not in dd:
                    dd[s] = num_dict[k1]
                else:
                    dd[s] += num_dict[k1]

            vs = dd.values()
            if vs:
                mx = max(vs)
                m = max(m, mx + num_dict[k])
            else:
                m = max(m, num_dict[k])

        return m


if __name__ == "__main__":
    c = Point(0, 0)
    s = Solution()
    l = [[84, 250], [0, 0], [1, 0], [0, -70], [0, -70], [1, -1], [21, 10], [42, 90], [-42, -230]]
    # l = [[1,1],[1,1],[1,0],[1,0], [1,-1], [1, -1]]
    fl = []
    for c in l:
        p = Point(c[0], c[1])
        fl.append(p)
    print(s.maxPoints(fl))

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