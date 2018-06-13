class Solution(object):
    ###https://leetcode.com/problems/maximum-swap/discuss/107073/C++-one-pass-simple-and-fast-solution:-1-3ms-O(n)-time
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        i = len(s) - 1
        left_idx = 0
        right_idx = 0
        max_value = -1
        max_idx = -1

        while (i >= 0):
            p = int(s[i])
            ## find the max value so far;
            if p > max_value:
                max_value = p
                max_idx = i
                #############be ver careful
                i -= 1
                #############be ver careful
                continue

            ## find the one in the most front smaller than max_value
            if p < max_value:
                left_idx = i
                right_idx = max_idx
                print(left_idx)
                print(right_idx)
            i -= 1

        s[left_idx], s[right_idx] = s[right_idx], s[left_idx]

        return int(''.join(s))


s = Solution()
print(s.maximumSwap(2736))
