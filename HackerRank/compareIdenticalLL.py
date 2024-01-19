def compare_lists(llist1, llist2):
    if llist1 is None or llist2 is None:
        return None
    while llist1 != None and llist2 != None:
        print(llist1.data)
        print(llist2.data)
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    return (llist1 == None and llist2 == None) 