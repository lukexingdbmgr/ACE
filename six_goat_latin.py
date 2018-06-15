class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        i = 0
        while i < len(words):
            if words[i][0] not in ['a', 'e', 'i', 'o', 'u']:
                words[i] += 'ma'
            else:
                c = words[i][0]
                print("c=", c)
                words[i] = words[i][1:] + c + 'ma'
            # i+=1 out of index ???
            words[i] += 'a' * (i + 1)
            i += 1

        return ' '.join(words)


s = Solution()
s.toGoatLatin("speak Goat Latin")
