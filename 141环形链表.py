# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 时间效率太低
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ans = False
        data = []
        while head:
            if head not in data:
                data.append(head)
                head = head.next
            else:
                ans = True
                break
        return ans

class Solution(object):
    # 哈希表
    def hasCycle(self, head):
        ans = False
        info = {}
        while head:
            if info.get(id(head), None):
                return True
            else:
                info[id(head)] = head
                head = head.next
        return ans