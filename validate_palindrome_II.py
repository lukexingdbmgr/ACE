class Solution(object):
    def valid_impl(self, s, k):
        t = 0
        j = len(s) - 1
        while (t <= j):
            if t == k or j == k:
                t += 1
                j -= 1
                continue
            if s[t] != s[j]:
                return False
            t += 1
            j -= 1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while (i <= j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if self.valid_impl(s, i) or self.valid_impl(s, j):
                    return True
                else:
                    return False
        return True



s = Solution()
s.validPalindrome("abc")