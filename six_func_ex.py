class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = {}
        stk = []
        last_call_time = 0
        for log in logs:
            cur_id, cur_status, cur_time = tuple(log.split(':'))
            if cur_status == 'start':
                stk.append(log)
            elif cur_status == 'end':
                top = stk[-1]
                top_id, top_status, top_time = tuple(top.split(':'))
                elapse = int(cur_time) - int(top_time) - int(last_call_time) + 1
                res[top_id] = elapse
                last_call_time += elapse  ## should += not =
                stk.pop()
        res_list = []
        keys = sorted(res)
        for key in keys:
            res_list.append(res[key])
        return res_list

logs = [
    "0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"
]
sl = Solution()
print(sl.exclusiveTime(7, logs))
