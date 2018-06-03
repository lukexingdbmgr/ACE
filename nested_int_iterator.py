
'''

l = [1,2,3,[[4,5,6], 7]]

[1 2 3]

pop()
[[4,5,6], 7]

[4,5,6], 7

pop()
[4 5 6]

4 5 6 7

>>> d.extendleft(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> d.appendleft(1)
>>>
>>>
>>> d.extendleft([1])
>>>
>>>
>>> d
deque([1, 1])
>>> d
deque([0])
>>>
>>>
>>> d.append(0)
>>> d
deque([0, 0])
>>> d.pop()
0
>>> d
deque([0])
>>>
>>>
>>> d.appendleft(1)
>>> d
deque([1, 0])
>>> d.popleft()
1
>>> d
deque([0])
>>>


'''

class getNext():

    def __init__(self, l):
        self.q = []
        for c in l:
            self.q.append(c)

    def next(self):
        while(len(self.q) and type(self.q[0]) is list):
            e = self.q.pop(0)
            for i in reversed(e):
                self.q.insert(0, i)
        if self.q:
            return self.q.pop(0)
        else:
            raise "No record"

    def hasNext(self):
        return len(self.q) > 0



import collections
d = collections.deque()
d.insert(0, 10)
c = d[0]
d.pop()


class getNext2():
    def __init__(self, l):
        self.d = collections.deque()
        for c in l:
            self.d.append(c)

    def next(self):
        while(self.d and type(self.d[0]) is list):
            e = self.d.popleft()
            for i in reversed(e):### [4,5,6] -> [6 ..] [5, 6...] [4,5,6 ...]
                self.d.appendleft(i)
        if self.d:
            return self.d.popleft()
        else:
            raise "no record"

    def hasNext(self):
        return len(self.d)


t = [1,2,3,[[4,15,6], 97]]
t1 = [[[[[],[-1], [t]]]]]

c = getNext2(t)

while(c.hasNext()):
    print(c.next())




