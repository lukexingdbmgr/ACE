class Solution(object):
    def getFactor_help(self, n, factors, res):
        i = None
        if factors == None:
            i = 2
        else:
            i = factors[-1]

        while i <= n / i:
            if n % i == 0:
                factors.append(i)
                factors.append(n / i)
                res.apeend(factors)

                factors.pop()  ### pop n/i
                self.getFactor(n / i, factors, res)
                factors.pop()  ## pop i

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        factors = []
        res = []

        self.getFactor_help(n, factors, res)
        return res
