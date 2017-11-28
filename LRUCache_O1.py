import time


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
        # 1 special position
        ## 1.1 do not need to change; at the right place
        ## 1.2 at the tail of the linked list; need to update the tail
        #2 after insert at special position --> update the tail
        if lnd.prev != self.link_head:
            if self.tail == lnd:
                self.tail = lnd.prev
            ## make sure it is unlinked
            ####nd = lnd.unlink()
            nd = lnd

            first = self.link_head.next

            self.link_head.next = nd
            nd.prev = self.link_head
            nd.next = first

            ## sanity test for first;
            if first:
                first.prev = nd
            else:
                ## this is the first real element
                self.tail = nd
                ##else: as already in the correct position -> do nothing

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

            expired = e.get('expired', None)
            if expired != None:
                if expired < time.time() * 1000000:  ## if timeout, unlink and delete
                    if self.tail == lnd:  ## adjust tail
                        self.tail = lnd.prev
                    self.d.pop(key, None)  ## dictionary remove this key
                    t = lnd.unlink()
                    del (t)
                    return -1

            self.touch(lnd)
            return res

    def evict(self):
        t = self.tail
        self.tail = t.prev
        t = t.unlink()
        tail_key = t.value
        self.d.pop(tail_key, None)
        del (t)

    def put(self, key, value, ttl=None):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0:
            raise "cap not is 0"
        v = self.d.get(key, None)

        ## if reach
        if len(self.d) == self.cap and v == None:
            self.evict()

        if self.d.get(key, None) != None:
            e = self.d[key]
            e["value"] = value
            lnd = e["link"]
            self.touch(lnd)
        else:
            new_node = LinkNode(key)
            self.touch(new_node)

            expired = None
            self.d[key] = {
                "value": value,
                "link": new_node
            }

        ## handle the timeout for this key
        hash_e = self.d[key]
        if ttl:
            expired = time.time() * 1000000 + ttl
            hash_e["expired"] =  expired



class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
