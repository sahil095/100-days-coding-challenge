def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    if text1 == text2:
        return len(text1)
    
    m = len(text1)
    n = len(text2)
    L = [[None]*(m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif text2[i-1] == text1[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[n][m]