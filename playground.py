class key_value():
    def __int__(self, k, v):
        self.key = k
        self.value = v

    def __lt__(self, other):
        if self.key == other.key:
            return self.value > other.value
        else:
            return self.key < other.key


import collections

d = collections.defaultdict(list)

d[0].append('1')
d[0].append('12')
d[0].append('134')

import functools


class sortedSubscriptions(object):
    def __init__(self, current_assigns):
        self.mp = current_assigns
        self.lst = [1, 23, 4]

    def compare(self, s1, s2):
        ret = self.mp[s1] - self.mp[s2]
        if ret == 0:
            ret = 1 if s1 > s2 else -1
        return ret

    def sort(self, lst):
        return sorted(lst, key=functools.cmp_to_key(self.compare))

    def __iter__(self):
        return self.lst.__iter__()


current_assigns = {"s1": 1, "s2": -200}
lst = ["s1", "s2"]

c = sortedSubscriptions(current_assigns)

for t in c:
    print(t)
