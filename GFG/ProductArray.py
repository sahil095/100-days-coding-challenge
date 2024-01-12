def productExceptSelf(self, nums, n):
    if n == 1:
        return [1]
    res = [1 for i in range(n)]
    i, p = 1, 1
    
    for i in range(n):
        res[i] = p
        p *= nums[i]
    p = 1
    for i in range(n-1, -1, -1):
        res[i] *= p
        p *= nums[i]
    return res