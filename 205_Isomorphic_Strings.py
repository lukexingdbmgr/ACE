from collections import defaultdict

'''
lessions:
    1. tuple can be hashed, not set tuple is immutable; set is mutable-> mutable can't be hashed
    2. two dict d1 == d2 iff key, value map is the same
    3. zip function
    4. set can be used to delete dupliate elements
'''

class Solution(object):
    def hashRes(self, s):
        res = {}
        d = defaultdict(list)

        i = 0
        for c in s:
            d[c].append(i)
            i += 1

        for k, v in d.items():
            if len(v) >= 2:
                ### set can be hashed but not list
                ## h = hash(set(v)) ## this is wrong as set is mutable; can't be the key
                h = hash(tuple(v))
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


if __name__ == "__main__":
    a = "abcde"
    d = "cde"
    l = list(zip(a, d))
    # l = [('a', 'c'), ('b', 'd'), ('c', 'e')]
    print(l)

    a = "egg"
    b = "add"
    ## l = [('e', 'a'), ('g', 'd'), ('g', 'd')]
    l = list(zip(a, b))
    s = set(l)
    print(l)
    ## {('g', 'd'), ('e', 'a')}
    print(s)
