def longestCommonPrefix(self, arr, n):
    res = arr[0]
    l = len(res)
    for i in range(1, len(arr)):
        while arr[i].find(res) != 0:
            res = res[:l - 1]
            l -= 1
            
            if not res:
                return "-1"
    return res