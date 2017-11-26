## python throw exceptions
import heapq
from  collections import OrderedDict


class key_value():
    def __init__(self, k, v):
        self.key = k
        self.value = v

    def __lt__(self, other):
        if self.key == other.key:
            return self.value > other.value
        else:
            return self.key < other.key

    def __eq__(self, other):
        return self.value == other.value

class maxHeap():
    def __init__(self):
        self.q = []

    def put(self, elem):
        newelem = key_value(elem.key * -1, elem.value)
        heapq.heappush(self.q, newelem)

    def pop(self):
        if len(self.q) != 0:
            return heapq.heappop(self.q)  ####

    def remove(self, elem):
        i = 0
        for i in range(len(self.q)):
            if self.q[i] == elem:
                self.q.remove(elem)
                break
        heapq.heapify(self.q)

    def getMax(self):
        return self.q[0]


class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dict = OrderedDict()
        self.k = None
        self.q = maxHeap()
        self.i = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        self.i += 1
        self.k = "step: " + str(self.i)

        self.dict[self.k] = x
        ## time complity log(n)
        self.q.put(key_value(x, self.k))

    def pop(self):
        """
        :rtype: int
        """
        k, v = self.dict.popitem(last=True)  # o1
        self.q.remove(key_value(k=v, v=k))  # o(logn)
        return v

    def top(self):
        """
        :rtype: int
        """
        ## time O(N) to see the orderedDict source code
        L = list(self.dict.items())
        k, v = L[-1]
        return v

    ### return max value * -1 with largest step
    def _peekMax(self):
        return self.q.getMax()

    def peekMax(self):
        """
        :rtype: int
        """
        kv = self._peekMax()
        return kv.key * (-1)

    ## need to track the new max
    def popMax(self):
        """
        :rtype: int
        """
        ## k is the real value
        ## v is the routing_key
        kv = self._peekMax()
        self.dict.pop(kv.value)
        self.q.pop()
        return kv.key * -1

if __name__ == "__main__":
    s = MaxStack()
    s.push(5)
    s.push(1)
    s.push(5)

    c = s.top()
    c = s.popMax()
    c = s.top()
    c = s.peekMax()
    c = s.pop()
    c = s.top()
