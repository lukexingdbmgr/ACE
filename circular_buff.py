
'''

1 2 3
i

'''
import threading

class circularBuffer:
    def dump(self):
        s = str()
        for c in self.buff:
            s += (str(c) + "_")
        print(s)

    def __init__(self, capacity):
        self.buff = [0] * capacity
        self.size = 0
        self.capacity = capacity
        self.head_index = 0
        self.tail_index = 0
        self.dump()

    def push_element(self, x):
        if self.size == self.capacity:
            raise Exception("the queue is full")
        self.buff[self.tail_index] = x
        self.tail_index = (self.tail_index + 1) % self.capacity
        self.size += 1
        self.dump()

    def pop_element(self):
        if self.size == 0:
            raise Exception("the queue is empty")
        ret = self.buff[self.head_index]
        self.head_index = (self.head_index + 1) % self.capacity
        self.size -= 1
        self.dump()


t = circularBuffer(3)

for c in range(1, 4):
    t.push_element(c)

t.pop_element()
t.push_element(7)
t.pop_element()
t.push_element(8)
t.pop_element()