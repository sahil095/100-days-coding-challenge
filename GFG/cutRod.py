######################## DP Iteraative ################################

def cutRod(prices, n):
    mat = [[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1:
                mat[i][j] = j*prices[i-1]
            else:
                if i > j:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = max(prices[i-1]+mat[i][j-i], mat[i-1][j])
    return mat[n][n]


######################## OR DP bottom up (GFG Accepted) ################################

def cutRod(self, price, n):
    INT_MIN = -32767
    val = [0 for x in range(n+1)]
    val[0] = 0
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
 
    return val[n]

