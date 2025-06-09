import sys

input = sys.stdin.readline

def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

A, B = map(int, input().split())
print('1' * gcd(A, B))
