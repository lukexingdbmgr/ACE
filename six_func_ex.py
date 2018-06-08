class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = {}
        stk = []
        for log in logs:
            cur_id, cur_status, cur_time = tuple(log.split(':'))
            if cur_status == 'start':
                stk.append(log)
            elif cur_status == 'end':
                top = stk[-1]
                top_id, top_status, top_time = tuple(top.split(':'))
                elapse = int(cur_time) - int(top_time) + 1
                if top_id in res:
                    res[top_id] += elapse
                else:
                    res[top_id] = elapse
                stk.pop()
                for l in stk:
                    pre_id, pre_status, pre_time = l.split(':')
                    if pre_id in res:
                        res[pre_id] -= elapse
                    else:
                        res[pre_id] = -elapse

        res_list = []
        keys = sorted(res)
        for key in keys:
            res_list.append(res[key])
        return res_list


logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]

sl = Solution()
print(sl.exclusiveTime(7, logs))


### the answer

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stk = []
        pre_time = 0
        res = [0] * n
        for log in logs:
            s = log.split(':')

            cur_id = int(s[0])
            cur_status = s[1]
            cur_time = int(s[2])

            if cur_status[0] == 's':
                if len(stk):
                    res[stk[-1]] += cur_time - pre_time
                pre_time = cur_time
                stk.append(cur_id)
            elif cur_status[0] == 'e':
                top = stk[-1]
                ###Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time.
                elapse = cur_time - pre_time + 1
                res[top] += elapse
                pre_time = cur_time + 1
                stk.pop()

        return res
