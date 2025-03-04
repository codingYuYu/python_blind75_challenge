class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast = slow = dummy

        # fast先走n步
        for i in range(n+1):
            fast = fast.next

        # fast & slow一起走
        # fast 走完
        # slow 會剩下 n 個 node
        while fast:
            fast = fast.next
            slow = slow.next

        # 讓slow 跳過要刪除的節點
        slow.next = slow.next.next

        return dummy.next