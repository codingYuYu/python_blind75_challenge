# 使用dummy node 技巧
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val > p2.val:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
            else:
                curr.next = p1
                curr = curr.next
                p1 = p1.next

        if p1:
            curr.next = p1
        if p2:
            curr.next = p2

        return dummy.next

'''
步驟 1: 建立 dummy
dummy → [None]
curr  → [None]

    dummy = ListNode()
    curr = dummy
    不是建立兩個不同的 ListNode，而是讓 curr 指向 dummy，它們實際上指向的是 同一個記憶體位址，如下所示：
    dummy (記憶體位址: 0x1234) → [ListNode(val=None, next=None)]
    curr  (記憶體位址: 0x1234) → [ListNode(val=None, next=None)]

步驟 2: curr.next = ListNode(1)
dummy → [None] ─→ [1]
curr        └────────→ [1]

步驟 3: curr = curr.next
dummy → [None] ─→ [1]
curr        └────────→ [1]

步驟 4: curr.next = ListNode(2)
dummy → [None] ─→ [1] ─→ [2]
curr        └────────────→ [2]

步驟 5: curr = curr.next
dummy → [None] ─→ [1] ─→ [2]
curr        └────────────→ [2]

步驟 6: curr.next = ListNode(3)
dummy → [None] ─→ [1] ─→ [2] ─→ [3]
curr        └──────────────→ [3]
'''

# 不使用dummy node 技巧
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:  # 若 list1 為空，直接回傳 list2
            return list2
        if not list2:  # 若 list2 為空，直接回傳 list1
            return list1

        # 確保 head 指向較小的那個節點
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        curr = head  # `curr` 指向目前的最後一個節點

        # 開始合併剩餘的節點
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next  # 移動 `curr`

        # 剩餘的節點直接接上
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return head  # 回傳合併後的鏈表頭部
