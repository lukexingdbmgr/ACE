## python throw exceptions
import heapq
from  collections import OrderedDict


class maxHeap():
    def __init__(self):
        self.q = []

    def put(self, elem):
        key, value = elem
        heapq.heappush(self.q, (key * -1, value))

    def get(self):
        if len(self.q) != 0:
            heapq.heappop()

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
        self.k = 0
        self.q = maxHeap()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.k += 1
        self.dict[self.k] = x
        ## time complity log(n)
        self.q.put((x, self.k))

    def pop(self):
        """
        :rtype: int
        """
        k, v = self.dict.popitem(last=True)
        e = (v, k)
        self.q.remove(e)
        return v

    def top(self):
        """
        :rtype: int
        """

        L = list(self.dict.items())
        k, v = L[-1]
        return v

    def peekMax(self):
        """
        :rtype: int
        """
        k, v = self.q.getMax()
        return k * -1

    ## need to track the new max
    def popMax(self):
        """
        :rtype: int
        """
        k, v = self.q.peekMax()
        self.dict.pop(v)
        self.q.pop()
        return v

if __name__ == "__main__":
    s = MaxStack()
    s.push(5)
    s.push(1)
    s.push(-5)

    c = s.popMax()
    c = s.peekMax()
    c = s.top()
