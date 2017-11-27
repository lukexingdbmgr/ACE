class key_value():
    def __int__(self, k, v):
        self.key = k
        self.value = v

    def __lt__(self, other):
        if self.key == other.key:
            return self.value > other.value
        else:
            return self.key < other.key


back
tracking
template
https: // discuss.leetcode.com / topic / 46161 / a - general - approach - to - backtracking - questions - in -java - subsets - permutations - combination - sum - palindrome - partitioning / 2
orderedDict
internal
http: // chenjiee815.github.io / collectionsbiao - zhun - ku - yuan - ma - xue - xi.html
