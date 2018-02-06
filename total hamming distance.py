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



s = Solution()
s.totalHammingDistance([4,14,2])