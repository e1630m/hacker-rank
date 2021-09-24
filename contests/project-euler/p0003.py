import sys


def pfactor(n):
    i, div = 2, n
    while i ** 2 <= div:
        if div % i:
            i += 1
        else:
            div //= i
    return div


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(pfactor(n))
