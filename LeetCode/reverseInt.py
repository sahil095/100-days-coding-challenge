def reverse(self, x: int) -> int:
    rev = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x != 0:
        rem = x % 10
        x = x // 10

        if rev > 2**31//10 or (rev == 2**31//10 and rem > 7):
            return 0
        if rev < -2**31//10 or (rev == -2**31//10 and rem < -8):
            return 0
        
        rev = rev * 10 + rem
    return sign * rev