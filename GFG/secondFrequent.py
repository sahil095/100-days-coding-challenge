def secFrequent(self, arr, n):
    d = {}
    for s in arr:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return sorted(d, key=d.get, reverse=True)[1]