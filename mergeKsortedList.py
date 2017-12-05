# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:  #### trap
                heapq.heappush(heap, (node.val, node))

        dummy = ListNode(-1)

        curr = dummy
        while (len(heap) != 0):
            v, nd = heapq.heappop(heap)
            curr.next = nd
            curr = curr.next

            if nd.next:
                heapq.heappush(heap, (nd.next.val, nd.next))

        return dummy.next
