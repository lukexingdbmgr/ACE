class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0:
            return 0
        ###trap
        if n < 0:
            return 1 / self.myPow(x, -n)
        ###trap

        p1 = self.myPow(x, n / 2)
        if n % 2 == 0:
            return p1 * p1
        else:
            return p1 * p1 * x
