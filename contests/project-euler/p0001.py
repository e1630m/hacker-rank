import sys


def gsum(n, d):
    q, r = divmod(n, d)
    return d * q * (q + 1) // 2 if r else d * q * (q - 1) // 2

    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(gsum(n, 3) + gsum(n, 5) - gsum(n, 15))
