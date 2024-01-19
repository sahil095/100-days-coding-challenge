####### Hashing #######
def majorityElement(self, A, N):
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    for key in d:
        if d[key] > N//2:
            return key
    return -1