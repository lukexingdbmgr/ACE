'''
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        cur = ['']

        for i in S:
            ret = []
            for item in cur:
                if i.isdigit():
                    #cur += i
                    ret.append(item + i)
                else:
                    ret.append(item + i)
                    if i.isupper(): <<<<<<<<<<<<<<
                        ret.append(item + chr(ord(i) + 32)) <<<<<<<<<<<< int to char
                    else:
                        ret.append(item + chr(ord(i) - 32))
            cur = ret

        return cur
'''


class Solution(object):

    def letterp(self, s_list, res, i):
        res.append("".join(s_list))
        p = i
        while (p < len(s_list)):  ## this is clever to do so
            c = s_list[p]
            if s_list[p].isalpha():
                if s_list[p].isupper():
                    s_list[p] = s_list[p].lower()
                elif s_list[p].islower():
                    s_list[p] = s_list[p].upper()
                #### only go to next level when s_list[p] is alpha()
                self.letterp(s_list, res,
                             p + 1)  ### use interator ref https://github.com/lukexingdbmgr/ACE/blob/master/subSets.py#L46
                s_list[p] = c
            p += 1

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s_list = list(S)
        res = []
        self.letterp(s_list, res, 0)
        return res
