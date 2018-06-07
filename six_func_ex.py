def calculate_logs(logs):
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
            elapse =  int(cur_time) - int(top_time) - int(last_call_time)
            res[top_id] = elapse
            last_call_time = elapse
            stk.pop()
    print(res)

logs = [

'1:start:0',
'2:start:3',

'3:start:5',
'3:end:19',

'2:end:24',
'1:end:90'
]

calculate_logs(logs)
