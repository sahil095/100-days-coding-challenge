def findExtra(self,a,b,n):
    #add code here
    sum_a = sum(a)
    sum_b = sum(b)
    diff = sum_a - sum_b
    idx = a.index(diff)
    return idx