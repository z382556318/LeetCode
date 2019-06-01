# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add(self, x, y, carry):
        tmp = x + y + carry
        if tmp >= 10:
            carry = 1
            tmp -= 10
        else:
            carry = 0
        return tmp, carry

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1

        cur = head = None
        carry = 0
        while l1 and l2:
            tmp, carry = self.add(l1.val, l2.val, carry)
            if not head:
                cur = head = ListNode(tmp)
            else:
                cur.next = ListNode(tmp)
                cur = cur.next
            l1 = l1.next
            l2 = l2.next

        if l1 is None:
            while l2 and carry == 1:
                tmp, carry = self.add(0, l2.val, carry)
                cur.next = ListNode(tmp)
                cur = cur.next
                l2 = l2.next
            else:
                if l2:
                    cur.next = l2
                elif carry == 1:
                    cur.next = ListNode(1)
        elif l2 is None:
            while l1 and carry == 1:
                tmp, carry = self.add(0, l1.val, carry)
                cur.next = ListNode(tmp)
                cur = cur.next
                l1 = l1.next
            else:
                if l1:
                    cur.next = l1
                elif carry == 1:
                    cur.next = ListNode(1)
        return head



if __name__ == '__main__':
    a = [9,8]
    b = [1]

    l1 = ListNode(9)
    l1.next = ListNode(8)

    l2 = ListNode(1)

    head = Solution().addTwoNumbers(l1,l2)
    while head:
        print(head.val)
        head = head.next