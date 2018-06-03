

'''
s = [1,2,3]

s = [] -> []
s = [1] -> [], + [1]
s = [1,2] -> [], [1], + [2], [1,2]
s = [1,2,3] -> [], [1], [2], [1,2] + [3], [1,3], [2,3], [1,2,3]
'''
import copy
def subSets(s):
    res = [[]]
    for c in s:
        sz = len(res)
        for i in range(sz):
            t = copy.deepcopy(res[i])
            #t = [res[i]]
            t.append(c)
            res.append(t)
    return res

def subSets_recur(s, j, res, sub_res):
    print("j = " + str(j))
    res.append(list(sub_res)) ## point 1 need to care
    for p in range(j, len(s)):
        print(list(range(j, len(s))))
        print("j2 = " + str(j))
        sub_res.append(s[p])
        # subSets_recur(s, j + 1, res, sub_res)
        j = j + 1
        subSets_recur(s, j, res, sub_res)
        sub_res.pop()
        print("_____________________________________")

def subSets_recur_2(s, j, res, sub_res):
    print("j = " + str(j))
    res.append(list(sub_res)) ## point 1 need to care
    p = j
    while(p < len(s)):
        print(list(range(j, len(s))))
        print("j2 = " + str(j))
        sub_res.append(s[p])
        # subSets_recur(s, j + 1, res, sub_res)
        p += 1
        subSets_recur_2(s, p, res, sub_res)
        sub_res.pop()
        print("_____________________________________")



res2 = []
subSets_recur([1,2,3, 10], 0, res2, [])
print(res2)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(subSets([1,2,3, 10]))
