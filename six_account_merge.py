class Solution(object):
    def merge(self, accs, prev_id, current_id):
        if prev_id != current_id:
            # !accs[prev_id].append(accs[current_id][1:]) <<<<< 1
            # !accs[prev_id].append(c for c in accs[current_id][1:]) <<<< 2
            for c in accs[current_id][1:]:
                accs[prev_id].append(c)

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_id_map = {}
        l = len(accounts)
        j = 0
        ###!! for j in range(len(accounts))
        ### if you can use while; don't use for .. range
        while j < len(accounts):
            acc = accounts[j]
            for mail in acc[1:]:
                if mail in email_id_map:
                    id = email_id_map[mail]
                    if id != j:
                        self.merge(accounts, id, j)
                        ## push all the mail to id map
                        for mail in acc[1:]:
                            email_id_map[mail] = id
                        accounts[j][0] = "!xxxx"
                        break
                else:
                    email_id_map[mail] = j
            j += 1  ###!!

        accounts = [x for x in accounts if x[0] != "!xxxx"]

        for i in range(len(accounts)):
            d = list(sorted(set(accounts[i][1:])))
            l = []
            l.append(accounts[i][0])
            accounts[i] = l + d
        return accounts


s = Solution()
p = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
     ["John", "johnsmith@mail.com", "john00@mail.com"],
     ["Mary", "mary@mail.com"],
     ["John", "johnnybravo@mail.com"]]

## reason;;repeated element in one row ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"]
p_wrong_1 = [["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
             ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
             ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
             ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
             ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]]
p_wrong_2 =

p = s.accountsMerge(p_wrong_1)

print(p)

'''
1.
>>> list("abc")
['a', 'b', 'c']
2.
>>> t1 = [1,2,3]
>>> t2 = [4,4]
>>> t1+t2
[1, 2, 3, 4, 4]
3.
>>> t1.append(t2)
>>> t1
[1, 2, 3, [4, 4]]
>>>

'''
