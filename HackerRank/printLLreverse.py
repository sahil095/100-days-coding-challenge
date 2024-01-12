def reversePrint(llist):
    # Write your code here
    if llist is None:
        return None
    if llist.next is None:
        return None
    stack = []
    while llist:
        stack.append(llist)
        llist = llist.next
    while len(stack):
        print(stack.pop().data)