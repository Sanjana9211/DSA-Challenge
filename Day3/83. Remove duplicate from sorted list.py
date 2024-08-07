# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next==None:
            return head
        temp=head
        temp=temp.next
        prev=head
        
        while(temp.next!=None):
            if temp.val == prev.val:
                temp=temp.next
                prev.next=temp
            else:
                temp=temp.next
                prev=prev.next
        if temp.val==prev.val:
            prev.next=None

        return head

        
