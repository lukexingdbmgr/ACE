class Solution(object):
    def minCost(self, cost):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        if (len(cost) == 0 or len(cost[0]) == 0):
            return 0

        for i in range(1, len(cost[0])):
            '''
            case 1 : paint use color 0:
                    the sum from house[0] to house[i] when house [i]  use color 0 = cost of house[i] using color 0 + min(cost from house i to (i-1) use when house i -1 use color 1, cost from house i to (i-1) when house i - 1 use color 2)

                    if house[i] use color 0 then the previous one can only use 1 or 2
            '''
            cost[i][0] = cost[i][0] + min(cost[i - 1][1], cost[i - 1][2])
            cost[i][1] = cost[i][1] + min(cost[i - 1][0], cost[i - 1][2])
            cost[i][2] = cost[i][2] + min(cost[i - 1][0], cost[i - 1][1])

        l = len(cost[0])

        return min(cost[l - 1][0], min(cost[l - 1][1], cost[l - 1][2]))


if __name__ == "__main__":
    s = Solution()
    cost = [[7, 6, 2]]
    s.minCost(cost)
