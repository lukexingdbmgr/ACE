### https://discuss.leetcode.com/topic/96884/very-simple-java-solution-with-detail-explanation/2

class Solution(object):
    res = 0

    def count(self, s, i, j):
        n = len(s)
        while (i >= 0 and j < n and s[i] == s[j]):
            i -= 1
            j += 1
            self.res += 1

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        for i in range(
                len(s)):  ## not len(s) - 1; "abc" when i point to 'c'; need to test the last one;  i is the mid point
            self.count(s, i, i)  ## fot the last element; here will add 1; the following line returns
            self.count(s, i, i + 1)

        return self.res


s = Solution()
s.countSubstrings("abc")
