# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        val = []
        while self != None:
            val.append(self.val)
            self = self.next
        return str(val)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = current = ListNode(0)
        val = 0
        while l1 or l2 or val:
            if l1:
                val = val + l1.val
                l1 = l1.next
            if l2:
                val = val + l2.val
                l2 = l2.next
            current.next = ListNode(val%10)
            current = current.next
            val = val // 10
        return dummy.next
        

if __name__ == "__main__":
    l1 = ListNode(0)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    #l1.next.next.next = ListNode(7)

    l2 = ListNode(0)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
        
    s = Solution()
    print s.addTwoNumbers(l1, l2)
