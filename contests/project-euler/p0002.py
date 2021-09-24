import sys


def fib(n):
    a, b = 1, 2
    t = 2
    while 1:
        a, b = b, a + b
        if b > n:
            return t
        if b % 2 == 0:
            t += b

            
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fib(n))
