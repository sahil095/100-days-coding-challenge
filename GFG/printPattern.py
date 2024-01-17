def pattern(self, N):
    res = []
    X = N
    res.append(X)
    while X > 0:
        X -= 5
        res.append(X)
    while X != N:
        X += 5
        res.append(X)
    return res