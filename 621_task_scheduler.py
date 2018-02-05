## https://www.youtube.com/watch?v=hvI-rJyG4ik
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        for c in tasks:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        mx = max(d.values())
        mx_num = 0
        for t in d.values():
            if t == mx:
                mx_num += 1
        ans = (mx - 1) * (n + 1) + mx_num
        return max(ans, len(tasks))



s = Solution()

s.leastInterval(tasks=["A","A","A","B","B","B"], n=2)