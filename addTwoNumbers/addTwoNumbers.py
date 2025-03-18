from typing import Optional
from __future__ import annotations

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insertAtBegin(self, val: int, next: 'ListNode'):
        pass

    def insertAtIndex(self, val: int, next: 'ListNode'):
        pass


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1.val)
 
def main():
    number1 = [1, 2, 3]
    number2 = [5, 6, 4]

    ListNode

    soln = Solution()
    intSum = soln.addTwoNumbers(l1, l2)
    # print(intSum)


if __name__ == '__main__':
    main()
