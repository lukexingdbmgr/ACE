class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        ###sorted(intervals, key=lambda inter: inter.start)
        intervals.sort(key=lambda x: x.start)
        ## trap ###
        prev = intervals.pop(0)

        res = []
        while (len(intervals) > 0):
            curr = intervals.pop(0)
            if prev.end < curr.start:
                res.append(prev)
                prev = curr
            else:
                prev = Interval(prev.start, max(curr.end, prev.end))

        res.append(prev)

        return res


s = Solution()
l = [Interval(1, 4), Interval(0, 0)]
s.merge(l)
