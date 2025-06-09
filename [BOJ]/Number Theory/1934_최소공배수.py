import sys

input = sys.stdin.readline

def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(a * b // g) 
