def deleteNode(llist, position):
    # Write your code here
    if llist is None:
        return None
    if llist.next is None:
        return llist
    idx = 0
    if position == idx:
        llist = llist.next
        return llist
    current = llist
    prev = None
    while current:
        if idx == position:
            prev.next = current.next
            current = current.next
            return llist
        else:
            idx += 1
            prev = current
            current = current.next