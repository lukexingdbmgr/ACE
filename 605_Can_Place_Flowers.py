class Solution(object):
    def canplace(self, f, i):
        if f[i] != 0:
            return False

        if i == 0:
            if len(f) == 1:
                return True
            else:
                if f[1] == 0:
                    return True
                else:
                    return False

        if i == len(f) - 1:
            if f[-2] == 0:
                return True
            else:
                return False

        return f[i - 1] == 0 and f[i + 1] == 0

    def canPlaceFlowers(self, f, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(f) == 0:
            if n == 0:
                return True
            else:
                return False

        lastpos = -1
        for i in range(len(f)):
            if self.canplace(f, i):
                f[i] = 7
                n -= 1  #### not n--
                if n == 0:
                    return True

        return False
