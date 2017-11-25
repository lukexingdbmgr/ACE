## python throw exceptions


from  collections import OrderedDict


class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dict = OrderedDict()
        self.k = 0
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.k += 1
        self.dict[self.k] = x

        if len(self.q) == 0:
            ## value -> key
            self.q.append((self.k, x))
        else:
            v, k = self.q[-1]
            if x >= v:
                self.q.append((self.k, x))

    def pop(self):
        """
        :rtype: int
        """
        k, v = self.dict.popitem(last=True)
        q_k, q_v = self.q[-1]

        if k == q_k:
            self.q.pop(-1)
        return v

    def top(self):
        """
        :rtype: int
        """

        for c, t in self.dict.items():
            return t

            # (c, _) = self.dict.items()
            # return c

    def peekMax(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return
        q_k, q_v = self.q[-1]
        return q_v

    def popMax(self):
        """
        :rtype: int
        """
        q_k, q_v = self.q[-1]
        self.dict.pop(q_k)
        self.q.pop()
        return q_v



if __name__ == "__main__":
    d = OrderedDict()
    d[1] = 10
    d[2] = 11
    d[3] = 15
    t = d.popitem(last=True)
    print("pop = ", t)

    (c, _) = d.items()

    print(c)

    print(d)
