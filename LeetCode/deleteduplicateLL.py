def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return None
    if head.next == None:
        return head
    first = head
    second = head.next
    while second != None:
        if first.val == second.val:
            first.next = second.next
            second = second.next
        else:
            first = first.next
            second = second.next
    return head