from collections import defaultdict


class Solution(object):
    def hashRes(s):
        res = {}
        d = defaultdict(list)

        for c in s:
            d[c].append(c)

        for k, v in d:
            if len(v) >= 2:
                h = hash(set(v))
                res[h] = 1
        return res

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False

        r1 = self.hashRes(s)
        r2 = self.hashRes(t)
        return r1 == r2
