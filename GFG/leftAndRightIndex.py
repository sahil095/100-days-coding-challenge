def indexes(self, v, x):
    n = len(v)
    idx1 = 0
    flag1 = False
    idx2 = 0
    for i in range(0, n):
        if v[i] == x and flag1 == False:
            idx1 = i
            flag1 = True
            break
    for i in range(idx1, n):
        if v[i] != x:
            idx2 = i-1
            break
        if i == n-1:
            idx2 = i
            break
    if flag1 == False:
        return [-1, -1]
    return [idx1, idx2]