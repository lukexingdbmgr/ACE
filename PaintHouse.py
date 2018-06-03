class Solution(object):
    def minCost(self, cost):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        if (len(cost) == 0 or len(cost[0]) == 0):
            return 0

        L = len(cost)

        for i in range(1, L):
            '''
            cost[row][col]
                row : len(cost)
                col : len(cost[0])
                
            for house i we try 3 possible paint solutios:
                if we paint with color 0, 
                    then the last house can only have two options: color 1 and color 2
                    so the overall solution is min((i-1, 1), (i-1, 2))
                    +
                    cost of house[i] with color k (old)
            '''
            cost[i][0] = cost[i][0] + min(cost[i - 1][1], cost[i - 1][2])
            cost[i][1] = cost[i][1] + min(cost[i - 1][0], cost[i - 1][2])
            cost[i][2] = cost[i][2] + min(cost[i - 1][0], cost[i - 1][1])

        ## the last house have 3 options;
        ## all of the painting options in 3 buckets
        ## find the min of 3
        return min(cost[L - 1][0], min(cost[L - 1][1], cost[L - 1][2]))


if __name__ == "__main__":
    s = Solution()
    cost = [[7, 6, 2]]
    s.minCost(cost)
