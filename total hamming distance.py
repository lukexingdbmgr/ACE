class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        res = 0
        for i in range(32):
            j = 1 << i ############ not j <<= i
            zezo = 0
            one = 0
            for e in nums:
                if j & e == 0:
                    zezo += 1
                else:
                    one += 1
            res += zezo * one

        return res


import heapq

class min_heap_node:
    def __init__(self, val):
        self.val = val
    def __le__(self, other):
        return self.val[1] > other.val[1]


d = {"a":10, "c": 100, "d":101}


def topk(d, k):
    min_heap = []
    for key in d:
        heapq.heappush(min_heap, (key, d[key]))
        if len(min_heap) == k + 1:
            heapq.heappop(min_heap)

    return min_heap


print(topk(d, 2))

s = Solution()
s.totalHammingDistance([4,14,2])