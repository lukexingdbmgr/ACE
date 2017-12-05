import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        forward = {beginWord}
        backward = {endWord}
        wordSet = set(wordList)

        res = 2

        while (forward and backward):
            if len(forward) > len(backward):
                forward, backward = backward, forward

            nexx = set()
            for word in forward:
                for i in range(0, len(word)):
                    # word = "abcde"
                    # i = 0 => first = [], second = bcde
                    # i = len -1 => first = abcd, second = []
                    first, second = word[:i], word[i + 1:]
                    for c in string.ascii_lowercase:
                        cand = first + c + second
                        ## test in small set first
                        if cand in backward:
                            return res
                        ## then test in bigger set
                        if cand in wordSet:
                            nexx.add(cand)
                            wordSet.discard(cand)
            ##traverse all for all the children, if no next level give up.
            if len(nexx) == 0:
                return 0
            forward = nexx
            res += 1

        return 0
