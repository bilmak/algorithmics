from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next=next
     
class Solution:   
    def add_Two_numbers_linked_list(self, l1:Optional[ListNode], l2: Optional[ListNode])->ListNode:
        dummy = ListNode(0)
        carry = 0
        current = dummy
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            #new digit
            total = val1+val2+carry
            carry = total//10
            total = total%10
            current.next = ListNode(total)
            #update‹
            current = current.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
    
    
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution = Solution()
result = solution.add_Two_numbers_linked_list(l1, l2)
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

print_linked_list(result)