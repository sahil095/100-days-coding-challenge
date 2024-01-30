def getMoneySpent(keyboards, drives, b):
    max_sum = 0
    n = len(keyboards)
    m = len(drives)
    for i in range(n):
        for j in range(m):
            t = keyboards[i] + drives[j]
            if max_sum < t and t <= b:
                max_sum = t
    if max_sum == 0:
        return -1
    return max_sum