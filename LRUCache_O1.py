class LinkNode(object):
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

    def unlink(self):
        if self.prev == None and self.value == float('inf'):
            return
        p = self.prev
        n = self.next

        if p != None:
            p.next = n
        if n != None:
            n.prev = p

        self.prev = None
        self.next = None
        return self


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.link_head = LinkNode(float('inf'))
        self.tail = self.link_head
        self.d = {}

    def touch(self, lnd):
        ## corner case: if there is only one element in the list
        if lnd.prev != self.link_head:
            if self.tail == lnd:
                self.tail = lnd.prev

            nd = lnd.unlink()
            first = self.link_head.next

            self.link_head.next = nd
            nd.prev = self.link_head
            nd.next = first

            if first:
                first.prev = nd
            else:
                self.tail = nd

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.d.get(key, None) == None:
            return -1
        else:
            e = self.d[key]
            res = e["value"]
            lnd = e["link"]

            self.touch(lnd)
            return res

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0:
            raise "cap not is 0"
        v = self.d.get(key, None)

        ## if the key already exist ; do not need to evict any elements
        if len(self.d) == self.cap and v == None:
            ### reach capacity

            t = self.tail
            self.tail = t.prev
            t = t.unlink()
            tail_key = t.value
            self.d.pop(tail_key, None)
            del (t)

        if self.d.get(key, None) != None:
            e = self.d[key]
            e["value"] = value
            lnd = e["link"]
            self.touch(lnd)
        else:
            new_node = LinkNode(key)
            self.touch(new_node)
            self.d[key] = {
                "value": value,
                "link": new_node
            }
