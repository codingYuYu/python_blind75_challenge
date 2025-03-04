# Tortoise and Hare (fast and slow pointers):
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False


# Use Set to remember visited values:
class Solution(object):
    def hasCycle(self, head):
        visited = set()

        while head:
            if head.val in visited:
                return True
            visited.add(head.val)
            head = head.next

        return False