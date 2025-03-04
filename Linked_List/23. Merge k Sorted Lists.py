class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(heap,(l.val,i))
        dummy = curr = ListNode()
        while heap:
            val, i = heapq.heappop(heap)
            curr.next = ListNode(val= val)
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i))
        return dummy.next