# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fp=head
        sp=head
        while(sp!=None and sp.next!=None):
            fp=fp.next
            sp=sp.next.next
        return fp
