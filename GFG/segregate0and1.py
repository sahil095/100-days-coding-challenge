def segregate0and1(self, arr, n):
    left, right = 0, n-1
  
    while left < right: 
        
        while arr[left] == 0 and left < right: 
            left += 1

        while arr[right] == 1 and left < right: 
            right -= 1

        if left < right: 
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1
    return arr


################# OR ################

# def segregate0and1(self, arr, n):
#     arr = srr.sort()
#     return arr