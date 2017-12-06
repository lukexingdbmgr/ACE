class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        sorted(intervals, key=lambda inter: inter.start)
        ## trap ###
        prev = intervals.pop(0)

        res = []
        while (len(intervals) > 0):
            curr = intervals.pop(0)
            if prev.end < curr.start:
                res.append(prev)
                prev = curr

            if prev.end >= curr.start:
                prev = Interval(min(prev.start, curr.start), max(curr.end, prev.end))

        res.append(prev)

        return res
